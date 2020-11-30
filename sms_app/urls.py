
from django.urls import path
from .views import *


urlpatterns = [
    path('',home_page,name="home"),
    path('student/',student_page,name="student"),
    path('student/profile/<roll_no>/',student_profile,name="profile"),
    path('student/delete/<roll_no>/',delete_student,name="delete"),
]