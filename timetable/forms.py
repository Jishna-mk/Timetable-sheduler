from django import forms
from .models import Class, Subject,Lab


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class  # Specify the model attribute
        fields = ['class_name', 'subjects', 'labs'] 

    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    labs = forms.ModelMultipleChoiceField(
        queryset=Lab.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
# class ClassForm(forms.ModelForm):
#     subjects = forms.ModelMultipleChoiceField(
#         queryset=Subject.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )
    
#     labs = forms.ModelMultipleChoiceField(
#         queryset=Lab.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )
# class ClassForm(forms.ModelForm):
#     subjects = forms.ModelMultipleChoiceField(
#         queryset=Subject.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )
    
#     labs = forms.ModelMultipleChoiceField(
#         queryset=Lab.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False  # Make labs field optional
#     )
#     class Meta:
#         model = Class
#         fields = ['class_name', 'subjects','labs']



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']


class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ['name']


class TimetableGenerateForm(forms.Form):
    confirm_generation = forms.BooleanField(
        label='I confirm that I want to generate the timetable',
        required=True,
    )
    selected_class = forms.ModelChoiceField(
        label='Select Class',
        queryset=Class.objects.all(),
        empty_label=None,
    )