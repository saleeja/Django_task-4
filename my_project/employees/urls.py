from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.department_list, name='department-list'),
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('list_func/<int:pk>/', views.employee_detail, name='employee-detail'),
    path('list_class/<pk>/', views.EmployeeDetailView.as_view()),
]

