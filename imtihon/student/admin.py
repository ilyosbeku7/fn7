from django.contrib import admin
from .models import Cities, Category, AirWays
# Register your models here.
admin.site.register(Cities)
admin.site.register(Category)
admin.site.register(AirWays)