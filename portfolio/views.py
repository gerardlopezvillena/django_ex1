from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects=Project.objects.all()
#    return(HttpResponse(html_base+"<h1>Portafoli</h1><h2>Aixo es el portafoli</h2>"))
    return(render(request,"portfolio/portfolio.html",{'projects':projects}))


