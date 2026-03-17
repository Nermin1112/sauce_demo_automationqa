import os
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        if request.node.rep_call.failed:
            page.screenshot(path=f"{SCREENSHOT_DIR}/{request.node.name}.png")
        browser.close()

@pytest.fixture
def inventory_page(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
    return login.login("standard_user", "secret_sauce")

@pytest.fixture
def cart_with_product(inventory_page):
    inventory_page.add_order("Sauce Labs Backpack")
    return inventory_page.open_cart()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)