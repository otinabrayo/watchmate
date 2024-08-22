from django.http import Http404
from rest_framework import status
from binge.models import Movie, Platform
from binge.api.serializers import MovieSerializer, PlatformSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# class Review()
class MovieAV(APIView):
    
    def get(self, request):  
        desc = Movie.objects.all()   
        serializer  = MovieSerializer(desc, many=True, context={'request': request})  #context={'request': request}
        return Response(serializer.data)
                
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=Http404)
        
        
class MovieDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            desc = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MovieSerializer(desc, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        desc = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(desc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        desc = Movie.objects.get(pk=pk)
        desc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class PlatformAV(APIView):
    
    def get(self, request):
        site = Platform.objects.all()
        serializer = PlatformSerializer(site,many=True, context={'request': request})
        return Response(serializer.data)
        
        
    def post(self, request):
        serializer = PlatformSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)     

class PlatformDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            site = Platform.objects.get(pk=pk)
        except Platform.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlatformSerializer(site, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        site = Platform.objects.get(pk=pk)
        serializer = PlatformSerializer(site, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
    def delete(self, request, pk):
        site = Platform.objects.get(pk=pk)
        site.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        