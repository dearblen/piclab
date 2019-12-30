from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return HttpResponse("my home")

def home(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'list.html')

def document(request):
    return render(request, 'document.html')

def test_ajax(request):
    return render(request, 'test_ajax.html')