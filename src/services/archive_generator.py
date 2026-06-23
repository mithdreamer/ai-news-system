from pathlib import Path
import json


def generate_archive(project_root):

    raw_folder = (
        project_root
        / "data"
        / "raw"
    )

    archive_files = []

    for file in raw_folder.glob("*-news.json"):

        if file.name == "latest-news.json":
            continue

        archive_files.append(file)

    archive_files.sort(reverse=True)

    html = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Haber Arşivi</title>
</head>
<body>

<nav>
    <a href="index.html">Güncel Haberler</a> |
    <a href="archive.html">Arşiv</a> |
    <a href="search.html">Arama</a>
</nav>

<h1>Haber Arşivi</h1>

<ul>
"""

    for file in archive_files:

        date_name = (
            file.stem
            .replace("-news", "")
        )

        html += f"""
<li>
    <a href="{date_name}-news.html">
        {date_name}
    </a>
</li>
"""

    html += """
</ul>

</body>
</html>
"""

    return html

def generate_search_index(project_root):

    raw_folder = project_root / "data" / "raw"

    all_news = []
    seen_links = set()

    for file in raw_folder.glob("*-news.json"):

        try:
            with open(file, "r", encoding="utf-8") as f:
                news = json.load(f)

                if isinstance(news, list):

                    for item in news:

                        link = item.get("link", "").strip()

                        if not link:
                            continue

                        if link in seen_links:
                            continue

                        seen_links.add(link)

                        all_news.append(item)

        except Exception as e:
            print(f"Hata: {file.name} -> {e}")

    return all_news