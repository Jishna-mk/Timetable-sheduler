from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register_teacher/',views.register_teacher,name='register_teacher'),
    path('login/',views.teacher_login,name='teacher-login'),
    path('teacher-dashboard/',views.teacher_dashboard,name='teacher-dashboard'),
    path('logout/',views.teacher_logout,name='teacher-logout'),
]