
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.showEmployee, name="showEmployee"),
    path('insert', views.insertEmployee, name="insertEmployee"),
    path('edit/<int:id>', views.editEmployee, name="editEmployee"),
    path('update/<int:id>', views.updateEmployee, name="updateEmployee"),
    path('delete/<int:id>', views.deleteEmployee, name="deleteEmployee"),
]