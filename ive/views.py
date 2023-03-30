from django.shortcuts import render

# Create your views here.
def show_one(request):
    context = {
        'name': '원영',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_KOtw4lFxVSNSaTLdLoHyilh2GK6olIaHtIYP3-dVdw&s',
    }

    return render(request, 'ive/member.html', context=context)

def show_you(request):
    context = {
        'name': '유진',
        'url': 'http://www.tvj.co.kr/news/photo/202204/70870_201468_375.jpg',
    }

    return render(request, 'ive/member.html', context=context)