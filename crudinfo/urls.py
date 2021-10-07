from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.homepage, name="homepage"),  # homepage is "user page" not homepage
    path("<int:user_id>/", views.userPage, name="userpage"),
    path('delete/<int:user_id>/', views.deleteUser, name="deletepage"),
    path('adduser/', views.addUser, name='adduserpage')
]
