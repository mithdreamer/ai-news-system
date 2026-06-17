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
            max-width: 900px;
            margin: 40px auto;
            line-height: 1.6;
        }

        .news-card {
            border: 1px solid #ddd;
            padding: 16px;
            margin-bottom: 16px;
            border-radius: 8px;
        }

        .category {
            font-size: 13px;
            font-weight: bold;
            color: #555;
        }

        .source {
            font-size: 13px;
            color: #777;
        }

        a {
            color: #0066cc;
        }
        .stats-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 30px;
        }

        .stat-card {
            border: 1px solid #ddd;
            padding: 12px 16px;
            border-radius: 8px;
            min-width: 120px;
            background: #f7f7f7;
        }

        .stat-card strong {
            display: block;
            font-size: 13px;
            color: #555;
        }

        .stat-card span {
            font-size: 24px;
            font-weight: bold;
        }
    </style>
</head>
<body>
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

    for item in news_items:
        html += f"""
    <div class="news-card">
        <div class="category">{item.get("category", "genel")}</div>
        <h2>{item.get("title", "")}</h2>
        <p>{item.get("summary", "")}</p>
        <div class="source">Kaynak: {item.get("source", "")}</div>
        <a href="{item.get("link", "")}" target="_blank">Haberi oku</a>
    </div>
"""

    html += """
</body>
</html>
"""

    return html