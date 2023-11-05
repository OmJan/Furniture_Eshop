from django.shortcuts import render
from furnitureapp.models.project import Project
from furnitureapp.models.project_category import Project_Categorie
from django.views import View


class project(View):
    def get(self, request):
        project_categorie = Project_Categorie.get_all_project_categories()
        Category_id = request.GET.get("project_category")
        if Category_id:
            project = Project.get_all_project_by_category_id(Category_id)
        else:
            project = Project.get_all_project()
        data = {}
        data["projects"] = project
        data["projects_categories"] = project_categorie
        return render(request, "project.html", data)
