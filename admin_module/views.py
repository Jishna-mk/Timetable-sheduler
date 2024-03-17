
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from teacher.models import Teacher
from student.models import Student



def login_admin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect('admin-dashboard')
            else:
                
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'admin_module/admin_login.html', {'form': form})


def admin_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('admin-login') 



@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    teachers_to_approve = Teacher.objects.filter(is_approved=False)
    students_to_approve = Student.objects.filter(is_approved=False)
    
    context = {
        'teachers_to_approve': teachers_to_approve,
        'students_to_approve': students_to_approve,
    }
    
    return render(request, 'admin_module/admin_dashboard.html', context)


def approve_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.is_approved = True
    teacher.save()
    return redirect('admin-dashboard')

def approve_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.is_approved = True
    student.save()
    return redirect('admin-dashboard')

def remove_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('admin-dashboard')

def remove_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    return redirect('admin-dashboard')