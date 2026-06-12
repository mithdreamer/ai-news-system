import json
from pathlib import Path


def load_rss_sources():

    config_file = (
        Path(__file__).resolve().parent.parent.parent
        / "config"
        / "rss_sources.json"
    )

    with open(
        config_file,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)