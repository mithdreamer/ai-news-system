import logging
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

LOG_DIR = PROJECT_ROOT / "logs"

LOG_DIR.mkdir(
    exist_ok=True
)

LOG_FILE = LOG_DIR / "app.log"


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def get_logger():
    return logging.getLogger("ai-news-system")

print("LOGGER DOSYASI YÜKLENDİ")
print(dir())