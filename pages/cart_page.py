from playwright.sync_api import Page
from pages.checkout_page import CheckoutPage

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.get_by_role("button", name="Checkout")


    def verify_product(self, product_name):
        return self.cart_items.filter(has_text=product_name)

    def remove_product(self, product_name):
        item = self.cart_items.filter(has_text=product_name)
        item.get_by_role("button", name="Remove").click()

    def checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.page)