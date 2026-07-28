from django.shortcuts import render
from apps.projects.models import Project

# Create your views here.
def home(request):

    #On affiche tous les projets
    #projects = Project.objects.all()
    
    #On affiche les projets que si on a coché qu'ils devaient être en ligne
    #De plus, dernier projet créé, = premier dans la vue. (le [-] = +récent au + ancien)

    return render(request, "core/home.html",)