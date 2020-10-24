from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(fooditem, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == fooditem.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(fooditem , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == fooditem.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(fooditem,cart):
    return fooditem.price * cart_quantity(fooditem,cart)

@register.filter(name='total_cart_price')
def total_cart_price(fooditems , cart):
    sum = 0 
    for p in fooditems:
        sum += price_total(p , cart)

    return sum

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)