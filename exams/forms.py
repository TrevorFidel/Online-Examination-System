from django import forms
from exams.models import Contact

class StudentForm(forms.Form):
    name = forms.CharField(label='Enter your name', max_length=50, required=True)
    age = forms.IntegerField(min_value=18, label='Enter your age', required=True)
    check = forms.BooleanField(label='Do you want to join', required=False)
    category = forms.ChoiceField(choices=[('Student', 'Student'), ('Parent', 'Parent'), ('Teacher', 'Teacher')])

class StudentComplains(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']