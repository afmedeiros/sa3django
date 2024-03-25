from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func1(request):
    return render(request,"app_aula/index.html")


def sobre(request):
    return render(request,"app_aula/sobre.html")

def discografia(request):
    return render(request,"app_aula/discografia.html")    

def menu(request):
    return render(request,"app_aula/menu.html")    