from django.db import models
from .categories import Categorie


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, default="", null=True, blank=True
    )
    description = models.TextField()
    image = models.ImageField(upload_to="upload/products/")

    @staticmethod
    def get_all_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.name
