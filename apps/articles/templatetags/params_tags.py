from django import template
from django.utils.http import urlencode

register = template.Library()


@register.simple_tag(takes_context=True)
def url_encode(context, **kwargs):
    params = context["request"].GET.dict()
    params.update(kwargs)
    return urlencode(params)
