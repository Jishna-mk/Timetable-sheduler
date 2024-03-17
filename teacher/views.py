from django.shortcuts import render,redirect
from .models import Teacher
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import TeacherRegistrationForm,TeacherLoginForm
from timetable.models import TimetableEntry


def index(request):
    return render(request,"index.html")

# def register_teacher(request):
#     if request.method == 'POST':
#         form = TeacherRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             teacher = Teacher.objects.create(user=user, subject_taught=form.cleaned_data['subject_taught'])

#             if teacher.is_approved:
#                 messages.success(request, 'Teacher registration successful.')
#                 return redirect('teacher-login')  
#             else:
#                 return render(request, 'teacher/waiting_approval.html')
             
#     else:
#         form = TeacherRegistrationForm()

#     return render(request, 'teacher/register.html', {'form': form})
def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Extract subject_taught1 and subject_taught2 from the form
            subject_taught1 = form.cleaned_data['subject_taught1']
            subject_taught2 = form.cleaned_data['subject_taught2']
            # Create the teacher object with the correct subjects
            teacher = Teacher.objects.create(user=user, subject_taught1=subject_taught1, subject_taught2=subject_taught2)

            if teacher.is_approved:
                messages.success(request, 'Teacher registration successful.')
                return redirect('teacher-login')  
            else:
                return render(request, 'teacher/waiting_approval.html')
    else:
        form = TeacherRegistrationForm()

    return render(request, 'teacher/register.html', {'form': form})


def teacher_login(request):
    if request.method == 'POST':
        form = TeacherLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                try:
                    teacher = user.teacher
                    if teacher.is_approved:
                        return redirect('teacher-dashboard')
                    else:
                        return render(request, 'teacher/waiting_approval.html')
                except Teacher.DoesNotExist:
                    
                    pass

    else:
        form = TeacherLoginForm()

    return render(request, 'teacher/login.html', {'form': form})


def teacher_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('teacher-login') 

from django.db.models import Q

def teacher_dashboard(request):
    user = request.user

    if hasattr(user, 'teacher'):
        teacher = user.teacher
        subject_taught1 = teacher.subject_taught1
        subject_taught2 = teacher.subject_taught2

        # Filter timetable entries for both subjects
        timetable_entries = TimetableEntry.objects.filter(
            Q(subject__name=subject_taught1) | Q(subject__name=subject_taught2)
        )

        context = {'timetable_entries': timetable_entries}
        return render(request, 'teacher/dashboard.html', context)
    else:
        return render(request, 'login.html')
