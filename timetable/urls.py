from django.urls import path
from .import views


urlpatterns = [
    path('create-subject/',views.create_subject,name='create-subject'),
    path('create-lab/',views.create_lab,name='create-lab'),
    path('create-class/',views.create_class,name='create-class'),
    path('view-classes/',views.view_classes,name='view-classes'),
    path('edit-class/<int:class_id>/',views.edit_class,name='edit-class'),
    path('delete-class/<int:class_id>/', views.delete_class, name='delete-class'),

    path('generate-timetable/',views.generate_timetable_view,name='generate-timetable'),
    path('display-timetable/',views.display_timetable,name='display-timetable'),
    
]