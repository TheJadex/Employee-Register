from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        # fields =  ('fullName','mobileNum', 'emp_code', 'position')
        fields = "__all__"
        labels = {
            # Used to edit the models
            'fullName':'Full Name',
            'mobileNum':'Phone Number',
            'emp_code':'Employee Code(ID)',
        }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False