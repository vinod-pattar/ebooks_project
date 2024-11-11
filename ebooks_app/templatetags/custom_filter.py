from django import template

register = template.Library()

@register.filter
def uppercase(value):
    print(value)
    return value.upper()

@register.filter
def lowercase(value):
    return value.lower()

@register.filter
def multiply(value, arg):
    return round(float(value) * float(arg), 2)


@register.filter
def is_author_detail(value):
    print(value)
    return bool(re.search(r'/[a-z]{2}/author/\d+', value))
