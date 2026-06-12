from datetime import datetime


def generate_news_script(news_items, max_items=8):
    today = datetime.now().strftime("%d.%m.%Y")

    selected_news = news_items[:max_items]

    lines = [
        f"Günaydın. Bugün {today}. Günün öne çıkan haber başlıklarıyla karşınızdayız.",
        ""
    ]

    for index, item in enumerate(selected_news, start=1):
        lines.append(f"{index}. {item['title']}")

        if item.get("summary"):
            clean_summary = item["summary"].replace("\n", " ").strip()
            lines.append(clean_summary[:350])

        lines.append("")

    lines.append(
        "Günün öne çıkan gelişmeleri şimdilik bu kadar. "
        "Bir sonraki haber özetinde görüşmek üzere."
    )

    return "\n".join(lines)