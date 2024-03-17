from django.shortcuts import render,redirect
from .forms import StudentRegistrationForm,StudentLoginForm
from .models import Student
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from timetable.models import TimetableEntry


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            student = Student.objects.create(user=user, class_name=form.cleaned_data['class_name'])
            if student.is_approved:
                messages.success(request, 'Student registration successful.')
                return redirect('student-login')  
            else:
                return render(request, 'student/waiting_approval.html')
           
    else:
        form = StudentRegistrationForm()

    return render(request, 'student/register.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                try:
                    student = user.student
                    if student.is_approved:
                        return redirect('student-dashboard')
                    else:
                        return render(request, 'student/waiting_approval.html')
                except Student.DoesNotExist:
                    
                    pass

    else:
        form = StudentLoginForm()

    return render(request, 'student/login.html', {'form': form})



def student_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('student-login') 




def student_dashboard(request):
    user = request.user
    if hasattr(user, 'student'):
        
        class_name = user.student.class_name
        timetable_entries = TimetableEntry.objects.filter(class_name__class_name=class_name)
        
       
        print(f"Class Name: {class_name}")
        print(f"Timetable Entries: {timetable_entries}")

        context = {'timetable_entries': timetable_entries}
        return render(request, 'student/dashboard.html', context)
    else:
        
        return render(request, 'login.html')
