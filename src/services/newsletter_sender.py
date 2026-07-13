import html
import os
from datetime import datetime
from typing import Any

import resend


def build_newsletter_html(
    categorized_news: list[dict[str, Any]],
    stats: dict[str, Any],
) -> str:
    """Günlük haber verilerinden sade bir HTML e-posta oluşturur."""

    news_items = []

    for item in categorized_news[:10]:
        title = html.escape(str(item.get("title", "Başlıksız haber")))
        summary = html.escape(str(item.get("summary", "")))
        url = html.escape(str(item.get("link", "#")), quote=True)
        category = html.escape(str(item.get("category", "Genel")))

        news_items.append(
            f"""
            <div style="
                border-bottom: 1px solid #e5e7eb;
                padding: 16px 0;
            ">
                <div style="
                    color: #6b7280;
                    font-size: 12px;
                    margin-bottom: 6px;
                    text-transform: uppercase;
                ">
                    {category}
                </div>

                <a href="{url}" style="
                    color: #111827;
                    font-size: 18px;
                    font-weight: 700;
                    text-decoration: none;
                ">
                    {title}
                </a>

                <p style="
                    color: #4b5563;
                    font-size: 14px;
                    line-height: 1.6;
                    margin: 8px 0 0;
                ">
                    {summary}
                </p>
            </div>
            """
        )

    generated_at = html.escape(str(stats.get("generated_at", "")))
    total_news = html.escape(str(stats.get("toplam_haber", len(categorized_news))))

    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Günün Haberleri</title>
    </head>
    <body style="
        background-color: #f3f4f6;
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 24px;
    ">
        <div style="
            background-color: #ffffff;
            border-radius: 12px;
            margin: 0 auto;
            max-width: 680px;
            padding: 32px;
        ">
            <h1 style="color: #111827; margin-top: 0;">
                Günün Haberleri
            </h1>

            <p style="color: #6b7280;">
                {generated_at} tarihinde hazırlanan {total_news} haberlik günlük özet.
            </p>

            {''.join(news_items)}

            <p style="
                color: #9ca3af;
                font-size: 12px;
                margin-top: 28px;
            ">
                Bu e-posta AI Haber Yayın Sistemi tarafından otomatik oluşturuldu.
            </p>
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