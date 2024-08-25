from rest_framework import serializers
from binge.models import Movie, Platform, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        # exclude = ('watchlist',)
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'       
        
class PlatformSerializer(serializers.ModelSerializer):
    platforms = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = Platform
        fields = '__all__'