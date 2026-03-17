from playwright.sync_api import expect

def test_complete_checkout(cart_with_product):
    product_name = "Sauce Labs Backpack"

    expect(cart_with_product.verify_product(product_name)).to_be_visible()

    finish_page = cart_with_product.checkout().complete_checkout()

    expect(finish_page.finish_text()).to_have_text("Thank you for your order!")