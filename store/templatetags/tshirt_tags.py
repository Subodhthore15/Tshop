from django import template
import math as m
register = template.Library()


@register.filter
def rupee(number):
    return f"₹ {number}"


@register.filter
def total_payable_amount(cart):
    amount = 0
    for c in cart:
        discount=c.get('tshirt').discount
        price=c.get('size').price
        sale_price=clc_sale_price(price,discount)
        amount_of_single_product = sale_price * c.get('quantity')

        amount = amount + amount_of_single_product

    return amount


@register.simple_tag
def min_price(tshirt):
    size = tshirt.sizevarient_set.all().order_by('price').first()

    return size.price


@register.simple_tag
def sale_price(tshirt):

    min_p = min_price(tshirt)  # it gives minimum price

    # size.min_price = size.price
    tshirt.after_discount = m.floor(min_p - (min_p*tshirt.discount/100))

    return tshirt.after_discount


@register.simple_tag
def get_active_size_button_class(active_size, size):
    # print(active_size , size)
    if active_size == size:
        return "dark"

    return "light"


@register.simple_tag
def multiply(a, b):
    return a*b


@register.simple_tag
def clc_sale_price(price, discount):
    p = m.floor(price - (price*discount/100))
    return p
