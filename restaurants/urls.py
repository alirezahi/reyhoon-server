
from django.urls import path

from . import views as restaurants_views

urlpatterns = [
    path('restaurants/<restaurant_id>/comments/', restaurants_views.restaurants_comments),
    path('restaurants/<restaurant_id>/', restaurants_views.restaurants_get),
    path('restaurants/', restaurants_views.restaurants_list),
    path('areas/', restaurants_views.area_list),
]
