from behave import given, when, then
from decimal import Decimal
from features.store import Store, Cart, Book, User

@given('an empty store with the following books:')
def step_impl(context):
    context.store = Store()
    for row in context.table:
        title = row['title']
        price_str = row['price']
        # If "stock" column exists (del2), use it; otherwise treat as large stock
        stock = int(row['stock']) if hasattr(context.table, 'headings') and 'stock' in context.table.headings else 10**9
        context.store.add_book(Book(title=title, price=Decimal(price_str), stock=stock))

@given('I have an empty cart')
def step_impl(context):
    context.cart = Cart(context.store)

@when('I add "{title}" to the cart')
def step_impl(context, title):
    context.cart.add_book_by_title(title)

@given('I add "{title}" to the cart')
def step_impl(context, title):
    context.cart.add_book_by_title(title)

@when('I add "{title}" to the cart {n:d} times')
def step_impl(context, title, n):
    for _ in range(n):
        context.cart.add_book_by_title(title)

@when('I remove "{title}" from the cart')
def step_impl(context, title):
    context.cart.remove_book_by_title(title)

@then('the cart should have {n:d} items')
def step_impl(context, n):
    assert context.cart.total_items() == n, f"expected {n} items, got {context.cart.total_items()}"

@then('the cart total should be {amount}')
def step_impl(context, amount):
    expected = Decimal(amount)
    assert context.cart.total() == expected, f"expected total {expected}, got {context.cart.total()}"

@then('the cart should have {qty:d} of "{title}"')
def step_impl(context, qty, title):
    assert context.cart.quantity_of(title) == qty, f"expected {qty} of {title}, got {context.cart.quantity_of(title)}"

@when('I empty the cart')
def step_impl(context):
    context.cart.empty()
