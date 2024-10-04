from django.db import models
from django_resized import ResizedImageField


class Users(models.Model):
    GENDER_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
        ('Boshqa', 'Boshqa'),
    ]

    REGION_CHOICES = [
        ('Toshkent', 'Toshkent'),
        ('Andijon', 'Andijon'),
        ('Samarqand', 'Samarqand'),
        ('Buxoro', 'Buxoro'),
        # Yana boshqa regionlarni qo'shishingiz mumkin
    ]

    CITY_CHOICES = [
        ('Toshkent shahar', 'Toshkent shahar'),
        ('Andijon shahar', 'Andijon shahar'),
        ('Samarqand shahar', 'Samarqand shahar'),
        # Boshqa shaharlar
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    birth_date = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    city_or_district = models.CharField(max_length=50, choices=CITY_CHOICES)
    profile_image = ResizedImageField(size=[100, 100], crop=['middle', 'center'], upload_to='profiles/')
        
    def __str__(self):
        return f"{self.name}"