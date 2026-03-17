

# Playwright UI Automation

Automated UI testing project for the SauceDemo web application using Playwright and Pytest.

## Project Overview

This project demonstrates end-to-end UI test automation using the Page Object Model (POM) design pattern.

It covers core user flows such as login, product management, cart validation, and checkout process.

The project is structured using reusable page classes, pytest fixtures, and clean test separation by functionality.

## Tech Stack

* Python
* Pytest
* Playwright
* Pytest-xdist (parallel execution)
* Pytest-html (test reports)

## Application Under Test

SauceDemo
https://www.saucedemo.com/

## Project Structure

```
project-root/

pages/
- login_page.py
- inventory_page.py
- cart_page.py
- checkout_page.py
- finish_page.py

test/
- test_login.py
- test_inventory.py
- test_cart.py
- test_checkout.py

conftest.py
requirements.txt
pytest.ini
.gitignore
README.md
```

## Test Coverage

### Login

* Successful login
* Invalid username
* Invalid password

### Inventory

* Add product to cart
* Remove product from cart

### Cart

* Verify product in cart
* Remove product from cart
* Checkout navigation
* Empty cart validation

### Checkout

* Complete checkout flow

## Features

* Page Object Model (POM)
* Reusable pytest fixtures
* Clean test structure (by page)
* Parallel test execution
* HTML test reports
* Automatic screenshots on failure
* CI/CD with GitHub Actions

## Running the Tests

Install dependencies:

```
pip install -r requirements.txt
```

Install Playwright browsers:

```
playwright install
```

Run tests:

```
pytest -n 2 --html=report.html
```

## Reports

After execution, HTML report is generated:

```
report.html
```

Screenshots (on failure):

```
screenshots/
```

## CI/CD

Tests are automatically executed via GitHub Actions on every push to the main branch.

---

This project is part of a QA automation portfolio demonstrating modern UI test automation practices using Playwright.

