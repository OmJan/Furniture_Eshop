from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from furnitureapp.models import Customer
from django.views import View

class ProfileView(View):
    @login_required
    def get(self, request):
        try:
            # Retrieve the customer associated with the current user
            customer = Customer.objects.get(user=request.user)
            context = {
                "customer": customer,
            }
            return render(request, "profile.html", context)
        except Customer.DoesNotExist:
            print("Customer does not exist for this user.")
            return render(request, "profile.html")
