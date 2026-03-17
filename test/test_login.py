from playwright.sync_api import expect,Page
from pages.login_page import LoginPage


def test_login_success(page: Page, base_url: str):
    login = LoginPage(page)
    login.open(base_url)
    inventory_page = login.login("standard_user", "secret_sauce")

    expect(inventory_page.inventory_list).to_be_visible()


def test_login_invalid_username(page: Page, base_url: str):
    login = LoginPage(page)
    login.open(base_url)
    login.login("invalid_user", "secret_sauce")
    
    expect(login.error_message).to_be_visible()
    expect(login.error_message).to_contain_text("Epic sadface")


def test_login_invalid_password(page: Page, base_url: str):
    login = LoginPage(page)
    login.open(base_url)
    login.login("standard_user", "invalid_password")

    expect(login.error_message).to_be_visible()
    expect(login.error_message).to_contain_text("Epic sadface")
    
