from django.db import models

# Create your models here.
class Order(models.Model):
    # Defining constants for the pizza sizes
    TOPPING_CHOICES = [
        ('Plain', 'Plain'),
        ('Meat', 'Meat'),
        ('Veggie', 'Veggie'),
        ('Margherita', 'Margherita'),
        ('Mushroom Spinach', 'Mushroom Spinach')
    ]
    
    # Fields
    comment = models.TextField(max_length=300, blank=True, default='No Comment')
    pizza_type = models.CharField( choices=TOPPING_CHOICES, default='Plain')
    
    