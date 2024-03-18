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

            # If subject is a string, fetch the Subject instance with that name
            if isinstance(subject, str):
                subject_instance = Subject.objects.get(name=subject)
            else:
                subject_instance = subject

            TimetableEntry.objects.create(
                class_name=selected_class,
                day=day,
                time=time_slot,
                subject=subject_instance,  # Use the Subject instance
                lab=lab
            )

    for teacher in Teacher.objects.all():
        teacher_class = random.choice(Class.objects.all())

        # Retrieve the subjects taught by the teacher
        subjects_taught = [teacher.subject_taught1, teacher.subject_taught2]

        for day in days_of_week:
            for time_slot in time_slots:
                # Randomly select one of the subjects taught by the teacher
                subject_name = random.choice(subjects_taught)
                if subject_name:
                    subject_instance = Subject.objects.get(name=subject_name)
                    TimetableEntry.objects.create(
                        class_name=teacher_class,
                        day=day,
                        time=time_slot,
                        subject=subject_instance
                    )
