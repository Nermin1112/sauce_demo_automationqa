from playwright.sync_api import Page, expect

class FinishPage:
    def __init__(self, page: Page):
        self.page = page
        self.thank_you_message = page.locator(".complete-header")
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html", timeout=5000)
        expect(self.thank_you_message).to_be_visible(timeout=5000)

    def finish_text(self):
        return self.thank_you_message