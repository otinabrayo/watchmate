from rest_framework import viewsets, generics
from binge.models import Movie, Platform, Review
from binge.api.serializers import MovieSerializer, PlatformSerializer, ReviewSerializer   
    
class MovieVS(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer 
       
class PlatformVS(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)
        serializer.save(watchlist=movie)
        
class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    