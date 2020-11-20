from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from voca.models import MidnightOil, Profile

from django.urls import reverse

from django.utils import timezone

#content_text = """Une ferme et constante résolution d\'exécuter tout ce que la raison lui conseillera,
#sans que ses passions ou ses appétits l'en détournent; et c'est la fermeté de cette résolution
#que je crois devoir être prise pour la vertue
#René Descartes"""

def index(request):
    content_text = """\"Une ferme et constante résolution d\'exécuter tout ce que la raison lui conseillera,
    et c'est la fermeté de cette résolution que je crois devoir être prise pour la vertue.\"
    René Descartes"""
    #pictures = []
    #time =
    #number of visitors
    context = {
        'content_text': content_text,
    }
    return render(request, 'voca/base_frontdoor.html', context)
