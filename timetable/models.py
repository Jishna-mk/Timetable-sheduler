from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Lab(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    class_name = models.CharField(max_length=10)
    subjects = models.ManyToManyField(Subject)
    labs = models.ManyToManyField(Lab)

    def __str__(self):
        return self.class_name
    

class TimetableEntry(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)  
    time = models.CharField(max_length=20) 
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.subject:
            subject_str = self.subject
        else:
            subject_str = "No Subject"
        
        if self.lab:
            lab_str = self.lab
        else:
            lab_str = "No Lab"
    
        return f'{self.class_name} - {self.day} - {self.time} - {self.subject} - {self.lab}'

