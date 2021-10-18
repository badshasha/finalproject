from django.urls import path
from . import views

urlpatterns = [
    path("",views.adminHomepage,name="adminHomePage"),
    path("subject_json/",views.subjectInfo,name='subject_json'),
    path("staffpriv_json/",views.userinfo_json,name='staffuser_json'),
    path("traffic_json/",views.traffic_json,name='trafic'),
]
