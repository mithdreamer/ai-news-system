import re


def clean_html(text):
    if not text:
        return ""

    clean_text = re.sub(
        r"<.*?>",
        "",
        text
    )

    return clean_text


def clean_spaces(text):
    if not text:
        return ""

    return " ".join(
        text.split()
    )


def clean_news_item(item):
    item["title"] = clean_spaces(
        item.get("title", "")
    )

    item["summary"] = clean_spaces(
        clean_html(
            item.get("summary", "")
        )
    )

    return item


def clean_news(news_items):
    cleaned_news = []

    for item in news_items:
        cleaned_item = clean_news_item(item)
        cleaned_news.append(cleaned_item)

    return cleaned_news