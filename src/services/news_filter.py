def is_valid_news(item):
    title = item.get("title", "").strip()
    summary = item.get("summary", "").strip()

    if len(title) < 15:
        return False

    if len(summary) < 30:
        return False

    return True


def normalize_title(title):
    return title.lower().strip()


def calculate_importance_score(item):
    title = item.get("title", "").lower()
    summary = item.get("summary", "").lower()

    score = 0

    keywords = [
        "son dakika",
        "açıklandı",
        "kriz",
        "savaş",
        "ekonomi",
        "enflasyon",
        "merkez bankası",
        "dolar",
        "euro",
        "deprem",
        "yangın",
        "teknoloji",
        "yapay zeka",
        "bakan",
        "cumhurbaşkanı",
        "avrupa",
        "amerika",
        "rusya",
        "çin"
    ]

    for keyword in keywords:
        if keyword in title or keyword in summary:
            score += 1

    score += min(len(summary) // 200, 3)

    return score


def filter_news(news_items):
    seen_titles = set()
    filtered_news = []

    for item in news_items:
        if not is_valid_news(item):
            continue

        normalized_title = normalize_title(
            item.get("title", "")
        )

        if normalized_title in seen_titles:
            continue

        seen_titles.add(normalized_title)

        item["importance_score"] = calculate_importance_score(item)

        filtered_news.append(item)

    filtered_news.sort(
        key=lambda x: x.get("importance_score", 0),
        reverse=True
    )

    return filtered_news