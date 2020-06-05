from django import template

register = template.Library()


@register.filter
def val2color(value):
    if float(value) > 1000:
        pass
    elif 2 > float(value) > 1:
        return 'pink'
    elif 5 > float(value) > 2:
        return 'tomato'
    elif float(value) > 5:
        return 'red'
    elif float(value) < 0:
        return 'green'
