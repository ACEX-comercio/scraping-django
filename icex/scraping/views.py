from bs4 import BeautifulSoup
import requests
from django.shortcuts import render

# Create your views here.
def saludo(request):
    #DEFINCION DE VARIABES
    ##definimos la lista de pises
    n_pais = ["Argentina","Bolivia","Brasi","Chile","Colombia","Costa Rica","Cuba","Ecuador","El Salvador","Guayana Francesa","Granada","Guatemala","Guayana","Haiti","Honduras","Jamaica","Mexico","Nicaragua","Paraguay","Panama","Peru","Puerto  Rico","Surinam","Uruguay","Venezuela"]
    ###link del noticiero
    not_url='http://www.bbc.com/mundo/search/?q='
    for i in range(len(n_pais)):
        url_pais=not_url+n_pais[i]
        print url_pais
    a=1
    b=3
    sum=a+b
    nombre="Israel"
    suma=sum
    blog="https://www.uno-de-piera.com"
    tupla=(1,2,3,4,5,6,7,8,9,10)
    context={
        'saludo':'hola que ase',
        'tupla':tupla,
        'nombre':nombre,
        'blog':blog,
        'suma':suma
    }
    #devolvemos los datos a la vista saludo.html
    return render(request, 'main.html', context)
    