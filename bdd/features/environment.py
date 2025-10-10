# features/environment.py
def before_scenario(context, scenario):
    # ensure fresh store/cart for each scenario; actual creation happens in steps
    context.store = None
    context.cart = None
    context.user = None
