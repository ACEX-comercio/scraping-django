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
    ##array de palabras mala
    #pal_malas=["muertos","virus","deficit","inflacion","destruir","huelgas","manifestaciones","pobreza","terremoto","desolacion","huracan","peligro","mueren","enfrentamiento","instabilidad","ilegales","devaluacion","perjuicio"]

    #DEFNIMOS TODA  LA LOGICA
    for i in range(len(n_pais)):
        url_pais=not_url+n_pais[i]#unimos el link y las partes
        #CAPTURAMOS EL CONTNIDO DE LA WEB 
        req = requests.get(url_pais)
        html = BeautifulSoup(req.text, "html.parser")
        #desgregamos y solo capturamos los valores de la clase hard-news-unit__headline-link
        print n_pais[i]#inprimimos en consola el nombe del pais
        noticias_pais = html.find_all("a", {"class": "hard-news-unit__headline-link"})#en la variable almasenamos todas la noticias
        for i, noticia_pais in enumerate(noticias_pais):# en este bucle sacamos todas las noticias
            noticia=noticia_pais.getText()#cogemos los titulos de las noticias
            palabra_noticia=noticia.split()#separar el titulo de las noticias
            for i, palabra in enumerate(palabra_noticia):#e buque que muestra acada palabra de la oracion
                #crearmos dos arrays uno de buenas palabras y la otra de palabras malas
                #y recoremos con un for y dentro un caomparador de palabras y al termina le damos un puntuacion
                print (palabra)
            print (palabra_noticia)
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
    