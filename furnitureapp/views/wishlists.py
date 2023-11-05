from django.shortcuts import render
from furnitureapp.middlewares.auth import auth_middleware
from furnitureapp.models.product import Product
from django.views import View

@auth_middleware
def wishlists(request):
    cart = request.session.get("cart", {})
    if request.method == "GET":
        ids = list(request.session.get("cart").keys() )
        products = Product.get_all_products_by_id(ids)
    elif request.method == "POST":
        product_id = request.POST.get("product")
        if product_id:
            cart = request.session.get("cart", {})
            if product_id in cart:
                cart.pop(product_id, None)
                request.session["cart"] = cart
                request.session.modified = True

        # Fetch the updated list of products after removal
        ids = list(request.session.get("cart").keys())
        products = Product.get_all_products_by_id(ids)

    return render(request, "wishlists.html", {"products": products})

