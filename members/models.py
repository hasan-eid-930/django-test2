from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import validate_email

class Teacher(models.Model):
  name=models.CharField( max_length=50)

class Members(models.Model):
  firstname = models.CharField(max_length=245)
  lastname = models.CharField(max_length=255)
  age=models.IntegerField(default=30)
  teacher=models.ForeignKey(Teacher,default=7,on_delete=models.CASCADE)
  date=models.DateField(auto_now=False, auto_now_add=True )
  datetime=models.DateTimeField( auto_now=True, auto_now_add=False)

class Course(models.Model):
  name=models.CharField(primary_key=True,default='mgh', max_length=50)
  duration=models.DurationField(default=datetime.timedelta(days=5))

class Lecture(models.Model):
  name=models.CharField( max_length=50)
  course=models.ForeignKey(Course,verbose_name='c_id', on_delete=models.CASCADE)

class Book(models.Model):
  name=models.CharField( max_length=50)
  price=models.DecimalField(max_digits=5, decimal_places=2,default=55)
  b=models.BooleanField(default=True)
