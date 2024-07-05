import time
from datetime import datetime

import requests

RATE_LIMIT_URL = "https://api.github.com/rate_limit"


def get_rate() -> dict:
    try:
        rate = requests.get(RATE_LIMIT_URL).json().get("rate")
        return rate
    except requests.RequestException as e:
        print(f"Error fetching rate limit: {e}")


def check_rate_limit_count() -> bool:
    rate = get_rate()
    return False if rate["remaining"] <= 1 else True


def check_rate_limit() -> None:
    while not check_rate_limit_count():
        reset_time = datetime.fromtimestamp(get_rate()["reset"])
        wait_range = (reset_time - datetime.now()).seconds
        print(f"Need to wait {wait_range} seconds for next rate limit check.")
        time.sleep(wait_range)
