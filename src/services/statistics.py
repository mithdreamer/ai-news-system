def generate_statistics(news_items):

    stats = {}

    stats["toplam_haber"] = len(news_items)

    for item in news_items:

        category = item.get(
            "category",
            "genel"
        )

        if category not in stats:
            stats[category] = 0

        stats[category] += 1

    return stats