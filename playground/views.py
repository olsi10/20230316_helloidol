from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("hello world")

def say_hello_html(request):
    return render(request, "playground/hello.html", {'name': '세상쨔응', 'greeting':
                                                     '반가우이'})

def say_bye(request):
    return HttpResponse("bye!")

def say_bye_html(request):
    context = {
        'name': '김지훈 선생님',
        'bye': '안녕히...',
    }
    return render(request, "playground/bye.html", context=context)
