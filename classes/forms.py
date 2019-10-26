from django import forms
from .models import Classroom, Student
from django.contrib.auth.models import User


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        exclude = ["teacher"]
        # fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        exclude = ["classroom"]

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())