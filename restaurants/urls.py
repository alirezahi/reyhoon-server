
from django.urls import path

from . import views as restaurants_views

urlpatterns = [
    path('restaurants/', restaurants_views.restaurants_list),
    path('areas/', restaurants_views.area_list),
]
