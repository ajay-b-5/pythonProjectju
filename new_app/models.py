from django.db import models

# Create your models here.
class foodName(model.model):
    food_category = (
        ('veg','veg'),
        ('non','non')
    )