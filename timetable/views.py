from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .forms import ClassForm,SubjectForm, TimetableGenerateForm,LabForm
from .models import Class,TimetableEntry
from .generate_timetable import generate_timetable
from django.http import JsonResponse


@user_passes_test(lambda u: u.is_superuser)
def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = SubjectForm()

    return render(request, 'timetable/create_subject.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def create_lab(request):
    if request.method == 'POST':
        form = LabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = LabForm()

    return render(request, 'timetable/create_lab.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def create_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')  
    else:
        form = ClassForm()

    return render(request, 'timetable/create_class.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def view_classes(request):
    classes = Class.objects.all()
    return render(request, 'timetable/view_classes.html', {'classes': classes})


@user_passes_test(lambda u: u.is_superuser)
def edit_class(request, class_id):
    instance = get_object_or_404(Class, id=class_id)
    
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('view-classes') 
    else:
        form = ClassForm(instance=instance)

    return render(request, 'timetable/edit_class.html', {'form': form})



@user_passes_test(lambda u: u.is_superuser)
def delete_class(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)
    
    if request.method == 'POST':
        class_instance.delete()
        return JsonResponse({'message': 'Class deleted successfully'})

    return render(request, 'timetable/view_classes.html', {'class_instance': class_instance})



@user_passes_test(lambda u: u.is_superuser)
def generate_timetable_view(request):
    if request.method == 'POST':
        form = TimetableGenerateForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm_generation']:
            selected_class = form.cleaned_data['selected_class']
            generate_timetable(selected_class)
            return redirect('display-timetable')
    else:
        form = TimetableGenerateForm()

    context = {'form': form}
    return render(request, 'timetable/generate_timetable.html', context)





# def display_timetable(request):
#     user = request.user
#     if hasattr(user, 'teacher'):
#         timetable_entries = TimetableEntry.objects.filter(subject=user.teacher.subject_taught1)
#         timetable_entries = TimetableEntry.objects.filter(subject=user.teacher.subject_taught2)
        
#     elif hasattr(user, 'student'):
#         timetable_entries = TimetableEntry.objects.filter(class_name=user.student.class_name)
#     else:
#         timetable_entries = TimetableEntry.objects.all()

    
#     timetable_by_class = {}
#     for entry in timetable_entries:
#         if entry.class_name not in timetable_by_class:
#             timetable_by_class[entry.class_name] = []
#         timetable_by_class[entry.class_name].append(entry)

#     context = {'timetable_by_class': timetable_by_class}
#     return render(request, 'timetable/display_timetable.html', context)
def display_timetable(request):
    user = request.user
    if hasattr(user, 'teacher'):
        subject1_timetable_entries = TimetableEntry.objects.filter(subject=user.teacher.subject_taught1)
        subject2_timetable_entries = TimetableEntry.objects.filter(subject=user.teacher.subject_taught2)
        timetable_entries = subject1_timetable_entries.union(subject2_timetable_entries)
        
    elif hasattr(user, 'student'):
        timetable_entries = TimetableEntry.objects.filter(class_name=user.student.class_name)
    else:
        timetable_entries = TimetableEntry.objects.all()

    timetable_by_class = {}
    for entry in timetable_entries:
        if entry.class_name not in timetable_by_class:
            timetable_by_class[entry.class_name] = []
        timetable_by_class[entry.class_name].append(entry)

    context = {'timetable_by_class': timetable_by_class}
    return render(request, 'timetable/display_timetable.html', context)
