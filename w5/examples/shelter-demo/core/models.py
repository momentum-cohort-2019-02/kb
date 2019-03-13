from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class DogBreed(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


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

    EASYGOING = 1
    PLAYFUL = 3
    ENERGETIC = 5

    ENERGY_LEVEL_CHOICES = (
        (EASYGOING, 'Easygoing'),
        (PLAYFUL, 'Playful'),
        (ENERGETIC, 'Energetic'),
    )

    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2, choices=AGE_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    breed = models.ForeignKey(
        DogBreed, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    energy_level = models.PositiveIntegerField(choices=ENERGY_LEVEL_CHOICES)
    picture = models.ImageField(upload_to='dogs/', null=True)
    good_with_kids = models.BooleanField(
        verbose_name="Good with kids", default=False)
    good_with_dogs = models.BooleanField(
        verbose_name="Good with other dogs", default=False)
    good_with_cats = models.BooleanField(
        verbose_name="Good with cats", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    favorited_by = models.ManyToManyField(
        to=User, related_name='favorite_dogs', through='Favorite')

    class Meta:
        ordering = ['-created_at']

    def get_traits(self):
        traits = []
        traits.append(self.get_age_display())
        traits.append(self.get_size_display())
        traits.append(self.get_energy_level_display())
        if self.good_with_kids:
            traits.append("Good with kids")
        if self.good_with_dogs:
            traits.append("Good with other dogs")
        if self.good_with_cats:
            traits.append("Good with cats")

        return traits

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dog_detail', args=(self.pk,))


class AdoptionApplication(models.Model):
    dog = models.ForeignKey(
        Dog, related_name='applications', on_delete=models.PROTECT)
    applicant = models.ForeignKey(
        User, related_name='applications', on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=20)
    current_pets = models.PositiveIntegerField("Number of current pets")
    fenced_backyard = models.BooleanField("Do you have a fenced backyard?")
    applied_at = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    dogs = models.ManyToManyField(Dog, related_name='events', blank=True)

    class Meta:
        ordering = ['start_at']

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        # If the slug is already set, stop here.
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        # while we can find a record already in the DB with the slug
        # we're trying to use
        while Event.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)

        self.slug = slug

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)
