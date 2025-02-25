import time
import asyncio
from playwright.async_api import async_playwright

with async_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page =browser.new_page()

    page.goto('https://www.baidu.com')

    time.sleep(2)

    browser.close()
















