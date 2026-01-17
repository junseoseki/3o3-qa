import pytest
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "base_url": os.getenv("MAIN_URL"),
        "viewport": {"width": 1920, "height": 1080},
        "locale": "ko-KR",
        "timezone_id": "Asia/Seoul"
    }

@pytest.fixture(autouse=True)
def auto_visit_base_url(page):
    page.goto("/")
    