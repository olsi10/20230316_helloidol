from django.urls import path
from ive import views

app_name = 'ive'

urlpatterns = [
    path('ive/show_one/', views.show_one, name='show_one'),
    path('ive/show_you/', views.show_you, name='show_you'),
    # path('bye_html/', views.say_bye_html, name='bye_html'),
]