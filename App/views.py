from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def defaultView(request):
    return render(request, "layout.html")


def employeeList(request):
    # This function deal with the list of employees

    context = {"employeelist":Employee.objects.all()}
    return render(request, "employeeList.html", context)

def employeeForm(request, id=0):
    # This function deals with get and post for insert and update operations

    if  request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form =EmployeeForm(instance=employee)
        return render(request, "employeeForm.html", {'form':form})
    else:
        if id == 0: # An insert operation
            form = EmployeeForm(request.POST)
        else: # Otherwise an update operation
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect(employeeList)

def employeeDelete(request):
    # This function deals with the deletion of an employee record 
    return