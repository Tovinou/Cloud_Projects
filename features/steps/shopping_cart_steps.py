from behave import given, when, then
from models.shopping_cart import ShoppingCart
from models.book import Book
from models.inventory import Inventory

@given('the following books are available:')
def step_impl(context):
    context.inventory = Inventory()
    for row in context.table:
        author = row['Author'] if hasattr(context.table, 'headings') and 'Author' in context.table.headings else "Unknown Author"
        book = Book(row['Title'], author, int(row['Price']))
        context.inventory.add_book(book, 10)  # Add 10 copies of each book

@given('I have added "{book_title}" to the cart')
def step_impl(context, book_title):
    if not hasattr(context, 'cart') or context.cart is None:
        context.cart = ShoppingCart()
    book = context.inventory.find_book(book_title)
    context.cart.add_book(book)

@given('I have added the following books to the cart:')
def step_impl(context):
    context.cart = ShoppingCart()
    for row in context.table:
        book = context.inventory.find_book(row['Book'])
        context.cart.add_book(book)

@when('I add "{book_title}" to the cart again')
def step_impl(context, book_title):
    if not hasattr(context, 'cart'):
        context.cart = ShoppingCart()
    book = context.inventory.find_book(book_title)
    context.cart.add_book(book)

@when('I remove "{book_title}" from the cart')
def step_impl(context, book_title):
    book = context.inventory.find_book(book_title)
    context.cart.remove_book(book)

@when('I clear the cart')
def step_impl(context):
    context.cart.clear()

@then('the cart should contain {count:d} book')
@then('the cart should contain {count:d} books')
def step_impl(context, count):
    assert context.cart.get_total_quantity() == count, \
        f"Expected {count} books, but got {context.cart.get_total_quantity()}"

@then('the total price should be {total:d} SEK')
def step_impl(context, total):
    assert context.cart.get_total_price() == total, \
        f"Expected total {total}, but got {context.cart.get_total_price()}"

@then('the cart should be empty')
def step_impl(context):
    assert context.cart.is_empty(), "Cart is not empty"

@then('the cart should contain {quantity:d} of "{book_title}"')
def step_impl(context, quantity, book_title):
    book = context.inventory.find_book(book_title)
    actual_quantity = context.cart.get_quantity(book)
    assert actual_quantity == quantity, \
        f"Expected {quantity} of {book_title}, but got {actual_quantity}"

@then('the cart should contain {quantity:d} "{book_title}"')
def step_impl(context, quantity, book_title):
    book = context.inventory.find_book(book_title)
    actual_quantity = context.cart.get_quantity(book)
    assert actual_quantity == quantity, \
        f"Expected {quantity} of {book_title}, but got {actual_quantity}"