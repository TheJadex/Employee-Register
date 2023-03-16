from django.urls import path
from . import views

urlpatterns = [
    path('', views.defaultView, name="defaultView"),
    path('list/', views.employeeList, name="employeeList"), # Get request to retrieve and display of all records
    path('form/', views.employeeForm, name="employeeForm"), # Get and post request for insert operation
    path('<int:id>/', views.employeeForm, name="employeeUpdate"), # Get and post request for the form
    path('delete/<int:id>/', views.employeeDelete, name="employeeDelete"), # Delete an item in the list
]