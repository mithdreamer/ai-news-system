import html
import os
from datetime import datetime
from typing import Any

import resend


def build_newsletter_html(
    categorized_news: list[dict[str, Any]],
    stats: dict[str, Any],
) -> str:
    """Haberleri kategorilere ayırarak profesyonel HTML bülteni oluşturur."""

    category_settings = {
        "teknoloji": {
            "label": "Teknoloji",
            "icon": "🤖",
            "color": "#2563eb",
            "background": "#eff6ff",
        },
        "ekonomi": {
            "label": "Ekonomi",
            "icon": "💰",
            "color": "#047857",
            "background": "#ecfdf5",
        },
        "dünya": {
            "label": "Dünya",
            "icon": "🌍",
            "color": "#4338ca",
            "background": "#eef2ff",
        },
        "gümrük": {
            "label": "Gümrük",
            "icon": "🛃",
            "color": "#c2410c",
            "background": "#fff7ed",
        },
        "genel": {
            "label": "Genel",
            "icon": "📰",
            "color": "#374151",
            "background": "#f3f4f6",
        },
    }

    normalized_news: list[dict[str, Any]] = []
    grouped_news: dict[str, list[dict[str, Any]]] = {}

    for item in categorized_news:
        category = str(
            item.get("category", "genel")
        ).strip().lower()

        if category not in category_settings:
            category = "genel"

        normalized_item = {
            **item,
            "normalized_category": category,
        }

        normalized_news.append(normalized_item)

        grouped_news.setdefault(category, [])
        grouped_news[category].append(normalized_item)

    category_counts = Counter(
        item["normalized_category"]
        for item in normalized_news
    )

    category_order = [
        "teknoloji",
        "ekonomi",
        "dünya",
        "gümrük",
        "genel",
    ]

    summary_cards: list[str] = []

    total_news = len(normalized_news)

    summary_cards.append(
        f"""
        <td style="padding: 6px;" width="20%">
            <div style="
                background-color: #111827;
                border-radius: 10px;
                color: #ffffff;
                padding: 14px 8px;
                text-align: center;
            ">
                <div style="
                    font-size: 22px;
                    font-weight: 700;
                    line-height: 1;
                ">
                    {total_news}
                </div>

                <div style="
                    font-size: 11px;
                    margin-top: 7px;
                    opacity: 0.85;
                ">
                    Toplam
                </div>
            </div>
        </td>
        """
    )

    for category_key in category_order:
        count = category_counts.get(category_key, 0)

        if count == 0:
            continue

        settings = category_settings[category_key]

        summary_cards.append(
            f"""
            <td style="padding: 6px;" width="20%">
                <div style="
                    background-color: {settings["background"]};
                    border-radius: 10px;
                    color: {settings["color"]};
                    padding: 14px 8px;
                    text-align: center;
                ">
                    <div style="
                        font-size: 20px;
                        line-height: 1;
                    ">
                        {settings["icon"]}
                    </div>

                    <div style="
                        font-size: 18px;
                        font-weight: 700;
                        margin-top: 6px;
                    ">
                        {count}
                    </div>

                    <div style="
                        font-size: 11px;
                        margin-top: 5px;
                    ">
                        {settings["label"]}
                    </div>
                </div>
            </td>
            """
        )

    category_sections: list[str] = []

    for category_key in category_order:
        category_news = grouped_news.get(category_key, [])

        if not category_news:
            continue

        settings = category_settings[category_key]
        news_cards: list[str] = []

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

            source = html.escape(
                str(item.get("source", ""))
            )

            source_html = ""

            if source:
                source_html = f"""
                <div style="
                    color: #9ca3af;
                    font-size: 12px;
                    margin-bottom: 8px;
                ">
                    Kaynak: {source}
                </div>
                """

            news_cards.append(
                f"""
                <tr>
                    <td style="
                        border-bottom: 1px solid #e5e7eb;
                        padding: 22px 0;
                    ">
                        {source_html}

                        <a
                            href="{url}"
                            style="
                                color: #111827;
                                display: block;
                                font-size: 18px;
                                font-weight: 700;
                                line-height: 1.45;
                                margin-bottom: 10px;
                                text-decoration: none;
                            "
                        >
                            {title}
                        </a>

                        <p style="
                            color: #4b5563;
                            font-size: 14px;
                            line-height: 1.75;
                            margin: 0 0 16px;
                        ">
                            {summary}
                        </p>

                        <a
                            href="{url}"
                            style="
                                background-color: {settings["color"]};
                                border-radius: 7px;
                                color: #ffffff;
                                display: inline-block;
                                font-size: 13px;
                                font-weight: 700;
                                padding: 10px 17px;
                                text-decoration: none;
                            "
                        >
                            Haberi Oku →
                        </a>
                    </td>
                </tr>
                """
            )

        category_sections.append(
            f"""
            <table
                role="presentation"
                width="100%"
                cellspacing="0"
                cellpadding="0"
                border="0"
                style="margin-top: 34px;"
            >
                <tr>
                    <td style="
                        background-color: {settings["background"]};
                        border-left: 5px solid {settings["color"]};
                        border-radius: 8px;
                        color: {settings["color"]};
                        font-size: 21px;
                        font-weight: 700;
                        padding: 14px 16px;
                    ">
                        {settings["icon"]} {settings["label"]}
                    </td>
                </tr>

                {''.join(news_cards)}
            </table>
            """
        )

    generated_at = html.escape(
        str(stats.get("generated_at", ""))
    )

    site_url = html.escape(
        os.getenv(
            "NEWSLETTER_SITE_URL",
            "https://mithdreamer.github.io/ai-news-system/",
        ),
        quote=True,
    )

    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >
        <title>AI Haber Bülteni</title>
    </head>

    <body style="
        background-color: #eef2f7;
        font-family: Arial, Helvetica, sans-serif;
        margin: 0;
        padding: 24px 10px;
    ">
        <table
            role="presentation"
            width="100%"
            cellspacing="0"
            cellpadding="0"
            border="0"
        >
            <tr>
                <td align="center">
                    <table
                        role="presentation"
                        width="100%"
                        cellspacing="0"
                        cellpadding="0"
                        border="0"
                        style="
                            background-color: #ffffff;
                            border-radius: 16px;
                            box-shadow: 0 8px 30px rgba(15, 23, 42, 0.08);
                            max-width: 700px;
                            overflow: hidden;
                        "
                    >
                        <tr>
                            <td style="
                                background-color: #111827;
                                padding: 38px 32px;
                                text-align: center;
                            ">
                                <div style="
                                    color: #93c5fd;
                                    font-size: 13px;
                                    font-weight: 700;
                                    letter-spacing: 1.6px;
                                    text-transform: uppercase;
                                ">
                                    AI Haber Yayın Sistemi
                                </div>

                                <h1 style="
                                    color: #ffffff;
                                    font-size: 34px;
                                    line-height: 1.2;
                                    margin: 12px 0;
                                ">
                                    🧠 Günün Haber Bülteni
                                </h1>

                                <p style="
                                    color: #d1d5db;
                                    font-size: 15px;
                                    line-height: 1.6;
                                    margin: 0;
                                ">
                                    Dünyanın önemli gelişmeleri,
                                    tek bir günlük özette.
                                </p>

                                <p style="
                                    color: #9ca3af;
                                    font-size: 13px;
                                    margin: 12px 0 0;
                                ">
                                    {generated_at}
                                </p>
                            </td>
                        </tr>

                        <tr>
                            <td style="padding: 26px 26px 8px;">
                                <h2 style="
                                    color: #111827;
                                    font-size: 18px;
                                    margin: 0 0 12px;
                                ">
                                    Bugünün Özeti
                                </h2>

                                <table
                                    role="presentation"
                                    width="100%"
                                    cellspacing="0"
                                    cellpadding="0"
                                    border="0"
                                >
                                    <tr>
                                        {''.join(summary_cards)}
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <tr>
                            <td style="padding: 0 32px 36px;">
                                {''.join(category_sections)}
                            </td>
                        </tr>

                        <tr>
                            <td style="
                                background-color: #f9fafb;
                                border-top: 1px solid #e5e7eb;
                                padding: 30px 24px;
                                text-align: center;
                            ">
                                <div style="
                                    color: #111827;
                                    font-size: 17px;
                                    font-weight: 700;
                                    margin-bottom: 12px;
                                ">
                                    AI Haber Yayın Sistemi
                                </div>

                                <p style="
                                    color: #6b7280;
                                    font-size: 13px;
                                    line-height: 1.6;
                                    margin: 0 0 18px;
                                ">
                                    Günlük haberleri, arşivi ve
                                    arama sayfasını web sitemizde
                                    inceleyebilirsin.
                                </p>

                                <a
                                    href="{site_url}"
                                    style="
                                        background-color: #2563eb;
                                        border-radius: 8px;
                                        color: #ffffff;
                                        display: inline-block;
                                        font-size: 14px;
                                        font-weight: 700;
                                        padding: 12px 20px;
                                        text-decoration: none;
                                    "
                                >
                                    Haber Sitesini Ziyaret Et
                                </a>

                                <p style="
                                    color: #9ca3af;
                                    font-size: 11px;
                                    line-height: 1.6;
                                    margin: 22px 0 0;
                                ">
                                    Bu e-posta AI Haber Yayın Sistemi
                                    tarafından otomatik oluşturuldu.
                                </p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
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