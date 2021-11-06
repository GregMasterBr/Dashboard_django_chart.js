from django.http import HttpResponse
from django.shortcuts import render,redirect


def encurtar(request):
    #return HttpResponse('Encurtador de Link')
    return render(request, 'encurtadordelink.html')
