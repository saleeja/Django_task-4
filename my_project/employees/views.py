from django.shortcuts import render
from .models import Department, Employee
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView


#  Create list view using function based view to show list of items from the first model
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

# Create list view using class based view to show list of items from the second model

class EmployeeListView(ListView):
     model = Employee
     template_name = 'employee_list.html'
     context_object_name = 'employees'

# Create detail view using function based view to show detail view of an item
def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

# Create detail view using class based view to show detail view of an item
class EmployeeDetailView(DetailView):
     model = Employee
     template_name = 'employee_detail.html'
     context_object_name = 'employee'
