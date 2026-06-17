def detect_category(item):
    title = item.get("title", "").lower()
    summary = item.get("summary", "").lower()

    text = title + " " + summary

    categories = {
        "ekonomi": [
            "ekonomi",
            "enflasyon",
            "dolar",
            "euro",
            "faiz",
            "merkez bankası",
            "borsa",
            "piyasa",
            "üretim",
            "endeks",
            "inşaat",
            "sanayi",
            "büyüme",
            "ticaret",
            "ihracat",
            "ithalat"
        ],
        "teknoloji": [
            "teknoloji",
            "yapay zeka",
            "robot",
            "yazılım",
            "telefon",
            "uydu",
            "siber"
        ],
        "dünya": [
            "abd",
            "amerika",
            "avrupa",
            "rusya",
            "çin",
            "ukrayna",
            "israil",
            "iran"
        ],
        "gümrük": [
            "gümrük",
            "ithalat",
            "ihracat",
            "lojistik",
            "liman",
            "ticaret",
            "vergi",
            "navlun"
        ],
        "spor": [
            "spor",
            "futbol",
            "basketbol",
            "galatasaray",
            "fenerbahçe",
            "beşiktaş",
            "trabzonspor"
        ]
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in text:
                return category

    return "genel"


def add_categories(news_items):
    categorized_news = []

    for item in news_items:
        item["category"] = detect_category(item)
        categorized_news.append(item)

    return categorized_news