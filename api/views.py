from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import escape

from api.models import Anime


def index(request):
    return render(request, 'api/index.html', context={})


"""
def ajouter_plateforme(request):
    if request.method == "POST":
        plateforme_name = escape(request.POST.get('plateforme_name'))
        plateforme_url = escape(request.POST.get('plateforme_url'))

        plateforme, created = Plateforme.objects.get_or_create(nom=plateforme_name, url=plateforme_url)

        if not created:
            return HttpResponse("La plateforme existe déjà", status=409)

        return HttpResponse(f'<div>{plateforme_name}</div>')

    return redirect('home')
"""