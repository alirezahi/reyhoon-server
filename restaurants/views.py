from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *

# Create your views here.

def restaurants_list(request):
    if request.method == 'GET':
        params = request.GET
        params = [
            ('area', params.get('area', None)),
            ('categories__name', params.get('category', None)),
        ]
        filters = dict( (key, value) for (key, value) in params if value != None )
        restaurants = Restaurant.objects.filter(**filters)
        restaurants_list = RestaurantSerializer(restaurants, many=True)
        return JsonResponse(restaurants_list.data,safe=False)


def area_list(request):
    if request.method == 'GET':
        params = request.GET
        area = params.get('area', '')
        areas = Address.objects.filter(area__icontains=area).values('area')
        areas_list = AreaSerializer(areas, many=True)
        return JsonResponse(areas_list.data,safe=False)