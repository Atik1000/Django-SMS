from django.shortcuts import render,redirect
from .models import Student


def home_page(request): 
    return render(request, 'home.html')


def student_page(request):
  student= Student.objects.filter(is_delete=False)
  context={
      'std':student
  }
  return render(request, 'student.html',context)


def student_profile(request,roll_no):
    student=Student.objects.get(roll=roll_no)
    context={
        'std':student
    }
    return render(request, 'profile.html',context)


def delete_student(request,roll_no):
    student=Student.objects.get(roll=roll_no)
    student.is_delete=True
    student.save()
    # student.delete()
    return redirect('student')
    