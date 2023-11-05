from django.db import models
from .project_category import Project_Categorie


class Project(models.Model):
    project_image = models.ImageField(upload_to="upload/project/")
    project_category = models.ForeignKey(Project_Categorie, on_delete=models.CASCADE, null=True, blank=True)

    @staticmethod
    def get_all_project():
        return Project.objects.all()

    @staticmethod
    def get_all_project_by_category_id(category_id):
        return Project.objects.filter(project_category=category_id)