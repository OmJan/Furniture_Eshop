from django.shortcuts import render, redirect
from furnitureapp.models.contact import Contact
from django.views import View
class contact(View):
    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):
        name = request.POST.get("name")
        phone_number = request.POST.get("phone")
        email = request.POST.get("email")
        description = request.POST.get("description")
        # print(name,phone_number,email,description)
        contact = Contact(
            name=name, phone_number=phone_number, email=email, description=description
        )
        contact.save()
        return redirect("home")
