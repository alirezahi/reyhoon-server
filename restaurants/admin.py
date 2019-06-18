from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Address)