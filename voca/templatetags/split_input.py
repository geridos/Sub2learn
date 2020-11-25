from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value): # Only one argument.
    #for match in finditer("is", "Life is good because it is an isy day."):
    #    print(match.span(), match.group())
    tokens = filter(None,re.split('\.|, |;|=| |\n|\s|\(|\)', value.lower()))
    print("register filter : ")
    print(tokens)
    index = 0
    array_of_pair = []
    pair = ()

    for t in tokens:
        found = False
        for w, i in array_of_pair:
            if t == w:
                array_of_pair.append([w, i])
                found = True
                break
        if found == False:
            array_of_pair.append([t, index])
            index += 1

    return array_of_pair
