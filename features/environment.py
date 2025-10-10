def before_scenario(context, scenario):
    # Reset context before each scenario
    context.cart = None
    context.inventory = None
    context.user_manager = None
    context.login_system = None
    context.error_message = None
    context.login_result = None