# Behave BDD - Bookstore assignment

## Overview
This repository contains Gherkin scenarios and Behave step-implementations for a simple bookstore shopping cart.
It covers:
- Del 1: Basic cart functionality (add, remove, total, quantity increment, empty cart)
- Del 2: Three extra features implemented: Discount (10% if >3 books), Stock management, and Receipt/email simulation.

## Files
- `features/del1_cart.feature` - Gherkin scenarios for core behavior
- `features/del2_extras.feature` - Gherkin scenarios for extras (discount, stock, receipt)
- `features/steps/cart_steps.py` - Steps for core cart scenarios
- `features/steps/extras_steps.py` - Steps for extra scenarios
- `features/store.py` - Simple Python classes: Book, Store, Cart, User
- `features/environment.py` - Behave environment setup

## How I solved the assignment
- I simulated the store and cart using Python classes (no web framework or DB).
- Discount: If total number of books > 3, apply 10% discount on whole cart.
- Stock: Each book has a `stock` attribute; adding more than stock will add only up to stock and create a message.
- Receipt: Checkout creates a receipt dict and simulates sending an email by appending to `Store.sent_emails`.

I chose these three extras because they are common e-commerce features and illustrate different testing needs:
- Discounts require numeric edge-case testing
- Stock requires stateful constraints and user feedback messages
- Receipt tests integration between checkout and "email sending" logic

## What was easy / hard
- Easy: Writing Gherkin for simple flows, mapping steps to functions.
- Harder: Deciding expected behavior for unrealistic quantities (negative values) — I chose to treat negative add attempts as ignored and create messages (so negative tests assert a 0 total).

## How to run
1. Create a Python virtual environment and install behave:
```bash
python -m venv .venv
.venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install behave
