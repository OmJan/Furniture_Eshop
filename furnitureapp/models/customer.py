from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def get_all_customer():
        return Customer.objects.all()

    def __str__(self):
        return self.first_name+self.last_name