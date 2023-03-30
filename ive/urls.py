from django.urls import path
from ive import views

app_name = 'ive'

urlpatterns = [
    path('show_one/', views.show_one, name='one'),
    path('show_you/', views.show_you, name='you'),
    # path('bye_html/', views.say_bye_html, name='bye_html'),
]