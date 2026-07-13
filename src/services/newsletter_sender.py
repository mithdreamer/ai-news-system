import html
import os
from datetime import datetime
from typing import Any

import resend


def build_newsletter_html(
    categorized_news: list[dict[str, Any]],
    stats: dict[str, Any],
) -> str:
    """Haberleri kategorilere ayırarak HTML e-posta oluşturur."""

    category_settings = {
        "ekonomi": {
            "label": "Ekonomi",
            "icon": "💰",
        },
        "teknoloji": {
            "label": "Teknoloji",
            "icon": "🤖",
        },
        "dünya": {
            "label": "Dünya",
            "icon": "🌍",
        },
        "gümrük": {
            "label": "Gümrük",
            "icon": "🛃",
        },
        "genel": {
            "label": "Genel",
            "icon": "📰",
        },
    }

    grouped_news: dict[str, list[dict[str, Any]]] = {}

    for item in categorized_news:
        category = str(item.get("category", "genel")).strip().lower()

        grouped_news.setdefault(category, [])
        grouped_news[category].append(item)

    category_sections = []

    for category_key in [
        "teknoloji",
        "ekonomi",
        "dünya",
        "gümrük",
        "genel",
    ]:
        category_news = grouped_news.get(category_key, [])

        if not category_news:
            continue

        settings = category_settings.get(
            category_key,
            {
                "label": category_key.title(),
                "icon": "📰",
            },
        )

        news_cards = []

        for item in category_news:
            title = html.escape(
                str(item.get("title", "Başlıksız haber"))
            )

            summary = html.escape(
                str(item.get("summary", ""))
            )

            url = html.escape(
                str(item.get("link", "#")),
                quote=True,
            )

            news_cards.append(
                f"""
                <div style="
                    border-bottom: 1px solid #e5e7eb;
                    padding: 20px 0;
                ">
                    <a
                        href="{url}"
                        style="
                            color: #111827;
                            display: block;
                            font-size: 18px;
                            font-weight: 700;
                            line-height: 1.4;
                            margin-bottom: 10px;
                            text-decoration: none;
                        "
                    >
                        {title}
                    </a>

                    <p style="
                        color: #4b5563;
                        font-size: 14px;
                        line-height: 1.7;
                        margin: 0 0 14px;
                    ">
                        {summary}
                    </p>

                    <a
                        href="{url}"
                        style="
                            background-color: #111827;
                            border-radius: 6px;
                            color: #ffffff;
                            display: inline-block;
                            font-size: 13px;
                            font-weight: 700;
                            padding: 10px 16px;
                            text-decoration: none;
                        "
                    >
                        Haberi Oku →
                    </a>
                </div>
                """
            )

        category_sections.append(
            f"""
            <section style="margin-top: 34px;">
                <h2 style="
                    border-bottom: 2px solid #111827;
                    color: #111827;
                    font-size: 22px;
                    margin: 0;
                    padding-bottom: 10px;
                ">
                    {settings["icon"]} {settings["label"]}
                </h2>

                {''.join(news_cards)}
            </section>
            """
        )

    generated_at = html.escape(
        str(stats.get("generated_at", ""))
    )

    total_news = html.escape(
        str(
            stats.get(
                "toplam_haber",
                len(categorized_news),
            )
        )
    )

    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width">
        <title>Günün Haberleri</title>
    </head>

    <body style="
        background-color: #f3f4f6;
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 24px 12px;
    ">
        <div style="
            background-color: #ffffff;
            border-radius: 12px;
            margin: 0 auto;
            max-width: 680px;
            padding: 32px;
        ">
            <header style="
                border-bottom: 1px solid #e5e7eb;
                padding-bottom: 24px;
            ">
                <div style="
                    color: #2563eb;
                    font-size: 13px;
                    font-weight: 700;
                    letter-spacing: 1px;
                    text-transform: uppercase;
                ">
                    AI Haber Yayın Sistemi
                </div>

                <h1 style="
                    color: #111827;
                    font-size: 32px;
                    margin: 10px 0;
                ">
                    Günün Haberleri
                </h1>

                <p style="
                    color: #6b7280;
                    font-size: 14px;
                    line-height: 1.6;
                    margin: 0;
                ">
                    {generated_at} tarihinde hazırlanan
                    {total_news} haberlik günlük özet.
                </p>
            </header>

            {''.join(category_sections)}

            <footer style="
                border-top: 1px solid #e5e7eb;
                color: #9ca3af;
                font-size: 12px;
                line-height: 1.6;
                margin-top: 36px;
                padding-top: 20px;
                text-align: center;
            ">
                Bu e-posta AI Haber Yayın Sistemi tarafından
                otomatik olarak oluşturuldu.
            </footer>
        </div>
    </body>
    </html>
    """


def send_newsletter(
    categorized_news: list[dict[str, Any]],
    stats: dict[str, Any],
) -> dict[str, Any]:
    """HTML bülteni ortam değişkenlerindeki sabit alıcıya gönderir."""

    api_key = os.getenv("RESEND_API_KEY")
    recipient = os.getenv("NEWSLETTER_TO")
    sender = os.getenv(
        "NEWSLETTER_FROM",
        "AI News <onboarding@resend.dev>",
    )

    if not api_key:
        raise RuntimeError("RESEND_API_KEY tanımlı değil.")

    if not recipient:
        raise RuntimeError("NEWSLETTER_TO tanımlı değil.")

    resend.api_key = api_key

    subject_date = datetime.now().strftime("%d.%m.%Y")
    newsletter_html = build_newsletter_html(categorized_news, stats)

    params: resend.Emails.SendParams = {
        "from": sender,
        "to": [recipient],
        "subject": f"Günün Haberleri - {subject_date}",
        "html": newsletter_html,
    }

    print("Resend API çağrısı yapılıyor...")

    response = resend.Emails.send(params)

    print("Resend cevabı:", response)

    return response