from behave import given, when, then
from models.shopping_cart import ShoppingCart
from models.book import Book
from models.inventory import Inventory

@given('the following inventory:')
def step_impl(context):
    context.inventory = Inventory()
    for row in context.table:
        book = Book(row['Book Title'], "Author", int(row['Price']))
        context.inventory.add_book(book, int(row['Stock']))
    context.cart = ShoppingCart()

@when('I add "{book_title}" to the cart')
def step_impl(context, book_title):
    if not getattr(context, 'cart', None):
        context.cart = ShoppingCart()
    book = context.inventory.find_book(book_title)
    success, message = context.inventory.reserve_book(book, context.cart)
    if success:
        context.cart.add_book(book)
    else:
        context.error_message = message

@when('I try to add "{book_title}" to the cart')
def step_impl(context, book_title):
    if not getattr(context, 'cart', None):
        context.cart = ShoppingCart()
    book = context.inventory.find_book(book_title)
    success, message = context.inventory.reserve_book(book, context.cart)
    if not success:
        context.error_message = message

@when('I try to add "{book_title}" to the cart again')
def step_impl(context, book_title):
    # Alias to reuse the same logic for trying again
    if not getattr(context, 'cart', None):
        context.cart = ShoppingCart()
    book = context.inventory.find_book(book_title)
    success, message = context.inventory.reserve_book(book, context.cart)
    if not success:
        context.error_message = message

@then('the inventory for "{book_title}" should be {remaining:d}')
def step_impl(context, book_title, remaining):
    book = context.inventory.find_book(book_title)
    assert context.inventory.get_available_stock(book) == remaining

@then('I should see "{expected_message}" message')
def step_impl(context, expected_message):
    assert hasattr(context, 'error_message')
    assert expected_message in context.error_message