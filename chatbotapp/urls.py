from django.urls import path
from chatbotapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
