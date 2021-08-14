from django import template

register = template.Library()

@register.simple_tag
def get_verbose_name(obj):
    # print(obj)
    return obj._meta.verbose_name

@register.simple_tag
def get_verbose_name_plural(obj):
    # print(obj)
    return obj._meta.verbose_name_plural