from django.shortcuts import render
from furnitureapp.models.feedback import Feedback
from django.views import View


class feedback(View):
    def get(self, request):
        return render(request, "feedback.html")

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        description = request.POST.get("desc")
        # print(name, email, description)
        feedback = Feedback(name=name, email=email, feedback_description=description)
        feedback.save()
        return render(request, "feedback.html")
