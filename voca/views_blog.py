import os
from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect

import collections

def sidebar_context():
    sidebar = collections.OrderedDict()
    sidebar['all'] = 'All'
    sidebar['computer'] = 'Computer'
    sidebar['history'] = 'History'
    sidebar['life'] = 'Life'
    sidebar['other'] = 'Other'
    return sidebar

def index(request, blog_page):
    print(blog_page)
    #content = load_content_context(blog_page)
    prefix_path = r"voca/templates/voca/articles"
    list_file = []
    for article in os.listdir(prefix_path):
        path_file = "voca/articles/" + article
        #with open(path_file, 'r') as f:
        list_file.append(path_file)

    context = {
        'sidebar' : sidebar_context(),
        'files' : list_file,
    }
    return render(request, 'voca/base_blog.html', context)

def load_content_context(page_name):
        if page_name == 'computer':
            return 'No articles yet on computer'
        elif page_name == 'history':
            return 'No articles yet on history'
        elif page_name == 'life':
            return 'No articles yet on life'
        elif page_name == 'other':
            return 'No articles yet on other'
        else:
            raise Http404("Nothing to article about that")
