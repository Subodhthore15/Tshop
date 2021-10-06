from django import template
import math as m
register = template.Library()








@register.simple_tag
def get_order_status_class(status):
    if status=="COMPLETED":
        return 'success'
    elif status=="PENDING":
        return 'warning'
    else:
        return 'info'



