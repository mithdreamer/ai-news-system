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
        .search-box {
    margin: 25px 0;
    }

        .search-box input {
            width: 100%;
            padding: 12px 14px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 8px;
        }

            .category-filters {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin: 20px 0 30px;
            }

            .category-filter-btn {
                padding: 8px 14px;
                border: 1px solid #ddd;
                border-radius: 999px;
                background: #f7f7f7;
                cursor: pointer;
            }

            .category-filter-btn.active {
                background: #222;
                color: white;
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
    <div class="search-box">
    <input
        type="text"
        id="home-search-input"
        placeholder="Güncel haberlerde ara..."
    >
</div>

<div class="category-filters">
    <button class="category-filter-btn active" data-category="all">Tümü</button>
    <button class="category-filter-btn" data-category="ekonomi">Ekonomi</button>
    <button class="category-filter-btn" data-category="teknoloji">Teknoloji</button>
    <button class="category-filter-btn" data-category="dünya">Dünya</button>
    <button class="category-filter-btn" data-category="gümrük">Gümrük</button>
    <button class="category-filter-btn" data-category="genel">Genel</button>
</div>

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
            search_text = f"""
            {item.get("title", "")}
            {item.get("summary", "")}
            {item.get("category", "")}
            {item.get("source", "")}
            """.lower()

            html += f"""
                <div
                    class="news-card"
                    data-search="{search_text}"
                    data-category="{item.get("category", "genel")}"
                >
                    <h3>{item.get("title", "")}</h3>
                    <p>{item.get("summary", "")}</p>
                    <div class="source">Kaynak: {item.get("source", "")}</div>
                    <a href="{item.get("link", "")}" target="_blank">Haberi Oku</a>
                </div>
            """           
    html += """
        <script>
            const homeSearchInput = document.querySelector("#home-search-input");
            const newsCards = document.querySelectorAll(".news-card");
            const categoryButtons = document.querySelectorAll(".category-filter-btn");

            let selectedCategory = "all";

            function filterNews() {
                const query = homeSearchInput.value.toLowerCase();

                newsCards.forEach(function (card) {
                    const text = card.dataset.search || "";
                    const category = card.dataset.category || "genel";

                    const matchesSearch = text.includes(query);
                    const matchesCategory =
                        selectedCategory === "all" || category === selectedCategory;

                    if (matchesSearch && matchesCategory) {
                        card.style.display = "block";
                    } else {
                        card.style.display = "none";
                    }
                });
            }

            homeSearchInput.addEventListener("input", filterNews);

            categoryButtons.forEach(function (button) {
                button.addEventListener("click", function () {
                    categoryButtons.forEach(function (btn) {
                        btn.classList.remove("active");
                    });

                    button.classList.add("active");
                    selectedCategory = button.dataset.category;

                    filterNews();
                });
            });
        </script>

    </body>
    </html>
    """

    return html