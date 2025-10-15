from behave import *
import requests

@when('jag anropar "{path}"')
def step_call_endpoint(context, path):
    context.response = requests.get(f"http://localhost:8080{path}")

    @then('ska jag se "{text}"')
    def step_verify_response(context, text):
        assert text in context.response.text
