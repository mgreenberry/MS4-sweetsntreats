from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView


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
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Reviews(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="reviews"
        )
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    review_title = models.CharField(max_length=254)
    review_body = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ['-date_added']

    def __str__(self):
        return self.review_title


class Favourite(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_profile}, {self.product}'


class FavouritesList(models.Model):
    favourites = models.ForeignKey(
        Favourite, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.id)
