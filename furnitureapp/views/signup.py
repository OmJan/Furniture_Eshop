from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from furnitureapp.models.customer import Customer
from django.views import View

class signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # initialize error_message as None
        error_message = None

        # validate
        if not first_name:
            error_message = "First Name is required"
        elif len(first_name) < 4:
            error_message = "Firt name must be 5 character or more"
        elif not last_name:
            error_message = "Last Name is required"
        elif not email:
            error_message = "Email id  is required"
        elif not phone:
            error_message = "Phone Number is required"
        elif not password:
            error_message = "Password is required"

        if error_message:
            return render(request, "signup.html", {"error": error_message})

        # converrt it into hash password
        hash_password = make_password(password)

        # Create a new Customer instance and save it to the database
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=hash_password,
        )
        customer.save()
        return redirect("home")
        return render(request, "signup.html")
