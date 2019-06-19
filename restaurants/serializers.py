from rest_framework import routers, serializers, viewsets
from .models import *


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

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


class  AreaSerializer(serializers.Serializer):
    area = serializers.CharField(max_length=50)


class  RestaurantSerializer(serializers.ModelSerializer):
    # logo = Base64ImageField(
    #     max_length=None, use_url=True,
    # )
    address = AddressSerializer()
    categories = CategorySerializer(many=True)
    foods = FoodSerializer(many=True)
    comments = CommentSerializer(many=True)
    average_rate = serializers.ReadOnlyField()

    class Meta:
        model = Restaurant
        # fields = '__all__'
        exclude = ['logo']
    
    def create(self, validated_data):
        foods_data = validated_data.pop('foods')
        categories_data = validated_data.pop('categories')
        comments_data = validated_data.pop('comments')
        address_data = validated_data.pop('address')
        print(foods_data)
        r = Restaurant.objects.create(**validated_data)
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            a = Address.objects.create(**address_data)
            r.address = a
        for food in foods_data:
            food_serializer = FoodSerializer(data=food)
            if food_serializer.is_valid():
                f = Food.objects.create(**food)
                r.foods.add(f)
        for category in categories_data:
            category_serializer = CategorySerializer(data=category)
            if category_serializer.is_valid():
                c = Category.objects.create(**category)
                r.categories.add(c)
        return r

