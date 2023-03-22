from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("hello world")

def say_hello_html(request):
    return render(request, "playground/hello.html")