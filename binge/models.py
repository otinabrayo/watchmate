from django.db import models

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