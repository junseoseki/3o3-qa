import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import os

load_dotenv()

@pytest.fixture(scope="session")
def browser():
    if os.getenv("CI") == "true":
        with sync_playwright() as p:
            yield p.chromium.launch(headless=True)
    else:
        with sync_playwright() as p:
            yield p.chromium.launch(headless=False)
    