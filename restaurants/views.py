from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *

# Create your views here.

def restaurants_list(request):
    restaurants = Restaurant.objects.all()
    restaurants_list = RestaurantSerializer(restaurants, many=True)
    return JsonResponse(restaurants_list.data,safe=False)