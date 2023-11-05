from django.shortcuts import render, redirect
from furnitureapp.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.views import View

class LoginView(View):
    def get(self, request):
        # if request.method == "GET":
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            customer = Customer.objects.get(email=email)
            if check_password(password, customer.password):
                request.session["customer_id"] = customer.id
                request.session["email"] = customer.email
                print("Email stored in session:", request.session.get("email"))  # Debug
                return redirect("home")
            else:
                error_message = "Email is not valid"
                return render(request, "login.html", {"error": error_message})
        except Customer.DoesNotExist:
            error_message = "Customer Does not Exits"
            return render(request, "login.html", {"error": error_message})
        return render(request, "signin.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")