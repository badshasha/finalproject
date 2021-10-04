from django.urls import path
from . import views

urlpatterns = [
    path("",views.adminHomepage,name="adminHomePage"),
]
