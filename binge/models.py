from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Platform(models.Model):
    site = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.site
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name='platforms')
    release_date = models.DateField()

    def __str__(self):
        return  self.title  
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    watchlist = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    comment = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title