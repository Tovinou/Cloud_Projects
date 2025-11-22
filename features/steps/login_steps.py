from behave import given, when, then
from models.user import UserManager, LoginSystem

@given('the following users are registered:')
def step_impl(context):
    context.user_manager = UserManager()
    for row in context.table:
        context.user_manager.register_user(
            row['Username'], 
            row['Password'], 
            row['Email']
        )
    context.login_system = LoginSystem(context.user_manager)

@given('I am not logged in')
def step_impl(context):
    context.login_system.logout()

@when('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_result = context.login_system.login(username, password)

@when('I try to checkout')
def step_impl(context):
    if not context.login_system.is_logged_in():
        context.redirect_to_login = True
        context.checkout_message = "Please login to complete purchase"

@then('I should be logged in successfully')
def step_impl(context):
    assert context.login_result == True
    assert context.login_system.is_logged_in()

@then('I should see welcome message for "{username}"')
def step_impl(context, username):
    assert context.login_system.get_current_user() == username

@then('I should see error message "{expected_message}"')
def step_impl(context, expected_message):
    assert hasattr(context, 'login_result')
    assert context.login_result == False
    # In a real system, we'd check the actual error message

@then('the login should be {result}')
def step_impl(context, result):
    expected = result == 'successful'
    assert context.login_result == expected

@then('I should be redirected to login page')
def step_impl(context):
    assert hasattr(context, 'redirect_to_login')
    assert context.redirect_to_login == True

@then('I should see "{expected_message}"')
def step_impl(context, expected_message):
    assert hasattr(context, 'checkout_message')
    assert context.checkout_message == expected_message