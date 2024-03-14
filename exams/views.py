from django.shortcuts import render

from exams.forms import StudentForm, StudentComplains



# Create your views here.
def home(request):
    return render(request, 'home.html')
def teacher(request):
    form = StudentComplains()
    return render(request, 'teacher.html', {'form': form})
def student(request):
    form = StudentForm()
    return render(request, 'student.html', {'form': form})

