from django.shortcuts import render, redirect
from django.contrib.auth import logout
from furnitureapp.models.product import Product
# from furnitureapp.models.profile import Profile
from furnitureapp.models.project import Project
from furnitureapp.models.categories import Categorie
from furnitureapp.models.client import Client
from furnitureapp.models.service import Service
from django.views import View