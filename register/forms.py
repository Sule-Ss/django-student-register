from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__' 
        labels = {"full_name": "Adınız", "phone_number":"Mobile", "mail":"Email","gender":"Gender", "student_number":"Student Number","path":"Path"}