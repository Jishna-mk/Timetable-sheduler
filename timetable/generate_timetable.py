import random
from timetable.models import Class, Subject, TimetableEntry, Lab
from teacher.models import Teacher

def generate_timetable(selected_class):
    time_slots = ['Period 1', 'Period 2', 'Period 3', 'Period 4', 'Period 5']
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    subjects = list(selected_class.subjects.all())
    labs = list(selected_class.labs.all())

    TimetableEntry.objects.filter(class_name=selected_class).delete()

    for day in days_of_week:
        for time_slot in time_slots:
           
            if random.choice([True, False]): 
                subject = random.choice(subjects)
                lab = None
            else:
                subject = None
                lab = random.choice(labs)
           
            TimetableEntry.objects.create(
                class_name=selected_class,
                day=day,
                time=time_slot,
                subject=subject,
                lab=lab
            )

    for teacher in Teacher.objects.all():
        teacher_class = random.choice(Class.objects.all())
   
    if teacher.subject_taught in teacher_class.subjects.all():
        for day in days_of_week:
            for time_slot in time_slots:
                TimetableEntry.objects.create(
                    class_name=teacher_class,
                    day=day,
                    time=time_slot,
                    subject=teacher.subject_taught
                )
