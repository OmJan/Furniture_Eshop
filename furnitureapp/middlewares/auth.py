from django.shortcuts import redirect

def auth_middleware(get_response):
    def middlerware(request):
        response = get_response(request)
        if not request.session.get('customer_id'):
            request.session["cart"] = {}
            return redirect("login")
        return response

    return middlerware