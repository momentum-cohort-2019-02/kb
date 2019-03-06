from django.db import models

# Create your models here.


class Dog(models.Model):
    PUPPY = 'PU'
    YOUNG = 'YG'
    ADULT = 'AD'
    SENIOR = 'SR'

    AGE_CHOICES = (
        (PUPPY, 'Puppy'),
        (YOUNG, 'Young'),
        (ADULT, 'Adult'),
        (SENIOR, 'Senior'),
    )

    TINY = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'

    SIZE_CHOICES = (
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    )

    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2, choices=AGE_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    picture = models.ImageField(upload_to='dogs/', null=True)

    def __str__(self):
        return self.name
