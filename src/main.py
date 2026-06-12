from pathlib import Path
from datetime import datetime

from services.news_fetcher import fetch_news
from services.news_filter import filter_news
from services.script_generator import generate_news_script

from utils.file_helper import save_json, save_text
from utils.logger import get_logger


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main():
    logger = get_logger()

    today = datetime.now().strftime("%Y-%m-%d")

    logger.info("Uygulama başlatıldı")

    print("AI Haber Yayın Sistemi başlatıldı...")

    news_items = fetch_news()
    filtered_news = filter_news(news_items)

    latest_json_file = PROJECT_ROOT / "data" / "raw" / "latest-news.json"
    archive_json_file = PROJECT_ROOT / "data" / "raw" / f"{today}-news.json"

    latest_script_file = PROJECT_ROOT / "outputs" / "scripts" / "daily-news-script.txt"
    archive_script_file = PROJECT_ROOT / "outputs" / "scripts" / f"{today}-script.txt"

    save_json(filtered_news, latest_json_file)
    save_json(filtered_news, archive_json_file)

    script = generate_news_script(filtered_news)

    save_text(script, latest_script_file)
    save_text(script, archive_script_file)

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


if __name__ == "__main__":
    main()