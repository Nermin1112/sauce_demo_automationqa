import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage




@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"
        
@pytest.fixture
def inventory_page(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
    inventory = login.login("standard_user", "secret_sauce")
    return inventory


@pytest.fixture
def cart_with_product(inventory_page):
    inventory_page.add_order("Sauce Labs Backpack")
    return inventory_page.open_cart()

import os

SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def pytest_runtest_makereport(item, call):
    if "page" in item.fixturenames:
        setattr(item, "rep_" + call.when, call)

@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            page.screenshot(path=f"screenshots/{request.node.name}.png")

        browser.close()