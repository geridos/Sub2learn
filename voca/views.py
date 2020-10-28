from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from voca.models import MidnightOil, Profile

from django.urls import reverse

from django.utils import timezone

def index(request):
    print('hello  view index')
    content_text = 'this is the web site of Bertrand'
    #pictures = []
    #time =
    #number of visitors
    context = {
        'content_text': content_text,
    }
    return render(request, 'voca/base_frontdoor.html', context)
