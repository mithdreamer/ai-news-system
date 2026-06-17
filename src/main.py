from pathlib import Path
from datetime import datetime

from services.news_fetcher import fetch_news
from services.news_filter import filter_news
from services.script_generator import generate_news_script

from utils.file_helper import save_json, save_text
from utils.logger import get_logger
from services.news_categorizer import add_categories
from services.statistics import generate_statistics
from services.news_cleaner import clean_news
from services.html_generator import generate_news_html


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main():
    logger = get_logger()

    today = datetime.now().strftime("%Y-%m-%d")

    logger.info("Uygulama başlatıldı")

    print("AI Haber Yayın Sistemi başlatıldı...")

    news_items = fetch_news()
    cleaned_news = clean_news(news_items)
    filtered_news = filter_news(cleaned_news)
    categorized_news = add_categories(filtered_news)

    latest_json_file = PROJECT_ROOT / "data" / "raw" / "latest-news.json"
    archive_json_file = PROJECT_ROOT / "data" / "raw" / f"{today}-news.json"

    latest_script_file = PROJECT_ROOT / "outputs" / "scripts" / "daily-news-script.txt"
    archive_script_file = PROJECT_ROOT / "outputs" / "scripts" / f"{today}-script.txt"

    save_json(categorized_news, latest_json_file)
    save_json(categorized_news, archive_json_file)

    script = generate_news_script(categorized_news)

    

    save_text(script, latest_script_file)
    save_text(script, archive_script_file)
    latest_html_file = PROJECT_ROOT / "outputs" / "html" / "daily-news.html"
    archive_html_file = PROJECT_ROOT / "outputs" / "html" / f"{today}-news.html"
    html = generate_news_html(categorized_news)

    save_text(html, latest_html_file)
    save_text(html, archive_html_file)

    stats = generate_statistics(
        categorized_news
    )

    print("\n--- HABER İSTATİSTİKLERİ ---")

    for key, value in stats.items():
        print(
            f"{key}: {value}"
        )

    logger.info(f"{len(news_items)} adet ham haber çekildi")
    logger.info(f"{len(filtered_news)} adet filtrelenmiş haber kaydedildi")
    logger.info(f"Arşiv JSON oluşturuldu: {archive_json_file}")
    logger.info(f"Arşiv TXT oluşturuldu: {archive_script_file}")
    logger.info("Yayın metni oluşturuldu")
    

    print("Haberler çekildi.")
    print(f"Ham haber sayısı: {len(news_items)}")
    print(f"Filtrelenmiş haber sayısı: {len(filtered_news)}")
    print(f"Güncel JSON: {latest_json_file}")
    print(f"Arşiv JSON : {archive_json_file}")
    print(f"Güncel TXT : {latest_script_file}")
    print(f"Arşiv TXT  : {archive_script_file}")
    print(f"Güncel HTML: {latest_html_file}")
    print(f"Arşiv HTML : {archive_html_file}")


if __name__ == "__main__":
    main()