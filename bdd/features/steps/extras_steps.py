# features/steps/extras_steps.py
from behave import given, when, then
from decimal import Decimal
from features.store import Store, Cart, Book, User

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    # simple auth simulation
    context.user = User(username=username, email=f"{username}@example.com", password=password)
    # store may hold users if needed; we accept any credentials here for simplicity
    context.logged_in = True

@when('I checkout')
def step_impl(context):
    # Simulate checkout: apply discounts, check stock and "send" receipt
    # Ensure logged in if required by store (we didn't enforce login for all flows)
    context.last_receipt = context.cart.checkout(user=getattr(context, 'user', None))

@then('the final total should be {expected_total}')
def step_impl(context, expected_total):
    expected = Decimal(expected_total)
    total = context.last_receipt['total'] if isinstance(context.last_receipt, dict) else Decimal('0.00')
    assert total == expected, f"Expected {expected} but got {total}"


@then('I should see a stock limit message for "{title}"')
def step_impl(context, title):
    assert any(title in msg for msg in context.cart.messages), f"No stock message for {title}; messages: {context.cart.messages}"

@then('a receipt should be created and sent to "{email}"')
def step_impl(context, email):
    sent = context.cart.store.sent_emails
    assert sent, "No email was sent"
    last = sent[-1]
    assert last['to'] == email, f"Receipt was sent to {last['to']}, expected {email}"

@then('the last sent email should contain "{text}"')
def step_impl(context, text):
    sent = context.cart.store.sent_emails
    assert sent, "No email sent"
    last = sent[-1]
    assert text in last['body'], f"'{text}' not found in email body: {last['body']}"
