from playwright.sync_api import Page,expect
from pages.inventory_page import InventoryPage

def test_add_product_to_cart(inventory_page):
    inventory_page.add_order("Sauce Labs Backpack")
    expect(inventory_page.shopping_cart_badge).to_have_text("1")

def test_remove_product_from_cart(inventory_page):
    inventory_page.add_order("Sauce Labs Backpack")
    inventory_page.remove_order("Sauce Labs Backpack")
    expect(inventory_page.shopping_cart_badge).to_have_count(0)