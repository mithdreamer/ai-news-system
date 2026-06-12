import feedparser
from datetime import datetime

from utils.config_loader import load_rss_sources
from utils.logger import get_logger

logger = get_logger()


def fetch_news(limit_per_source=10):

    all_news = []

    rss_sources = load_rss_sources()
    
    print("Yüklenen kaynaklar:")
    print(rss_sources)

    for source in rss_sources:

        logger.info(
            f"RSS çekiliyor: {source['name']}"
        )

        feed = feedparser.parse(
            source["url"]
        )

        

        logger.info(
            f"RSS tamamlandı: {source['name']}"
        )

        print(source["name"], len(feed.entries))

        logger.info(f"RSS tamamlandı: {source['name']}")

        for entry in feed.entries[:limit_per_source]:

            all_news.append(
                {
                    "source": source["name"],
                    "title": entry.get(
                        "title",
                        ""
                    ),
                    "summary": entry.get(
                        "summary",
                        ""
                    ),
                    "link": entry.get(
                        "link",
                        ""
                    ),
                    "published": entry.get(
                        "published",
                        ""
                    ),
                    "fetched_at": datetime.now().isoformat()
                }
            )
    return all_news
    
    