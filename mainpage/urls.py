from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadMain ,name = "indexpage"),
    path('login/',views.login , name= "login"),
    path('signin/',views.singin , name = "sign"),
    path('dashboard/',views.userDashBroard,name='userdashbord'),
    path('logout/',views.logout,name='logout'),
    path('selectsubject/',views.userDashBrod_selectedsub,name='selecet_subject'),
    path('addusersubject/',views.addusersubject,name='adduser_subject'),
    path('removeusersubject/<int:id>',views.removeusersubject,name='removeuser_subject'),
    path('exampage/', views.exampage, name='exampage'),
    path('dashboard/json/', views.json, name='test_json'),
    path('dashboard/json_subject',views.json_subject,name='json_subject'),
    path('exampage/sub/<int:id>',views.examsubtopic,name="examsubtopic"),#json
    path('exampage/sub/subexam/<int:id>',views.examsubtopicpage , name ="examsubtopicpage"), # real page
    path('exampage/check',views.testingPost,name="check"),
    path('exampage/exam_json',views.getExamResult,name='exam_json'),
    # path('exampage/exam_chart/<int:id>', views.getSubjectChart, name='exam_chart'),   # delete this code
    path('exampage/json/<int:id>',views.getSubjectChart , name='exam_sub_json'), # get json informatoin
    path('exampage/json_chart/<int:id>', views.getChart, name='exam_chart'),
    path('exampage/fullpage/<int:id>',views.fullpaper,name='fullpapaer'),
]
