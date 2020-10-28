from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

import collections

def sidebar_context():
    sidebar = collections.OrderedDict()
    sidebar['mystory'] = 'My story'
    sidebar['resume'] = 'Resume'
    sidebar['mypictures'] = 'My pictures'
    sidebar['books'] = 'Books I like'
    return sidebar

def index(request, aboutme_page):
    print(aboutme_page)
    content = load_content_context(aboutme_page)
    context = {
        'sidebar' : sidebar_context(),
        'content' : content,
    }
    return render(request, 'voca/aboutme/aboutme_mystory.html', context)

def load_content_context(page_name):
        if page_name == 'mystory':
            return 'this is my life'
        elif page_name == 'books':
            return 'this are my books'
        elif page_name == 'resume':
            return 'this is my resume'
        elif page_name == 'mypictures':
            return 'this are my pictures'
        else:
            raise Http404("Nothing to talk about that")

