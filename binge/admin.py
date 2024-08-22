from django.contrib import admin
from binge.models import Movie, Platform, Review

# Register your models here.


admin.site.register(Movie)
admin.site.register(Platform)
admin.site.register(Review)