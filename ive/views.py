from django.shortcuts import render

# Create your views here.
def show_one(request):
    context = {
        'name': '원영',
        'urls': 'https://talkimg.imbc.com/TVianUpload/tvian/TViews/image/2022/10/01/gppKEHUiAyIO638002448398716484.jpg',
    }

    return render(request, 'ive/one.html', context=context)

def show_you(request):
    context = {
        'name': '유진',
        'urls': 'http://www.tvj.co.kr/news/photo/202204/70870_201468_375.jpg',
    }

    return render(request, 'ive/you.html', context=context)