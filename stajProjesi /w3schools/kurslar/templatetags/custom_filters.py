# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='custom_split')
def custom_split(value, arg):
    return value.split(arg)
    