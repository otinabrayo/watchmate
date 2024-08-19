from django.urls import path, include
from binge.api.views import MovieAV, MovieDetailAV, PlatformAV, PlatformDetailAV

urlpatterns = [
    path('list/', MovieAV.as_view(), name='movie-list'),
    path('list/<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
    path('site/',PlatformAV.as_view(), name='site'),
    path('site/<int:pk>',PlatformDetailAV.as_view(), name='platform-detail'),
    
]