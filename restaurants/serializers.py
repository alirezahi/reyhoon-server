from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.
class  FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class  AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class  CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class  RestaurantSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    categories = CategorySerializer(many=True)
    foods = FoodSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'