from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.FileField(upload_to='photos/product')
    description = models.TextField(max_length=500)
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_info', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
