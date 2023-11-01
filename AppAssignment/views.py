from django.shortcuts import render
from AppAssignment.forms import EmployeeForm
from AppAssignment.models import Employee
def image(request):
    return render(request,'image.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def gallery(request):
    return render(request,'gallery.html')


def join(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'join.html')
    else:
        return render(request, 'join.html')


def details(request):
    members = Employee.objects.all()
    return render(request, 'details.html', {'all': members})
# Create your views here.
