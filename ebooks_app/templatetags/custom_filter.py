from django import template

register = template.Library()

@register.filter
def uppercase(value):
    print(value)
    return value.upper()

@register.filter
def lowercase(value):
    return value.lower()
