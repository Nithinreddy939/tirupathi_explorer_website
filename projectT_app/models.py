from django.db import models

# Create your models here.

#creating one data table for storing data in database

class Tirupathi_data_collection(models.Model):
    name = models.CharField( max_length=200)
    description = models.TextField()
    category = models.IntegerField()
    image = models.ImageField(upload_to='static/images') 
    category_name =models.CharField( max_length=50)
    def __str__(self):
        return self.name