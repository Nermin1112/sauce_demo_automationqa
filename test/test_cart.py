from playwright.sync_api import Page,expect


def test_product_in_cart(cart_with_product):
    expect(cart_with_product.verify_product("Sauce Labs Backpack")).to_be_visible()

def test_remove_product(cart_with_product):
    cart_with_product.remove_product("Sauce Labs Backpack")
    
    expect(cart_with_product.verify_product("Sauce Labs Backpack")).to_have_count(0)

def test_checkout_navigation(cart_with_product):
    checkout_page = cart_with_product.checkout()

    expect(checkout_page.title).to_have_text("Checkout: Your Information")

def test_cart_empty(inventory_page):
    cart_page = inventory_page.open_cart()
    expect(cart_page.cart_items).to_have_count(0)



