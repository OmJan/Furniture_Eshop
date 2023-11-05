from django.db import models


class Client(models.Model):
    title1 = models.CharField(max_length=40, default="")
    image = models.ImageField(upload_to="upload/client/")

    @staticmethod
    def get_all_client():
        return Client.objects.all()

    def __self__(self):
        return self.title1
