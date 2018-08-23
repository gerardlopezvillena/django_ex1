from django.shortcuts import render,HttpResponse

html_base='''
Projecte Personal
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Referent a</a></li>
    <li><a href="/portfolio">Portafoli</a></li>
    <li><a href="/contact">Contacte</a></li>
</ul>
'''

# Create your views here.
def home(request):
#    return(HttpResponse(html_base+"<h1>Pagina Principal</h1><h2>Portada</h2>"))
     return(render(request,"core/home.html"))

def about(request):
#    return(HttpResponse(html_base+"<h1>Hola Django</h1><h2>Em dic Gerard i soc biotecnoleg</h2>"))
     return(render(request,"core/about.html"))

def contact(request):
#    return(HttpResponse(html_base+"<h1>Contacte</h1><h2>Informacio de contacte</h2>"))
     return(render(request,"core/contact.html"))
