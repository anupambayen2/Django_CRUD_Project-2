from django import views
from django.shortcuts import redirect, render
from django.views import View
from .models import Student
from .forms import AddStudentForm

# Create your views here.

class Home(View):
    def get(self,request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html',{'stu_data':stu_data})

    
class Add_Student(View):
    def get(self,request):
        fm = AddStudentForm()
        return render(request,'core/add_student.html',{'form':fm})
    
    def post(self,request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core/add_student.html',{'form':fm})

class Delete_Student(View):
    def post(self,request):
        data = request.POST
        id = data.get('id')
        stud_data = Student.objects.get(id=id)
        stud_data.delete()
        return redirect('/')


class Edit_Student(View):
    def get(self, request, id):
        stu_data = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu_data)
        return render(request,'core/edit_student.html',{'form':fm})

    def post(self, request, id):
        stu_data = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=stu_data)
        if fm.is_valid:
            fm.save()
            return redirect('/')
        else:
            pass


