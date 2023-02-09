from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .services import *


def index(request):
    pole = pole_game.show2()

    context = {
        'pole': pole
    }

    return render(request, 'sapy/index.html', context)
