def generate_news_html(news_items, stats):
    html = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Günün Haberleri</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 40px auto;
            line-height: 1.6;
        }

        .stats-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 30px;
        }

        .stat-card {
            border: 1px solid #ddd;
            padding: 12px 20px;
            border-radius: 8px;
            min-width: 140px;
            background: #f7f7f7;
        }

        .stat-card strong {
            display: block;
            color: #444;
        }

        .stat-card span {
            font-size: 28px;
            font-weight: bold;
        }

        .featured-list {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 16px 24px;
            background: #fafafa;
            margin-bottom: 35px;
        }

        .featured-list li {
            margin-bottom: 8px;
        }

        .category-title {
            margin-top: 40px;
            border-bottom: 2px solid #222;
            padding-bottom: 6px;
        }

        .news-card {
            border: 1px solid #ddd;
            padding: 16px;
            margin-bottom: 16px;
            border-radius: 8px;
        }

        .news-card h3 {
            margin-top: 0;
        }

        .source {
            font-size: 13px;
            color: #777;
            margin-bottom: 8px;
        }

        a {
            color: #0066cc;
        }
    </style>
</head>
<body>

        <nav>
            <a href="index.html">Güncel Haberler</a> |
            <a href="archive.html">Arşiv</a> |
            <a href="search.html">Arama</a>
        </nav>
    <h1>Günün Haberleri</h1>
"""

    html += """
    <div class="stats-grid">
"""

    for key, value in stats.items():
        html += f"""
        <div class="stat-card">
            <strong>{key}</strong>
            <span>{value}</span>
        </div>
"""

    html += """
    </div>
"""

    top_news = sorted(
        news_items,
        key=lambda x: x.get("importance_score", 0),
        reverse=True
    )[:5]

    html += """
    <h2>🔥 Öne Çıkan Haberler</h2>
    <ul class="featured-list">
"""

    for item in top_news:
        html += f"""
        <li>
            <a href="{item.get("link", "")}" target="_blank">
                <strong>{item.get("title", "")}</strong>
            </a>
        </li>
"""

    html += """
    </ul>
"""

    grouped_news = {}

    for item in news_items:
        category = item.get("category", "genel")

        if category not in grouped_news:
            grouped_news[category] = []

        grouped_news[category].append(item)

    for category, items in grouped_news.items():
        html += f"""
    <h2 class="category-title">{category.upper()}</h2>
"""

        for item in items:
            html += f"""
    <div class="news-card">
        <h3>{item.get("title", "")}</h3>
        <p>{item.get("summary", "")}</p>
        <div class="source">Kaynak: {item.get("source", "")}</div>
        <a href="{item.get("link", "")}" target="_blank">Haberi Oku</a>
    </div>
"""

    html += """
</body>
</html>
"""

    return html