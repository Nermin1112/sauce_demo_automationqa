from playwright.sync_api import Page,expect
from pages.finish_page import FinishPage

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.first_name_input = page.get_by_role("textbox", name="First Name")
        self.last_name_input = page.get_by_role("textbox", name="Last Name")
        self.postal_code_input = page.get_by_role("textbox", name="Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")

        self.finish_button = page.get_by_role("button", name="Finish")

    def complete_checkout(self, first_name="John", last_name="Doe", postal_code="71000"):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        
        self.continue_button.click()

        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

        self.finish_button.click()

        return FinishPage(self.page)