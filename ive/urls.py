from django.urls import path
from ive import views

app_name = 'ive'

urlpatterns = [
    path('oneyoung/', views.show_oneyoung(), name='show_oneyoung'),
    path('youjin/', views.show_youjing(), name='show_youjin'),
    # path('bye_html/', views.say_bye_html, name='bye_html'),
]