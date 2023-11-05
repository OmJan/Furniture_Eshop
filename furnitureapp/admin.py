from typing import Any
from django.contrib import admin
from .models.customer import Customer
from .models.client import Client
from .models.project import Project
from .models.service import Service
from .models.categories import Categorie
from .models.product import Product
from .models.slider import Slider
from .models.contact import Contact
from .models.feedback import Feedback
from .models.project_category import Project_Categorie
# from .models.profile import Profile
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Customer)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Project_Categorie)
# admin.site.register(Profile)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')

# class profile(admin.ModelAdmin):
#     list_display = ('user', 'customer', 'birthdate', 'Gender')


    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100"/>')
    
    display_image.short_description = "Image"

class Media:
        css = {
            "all": ("css/custom_admin.css",),
        }