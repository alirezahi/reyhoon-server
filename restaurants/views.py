from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

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


def restaurants_get(request, restaurant_id):
    if request.method == 'GET':
        restaurant = Restaurant.objects.filter(restaurant_id=restaurant_id)
        if restaurant.count() <= 0:
            return JsonResponse({})
        restaurant = restaurant.last()
        restaurant_detail = RestaurantSerializer(restaurant)
        return JsonResponse(restaurant_detail.data,safe=False)


def restaurants_comments(request, restaurant_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(co_restaurant_list__restaurant_id=restaurant_id).order_by('-created_at')
        comments_list = CommentSerializer(comments, many=True)
        return JsonResponse(comments_list.data,safe=False)


def area_list(request):
    if request.method == 'GET':
        params = request.GET
        area = params.get('area', '')
        areas = Address.objects.filter(area__icontains=area).values('area')
        areas_list = AreaSerializer(areas, many=True)
        return JsonResponse(areas_list.data,safe=False)