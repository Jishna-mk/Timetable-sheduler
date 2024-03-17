from django.urls import path
from .import views


urlpatterns = [
    path('admin-login/',views.login_admin,name='admin-login'),
    path('admin-logout/',views.admin_logout,name='admin-logout'),
    path('admin-dashboard/',views.admin_dashboard,name='admin-dashboard'),
    path('approve_teacher/<int:teacher_id>/', views.approve_teacher, name='approve_teacher'),
    path('approve_student/<int:student_id>/', views.approve_student, name='approve_student'),
    path('remove-teacher/<int:teacher_id>/', views.remove_teacher, name='remove-teacher'),
    path('remove-student/<int:student_id>/', views.remove_student, name='remove-student'),
]