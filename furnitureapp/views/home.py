from django.shortcuts import render
from furnitureapp.models.product import Product
from furnitureapp.models.client import Client
from furnitureapp.models.categories import Categorie
from furnitureapp.models.service import Service
from furnitureapp.models.slider import Slider
from django.views import View


class home(View):

    def post(self, request):
        products = Product.get_all_products()
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart", {})
        if product in cart:
            if remove:
                if cart[product] <= 1:
                    cart.pop(
                        product, None
                    )  # Remove the key if it exists, or do nothing if it doesn't
                else:
                    cart[product] -= 1
            else:
                cart[product] += 1
        else:
            cart[product] = 1
        request.session["cart"] = cart  # Update the cart in the session
        data ={
            "products": products
        }
        return render(request, "home.html",data)

    def get(self, request):
        products = Product.get_all_products()
        slider = Slider.get_all_slider()
        data ={
            "sliders":slider,
            "products": products,
        }
        return render(request, "home.html", data)


def about(request):
    return render(request, "about.html")


def client(request):
    client = Client.get_all_client()
    return render(request, "client.html", {"clients": client})


def product(request):
    products = None
    category = Categorie.get_all_categories()
    categoryID = request.GET.get("category")
    if categoryID:
        products = Product.get_all_products_by_category_id(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data["products"] = products
    data["categories"] = category
    return render(request, "product.html", data)


def service(request):
    services = Service.get_all_sevices()
    service_data = []
    for service in services:
        service_name_hash = abs(hash(service.service_name)) % 16777215 
        service_data.append({
            'service':service,
            'service_name_hash': service_name_hash
        })

    return render(request, "service.html", {"services": service_data})


