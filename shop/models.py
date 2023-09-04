from django.db import models


class tech(models.Model):
    name = models.CharField(max_length=300)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    count = models.IntegerField()
    cost = models.FloatField()
    pic = models.ImageField(upload_to="shop/static/image")

# Create your models here.



# python manage.py makemigration
# python manage.py migrate
#python manage.py createsuperuser


