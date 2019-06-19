from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

import json

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


@csrf_exempt
def restaurants_get(request, restaurant_id):
    if request.method == 'GET':
        restaurant = Restaurant.objects.filter(restaurant_id=restaurant_id)
        if restaurant.count() <= 0:
            return JsonResponse({})
        restaurant = restaurant.last()
        restaurant_detail = RestaurantSerializer(restaurant)
        return JsonResponse(restaurant_detail.data,safe=False)
    if request.method == 'POST':
        params = request.body
        data = json.loads(params.decode('utf8'))
        for item in ['foods','categories','comments']:
            if not(item in data):
                data[item] = []
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors)

        # name_id = data['id']
        # name = data['name']
        # logo = data['logo']
        # opening_time = data['opening_time']
        # closing_time = data['closing_time']
        # if 'address' in data:
        #     city = data['address']['city']
        #     area = data['address']['area']
        #     address_line = data['address']['address_line']
        # if 'foods' in data:
        #     for food in data['foods']:
        #         food_id = food['id']
        #         name = food['name']
        #         price = food['price']
        #         description = food['description']
        #         food_set = food['food_set']
        # if 'categories' in data:
        #     for category in data['categories']:
        #         category_id = category['id']
        #         name = category['name']
        

@csrf_exempt
def restaurants_comments(request, restaurant_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(co_restaurant_list__restaurant_id=restaurant_id).order_by('-created_at')
        comments_list = CommentSerializer(comments, many=True)
        return JsonResponse(comments_list.data,safe=False)
    if request.method == 'POST':
        r = Restaurant.objects.get(restaurant_id=restaurant_id)
        params = request.POST
        author = params.get('author','')
        quality = params.get('quality',0)
        packaging = params.get('packaging',0)
        delivery_time = params.get('delivery_time',0)
        text = params.get('text','')
        comment, is_created = Comment.objects.get_or_create(author=author,quality=quality,packaging=packaging,delivery_time=delivery_time,text=text)
        r.comments.add(comment)
        return JsonResponse({'status':'created!'},status=200)


def area_list(request):
    if request.method == 'GET':
        params = request.GET
        area = params.get('area', '')
        areas = Address.objects.filter(area__icontains=area).values('area')
        areas_list = AreaSerializer(areas, many=True)
        return JsonResponse(areas_list.data,safe=False)