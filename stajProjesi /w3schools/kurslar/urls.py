
from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name='index'),
    path("html/<str:ref_ad>/",html,name='html'),
    path('<str:kat_ad>/',deneme,name='deneme'),
    # path('search/',search,name="search"),
]