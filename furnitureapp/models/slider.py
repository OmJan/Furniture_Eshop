from django.db import models

class Slider(models.Model):
    s_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to="upload/slider/")

    @staticmethod
    def get_all_slider():
        return Slider.objects.all()
    
    def __str__(self):
        return self.s_name
    





