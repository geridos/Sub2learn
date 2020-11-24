from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value): # Only one argument.
    #for match in finditer("is", "Life is good because it is an isy day."):
    #    print(match.span(), match.group())
    return filter(None,re.split('\.|,|;|=| |\n|\s|\(|\)', value))
