from django import forms
from AppAssignment.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['first_name', 'last_name','email', 'password', 'age']
