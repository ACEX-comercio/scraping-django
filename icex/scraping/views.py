from bs4 import BeautifulSoup
import requests
from django.shortcuts import render

# Create your views here.
url='http://www.radiouno.pe/'
def saludo(request):
    req = requests.get(url)
    html = BeautifulSoup(req.text, "html.parser")
    print html
    #status_code = req.status_code
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
    
cesar escobar certificado virtual inportacion de china 