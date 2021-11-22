from django import template

register = template.Library()

@register.simple_tag
def get_right(right=None):
    return right
