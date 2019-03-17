# Generated by Django 2.1.7 on 2019-03-11 19:47

from django.db import migrations
from django.conf import settings
import os.path
import csv
from django.core.files import File


def load_dog_data(apps, schema_editor):
    """
    Read a CSV file full of dogs and insert them into the database.
    """
    Dog = apps.get_model('core', 'Dog')
    datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    datafile = os.path.join(datapath, 'dogs.csv')
    with open(datafile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            dog_name = row['name']
            # Don't create a dog if one with that name already exists.
            if Dog.objects.filter(name=dog_name).count():
                continue
            dog = Dog(
                name=row['name'],
                size=row['size'],
                age=row['age'],
                good_with_kids=row['good_with_kids'],
                good_with_dogs=row['good_with_dogs'],
                good_with_cats=row['good_with_cats'],
                energy_level=3)
            dog.picture.save(
                row['image'],
                File(open(os.path.join(datapath, row['image']), 'rb')))

            dog.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_adoptionapplication'),
    ]

    operations = [migrations.RunPython(load_dog_data)]