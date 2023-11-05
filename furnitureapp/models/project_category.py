from django.db import models

class Project_Categorie(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_project_categories():
        return Project_Categorie.objects.all()