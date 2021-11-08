from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import FormLinks
from . models import Links

def encurtar(request):
    #return HttpResponse('Encurtador de Link')
    form = FormLinks()
    status = request.GET.get('status')
    return render(request, 'encurtadordelink.html',{'form':form,'status':status})

def valida_link(request):
    form = FormLinks(request.POST)
    
    link_encurtado = form.data['link_encurtado']
    print(link_encurtado)
    links = Links.objects.filter(link_encurtado = link_encurtado) 
    print(links)
    if len(links) > 0:
        return redirect("/encurtadordelink/?status=1")

    if form.is_valid():
        try:
            form.save()
            link_ = 'http://localhost:8000/encurtadordelink/' +link_encurtado
            return HttpResponse (f"O seu link foi criado com sucesso e é: <a href='{link_}' target='_blank'>{link_}</a>")
        except:
            return HttpResponse ('Erro interno no sistema')

def redirecionar(request,link):
    return HttpResponse(link)