from django.urls import path
from .views.home import home, service, product, about, client
from .views.feedback import feedback
from .views.project import project
from .views.wishlists import wishlists
from .views.contact import contact
from .views.login import LoginView, LogoutView
from .views.profile import ProfileView
from .views.signup import signup


urlpatterns = [
    path("",home.as_view(),name='home'),
    path("about",about,name='about'),
    path("service",service,name='service'),    
    path("project",project.as_view(),name='project'),
    path("product",product,name='product'),
    path("client",client,name="client"),
    path("contact",contact.as_view(),name='contact'),
    path("feedback",feedback.as_view(),name='feedback'),
    path("wishlists",wishlists,name='wishlists'),
    path("signup",signup.as_view(),name='signup'),
    path("login",LoginView.as_view(),name='login'),
    path("logout/",LogoutView.as_view(),name='logout'),
    path("profile", ProfileView.as_view(), name="profile"),
]