from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    feedback_description = models.TextField()

    def __str__(self):
        return self.name
