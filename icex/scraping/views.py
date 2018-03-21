from bs4 import BeautifulSoup
import requests
from django.shortcuts import render

#funcion para ver si nesesiamos trasformar
def decodificacion(codepalabra):
    if len(codepalabra)<2:
        auxpalabra=codepalabra.encode("latin1")
    else:
        auxpalabra=codepalabra
    return auxpalabra.lower()

# creamos una vista.
def saludo(request):
    #DEFINCION DE VARIABES
    ##definimos la lista de pises
    #,"Brasi","Chile","Colombia","Costa Rica","Cuba","Ecuador","El Salvador","Guayana Francesa","Granada","Guatemala","Guayana","Haiti","Honduras","Jamaica","Mexico","Nicaragua","Paraguay","Panama","Peru","Puerto  Rico","Surinam","Uruguay","Venezuela"
    n_pais = ["Argentina","Bolivia","Brasi"]
    ###link del noticiero
    not_url='http://www.bbc.com/mundo/search/?q='
    ##array de palabras mala
    pal_malas=["muertos","virus","deficit","inflacion","destruir","huelgas","manifestaciones","pobreza","terremoto","desolacion","huracan","peligro","mueren","enfrentamiento","instabilidad","ilegales","devaluacion","perjuicio","riesgo","falta","asesinatos","muertes","muerte","pobreza","matar","violar","marihuana"]
    pal_buenas=["crea","reduce","resuelve","deflacion","dinero","comienza","remplasara","peruana","gana","bien","cura","salva","vivio","capturado","premio","suerte","encontro","gano","participa","triunfo","castigo","promesas"]

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
            punt_nbuenas=0
            punt_nmalas=0   
            punt_nneutro=0
            #for i, palabra in enumerate(palabra_noticia):
                #print palabra
            for i, palabra in enumerate(palabra_noticia):#e buque que muestra acada palabra de la oracion
                #crearmos dos arrays uno de buenas palabras y la otra de palabras malas
                #y recoremos con un for y dentro un caomparador de palabras y al termina le damos un puntuacion
                for i, pal_mala in enumerate(pal_malas):
                    if decodificacion(palabra)==pal_mala:
                        punt_nmalas=punt_nmalas+1
                        print "palabra mala : ", pal_mala
                for i, pal_buena in enumerate(pal_buenas):
                    if decodificacion(palabra)==pal_buena:
                        punt_nbuenas=punt_nbuenas+1
                        print "palabra buena : ", pal_buena

                #print (decodificacion(palabra).lower())
            print (palabra_noticia)
            print "buenas : ",punt_nbuenas
            print "malas : ",punt_nmalas
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
    