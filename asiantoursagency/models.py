from django.db import models

class Tour(models.Model):
    CATEGORY_CHOICES = [
        ('economic', 'Economic'),
        ('moderate', 'Moderate'),
        ('luxury', 'Luxury'),
    ]
    
    # Tour details
    title = models.CharField(max_length=200, default='Amazing Tour Package')
    description = models.TextField(default='Experience the best of your destination with our exclusive tour package.')
    origin_country = models.CharField(max_length=64, default='India')
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='moderate')
    is_hot_deal = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    image_url = models.URLField(default='https://source.unsplash.com/random/800x600/?vacation')
    
    def get_discounted_price(self):
        return self.price - (self.price * self.discount / 100)
    
    def __str__(self):
        return f"{self.title} - {self.get_category_display()} - ${self.price}"