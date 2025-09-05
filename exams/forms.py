from django import forms
from .models import Exam
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title','description','questions','duration_minutes','active']
        widgets = {'questions': forms.CheckboxSelectMultiple}
