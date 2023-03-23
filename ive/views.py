from django.shortcuts import render

def show_oneyoung(request):
    context = {
        'name': '원영',
        'url': 'https://img.hankyung.com/photo/202207/BF.30710089.1.jpg',
    }
    return render(request, "ive/oneyoung.html", context=context)

def show_youjin(request):
    context = {
        'name': '유진',
        'url': 'http://newsimg.hankookilbo.com/2015/04/12/201504121021832835_1.jpg',
    }
    return render(request, "ive/oneyoung.html", context=context)