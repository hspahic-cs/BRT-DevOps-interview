from django.db import models

# Create your models here.
class Order(models.Model):
    # Defining constants for the pizza sizes
    TOPPING_CHOICES = [
        ('P', 'Pepperoni'),
        ('M', 'Mushrooms'),
        ('O', 'Onions'),
        ('S', 'Sausage'),
        ('B', 'Bacon'),
        ('G', 'Extra cheese'),
        ('', 'None')
    ]
    
    # Fields
    comment = models.TextField(max_length=300, blank=True)
    toppings = models.CharField(max_length=1, 
                                choices=TOPPING_CHOICES, 
                                default='')
    
    