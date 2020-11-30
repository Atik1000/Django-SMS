from django.db import models

class Student(models.Model):
    GENDER_CHOICE=(
        ('male','Male'),
        ('female','Female')
    )
    name=models.CharField(max_length=120)
    father=models.CharField(max_length=120)
    mother=models.CharField(max_length=120)
    photo=models.ImageField(upload_to='student_photo/')
    roll=models.IntegerField(unique=True)
    reg=models.IntegerField(unique=True)
    gender=models.CharField(choices=GENDER_CHOICE,max_length=6)
    dob=models.DateField()
    date_time=models.DateTimeField(auto_now_add=True)
    is_delete=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.roll)