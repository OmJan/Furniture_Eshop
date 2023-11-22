from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=50)

    @staticmethod
    def get_all_sevices():
        return Service.objects.all()

    def __str__(self):
        return self.service_name
