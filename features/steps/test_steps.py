from behave import when, then
import requests

BASE_URL = "http://localhost:8080"

@when('jag anropar "{path}"')
def step_call_endpoint(context, path):
    context.response = requests.get(f"{BASE_URL}{path}")

@then('ska jag se "{text}"')
def step_verify_response(context, text):
    assert text in context.response.text
