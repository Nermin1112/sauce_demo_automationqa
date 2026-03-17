from playwright.sync_api import Page
from pages.inventory_page import InventoryPage


class LoginPage:

    def __init__(self, page: Page):
        self.page = page    
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator('[data-test="error"]')

    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        return InventoryPage(self.page)


