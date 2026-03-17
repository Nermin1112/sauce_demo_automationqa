from playwright.sync_api import Page
from pages.cart_page import CartPage

inventory_list = ".inventory_list"

class InventoryPage :
    def __init__(self,page : Page ):
        self.page = page
        self.inventory_list = page.locator(inventory_list)
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")


    def add_order(self, product_name):
        product = self.page.locator(".inventory_item").filter(has_text = product_name)
        product.get_by_role("button", name="Add to cart").click()
        
    def remove_order(self, product_name):
        product = self.page.locator(".inventory_item").filter(has_text = product_name)
        product.get_by_role("button", name="Remove").click()

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()
        return CartPage(self.page)