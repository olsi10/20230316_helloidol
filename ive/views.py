from django.shortcuts import render

# Create your views here.
def show_one(request):
    context = {
        'name': '원영',
        'url': 'http://health.chosun.com/site/data/img_dir/2011/01/06/2011010601681_0.jpg',
    }

    return render(request, 'ive/member.html', context=context)

def show_you(request):
    context = {
        'name': '유진',
        'url': 'http://www.tvj.co.kr/news/photo/202204/70870_201468_375.jpg',
    }

    return render(request, 'ive/member.html', context=context)