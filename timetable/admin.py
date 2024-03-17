from django.contrib import admin
from .models import Class, Subject, TimetableEntry,Lab

# Register your models here.


admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Lab)
admin.site.register(TimetableEntry)