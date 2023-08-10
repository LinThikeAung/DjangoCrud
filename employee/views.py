from django.shortcuts import render,redirect
from employee.models import EmpModel
from django.contrib import messages
from employee.forms import EmpForms

# Create your views here.

def showEmployee(request):
    lists = EmpModel.objects.all()
    return render(request,"index.html",{"lists": lists})

def insertEmployee(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('occupation') and request.POST.get('salary') and request.POST.get('gender'):
            employee = EmpModel()
            employee.name = request.POST.get('name')
            employee.email= request.POST.get('email')
            employee.occupation = request.POST.get('occupation')
            employee.salary = request.POST.get('salary')
            employee.gender = request.POST.get('gender')
            employee.save()
            messages.success(request, 'Employee '+ employee.name + ' is saved successfully.')
            return render(request, 'insert.html')
        else:
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

def editEmployee(request,id):
    editEmp = EmpModel.objects.get(id=id)
    return render(request,'edit.html',{'employee':editEmp})

def updateEmployee(request,id):
    updateEmp = EmpModel.objects.get(id=id)
    forms     = EmpForms(request.POST, instance=updateEmp)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Employee updated successfully.')
        return redirect('editEmployee',id)
    
def deleteEmployee(request,id):
    deleteEmp = EmpModel.objects.get(id=id)
    deleteEmp.delete()
    return redirect('showEmployee')
