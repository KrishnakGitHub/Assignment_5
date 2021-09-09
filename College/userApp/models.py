from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# # Create your models here.
class MyUser(User):
	is_student = models.BooleanField(default=False)
	is_lecturer = models.BooleanField(default=False)
	is_employee = models.BooleanField(default=False)

class Department(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Student(models.Model):
	user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
	department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name="student_department")

	def __str__(self):
		return self.user.first_name 

class Leacturare(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department,related_name='lecturer_department')

    def __str__(self):
        return str(self.user)

class Employee(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    Employee_Type = models.CharField(max_length=100, choices=(("Pune", "Pune"), ("Sweeper", "Sweeper")))

    def __str__(self):
        return self.user.username