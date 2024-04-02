from django.db import models

# Create your models here.
class Order(models.Model):
    # Defining constants for the pizza sizes
    PIZZA_TYPE = [
        ('Plain', 'Plain'),
        ('Meat', 'Meat'),
        ('Veggie', 'Veggie'),
        ('Margherita', 'Margherita'),
        ('Mushroom Spinach', 'Mushroom Spinach')
    ]
    
    MAX_PIZZA_LENGTH = max(len(pizza_type[0]) for pizza_type in PIZZA_TYPE)

    # Fields
    comment = models.TextField(max_length=300, blank=True, default='No Comment')
    pizza_type = models.CharField(max_length=MAX_PIZZA_LENGTH, choices=PIZZA_TYPE, default='Plain')
    
    