from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render( request, 'AppTemplates/index.html')

def reader():
    pass


def post():
    pass

def search(request):
    return HttpResponse('ok')