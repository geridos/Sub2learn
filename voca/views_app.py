from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from voca.models import MidnightOil, Profile

from django.utils import timezone

from .parser import parse

import collections

def sidebar_context(profile_name):
    sidebar = collections.OrderedDict()
    sidebar['/voca/app/profiles'] = 'Change profiles'
    sidebar['/voca/app/' + profile_name + '/stat'] = 'Statictics'
    sidebar['/voca/app/' + profile_name + '/new_input'] = 'New inputs'
    sidebar['/voca/app/' + profile_name + '/words/burntoil'] = 'Leant words'
    sidebar['/voca/app/' + profile_name + '/words/midnightoil'] = 'Midnight oil'
    return sidebar

def sidebar_index_context():
    sidebar = collections.OrderedDict()
    sidebar['new_profile'] = 'Add new profile'
    return sidebar

def sidebar_new_profile_context():
    sidebar = collections.OrderedDict()
    sidebar['profiles'] = 'Profiles'
    return sidebar

def index(request):
    print('index view')
    list_profile = get_list_or_404(Profile)
    context = {
        'list_profile': list_profile,
        'sidebar' : sidebar_index_context()
    }
    print(list_profile)
    return render(request, 'voca/app/index.html', context)


def add_new_profile(request):
    if request.method == 'POST':
        new_text = request.POST.get('textfield', None)

        profile = Profile(name=new_text).save()

        #index(request)
        list_profile = get_list_or_404(Profile)
        context = { 'list_profile': list_profile,
            'sidebar' : sidebar_index_context()
        }
        return render(request, 'voca/app/index.html', context)
    else:
        context = {
            'sidebar' : sidebar_new_profile_context()
        }
        return render(request, 'voca/app/new_profile.html', context)

def burntOil(request, profile_name):
    profile = get_object_or_404(Profile, name=profile_name)
    list_words = profile.midnightoil_set.filter(burnt=True)
    context = {
        'profile': profile,
        'mode': "burntOil",
        'list_words': list_words,
        'sidebar' : sidebar_context(profile.name)
    }
    return render(request, 'voca/app/learnt_words.html', context)


#TODO check if the words are in the EN dictionary
#TODO try to catch phrasal verbes
#TODO use the removed_token list as a filter for other input
def midnightOil(request, profile_name):
    profile = get_object_or_404(Profile, name=profile_name)
    if request.method == 'POST':
        post_results = request.POST.items()

        selected_words = []
        for key, value in post_results:
            if key == 'csrfmiddlewaretoken' or value.isdigit == False:
                print("this key = %s, value %s is ignored" % (key, value))
                continue
            print("key = %s, value %s" % (key, value))
            selected_words.append(key)
            word_learnt = profile.midnightoil_set.get(pk=value)
            word_learnt.burnt = True
            word_learnt.save()

        print(selected_words)
        list_words = profile.midnightoil_set.filter(burnt=False)
        context = {
            'profile': profile,
            'mode': "MidnightOil",
            'list_words': list_words,
            'selected_words': selected_words,
            'sidebar' : sidebar_context(profile.name)
        }
        return render(request, 'voca/app/tolearn_words.html', context)
    else:
        list_words = profile.midnightoil_set.filter(burnt=False)
        context = {
            'profile': profile,
            'mode': "MidnightOil",
            'list_words': list_words,
            'sidebar' : sidebar_context(profile.name)
        }
        return render(request, 'voca/app/tolearn_words.html', context)


def profile_stat(request, profile_name):
    profile = get_object_or_404(Profile, name=profile_name)
    number_learnt = len(profile.midnightoil_set.filter(burnt=True))
    number_tolearnt = len(profile.midnightoil_set.filter(burnt=False))
    context = {
        'stat_learnt' : number_learnt,
        'stat_tolearn' : number_tolearnt,
        'profile': profile,
        'sidebar' : sidebar_context(profile.name)
    }
    return render(request, 'voca/app/profile_stat.html', context)

def new_input(request, profile_name):
    profile = get_object_or_404(Profile, name=profile_name)
    if request.method == 'POST':
        new_text = request.POST.get('textfield', None)

        tokens = parse(new_text)
        filtered_words = tokens[0]
        removed_tokens = tokens[1]

        print('removed_tokens')
        print(removed_tokens)

        not_in_database_words = [w for w in filtered_words
            if len(MidnightOil.objects.filter(word=w, profile=profile.id)) == 0]

        in_database_words = [w for w in filtered_words
            if len(MidnightOil.objects.filter(word=w, profile=profile.id)) > 0]

        print('words not in database')
        print(not_in_database_words)

        [ profile.midnightoil_set.create(word=w) for w in not_in_database_words ]

        context = {
            'profile': profile,
            'not_words': not_in_database_words,
            'in_words': in_database_words,
            'removed_tokens': removed_tokens,
            'sidebar' : sidebar_context(profile.name),
        }
        return render(request, 'voca/app/input.html', context)
    else:
        context = {
            'sidebar' : sidebar_context(profile.name),
        }
        print('Hello no request post')
        return render(request, 'voca/app/input.html', context)