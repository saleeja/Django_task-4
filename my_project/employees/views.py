from django.shortcuts import render
from django.views.generic import ListView
from .models import Department, Employee
from django.shortcuts import render, get_object_or_404
from django.views import View

#  Create list view using function based view to show list of items from the first model
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

# Create list view using class based view to show list of items from the second model

class EmployeeListView(View):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        context = {'employees': employees}
        return render(request, 'employee_list.html', context)

# Create detail view using function based view to show detail view of an item
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

# Create detail view using class based view to show detail view of an item
class EmployeeDetailView(View):
    def get(self, request, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=kwargs['pk'])
        return render(request, 'employee_detail.html', {'employee': employee})