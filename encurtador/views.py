from django.http import HttpResponse
from django.shortcuts import render


def encurtadordelink(request):
    #return HttpResponse('Encurtador de Link')
    return render(request, 'encurtadordelink.html')