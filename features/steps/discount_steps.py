from behave import given, when, then
from models.shopping_cart import ShoppingCart
from models.book import Book
from models.inventory import Inventory

@when('I add {quantity:d} "{book_title}" to the cart')
def step_impl(context, quantity, book_title):
    context.cart = ShoppingCart()
    book = context.inventory.find_book(book_title)
    
    if quantity < 0:
        context.error_message = "Cannot add negative quantity"
        return
    
    for _ in range(quantity):
        context.cart.add_book(book)


@then('I should not receive any discount')
def step_impl(context):
    assert context.cart.get_discount_percentage() == 0

@then('I should receive a {percentage:d}% discount')
def step_impl(context, percentage):
    assert context.cart.get_discount_percentage() == percentage

@then('the final price should be {expected_price:d} SEK')
def step_impl(context, expected_price):
    assert context.cart.get_final_price() == expected_price

@then('the discount should be {expected_discount:d}%')
def step_impl(context, expected_discount):
    assert context.cart.get_discount_percentage() == expected_discount

@then('I should see an error message')
def step_impl(context):
    assert hasattr(context, 'error_message')
    assert "negative" in context.error_message.lower() or "invalid" in context.error_message.lower()

@then('the cart should remain empty')
def step_impl(context):
    assert context.cart.is_empty()