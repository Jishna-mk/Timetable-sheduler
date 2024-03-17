from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Teacher
from timetable.models import Subject

class TeacherRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    subject_taught = forms.ModelChoiceField(queryset=Subject.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'subject_taught']





class TeacherLoginForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ['username', 'password']