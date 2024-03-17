from django.urls import path
from .import views

urlpatterns = [
    path('register_student/',views.register_student,name='register_student'),
    path('login/',views.student_login,name='student-login'),
    path('logout/',views.student_logout,name='student_logout'),
    path('student-dashboard/',views.student_dashboard,name='student-dashboard'),

]