from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    client = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tools = models.TextField()
    is_sold = models.BooleanField(default=True)
    sale_type = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    audio = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)

    

    def __str__(self):
        return self.name
