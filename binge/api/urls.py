from django.urls import path, include
from rest_framework.routers import DefaultRouter
from binge.api.views import PlatformVS, MovieVS, ReviewCreate, ReviewList, ReviewDetail

router = DefaultRouter()
router.register('site', PlatformVS, basename='sites' )
router.register('list', MovieVS, basename='lists' )

urlpatterns = [
    path('', include(router.urls)),
    
    path('site/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'), 
    path('site/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('site/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

]