from django.db import models

# Create your models here.

class Student(models.Model):
	name=models.CharField(max_length=15)
	fname=models.CharField(max_length=15)
	email=models.EmailField(max_length=15)
	password=models.CharField(max_length=15)
	gender=models.CharField(max_length=15)
	dob=models.CharField(max_length=15)
	mob=models.IntegerField()


class Faculty(models.Model):
	name=models.CharField(max_length=15)
	fname=models.CharField(max_length=15)
	email=models.EmailField(max_length=15)
	password=models.CharField(max_length=15)
	gender=models.CharField(max_length=15)
	dob=models.CharField(max_length=15)
	mob=models.IntegerField()

class Admin(models.Model):
	name=models.CharField(max_length=15)
	fname=models.CharField(max_length=15)
	email=models.EmailField(max_length=15)
	password=models.CharField(max_length=15)
	gender=models.CharField(max_length=15)
	dob=models.CharField(max_length=15)
	mob=models.IntegerField()
	
	

	def __str__(self):
		rec=str(self.id)+self.name+self.fname+self.email+self.password+self.gender+self.dob+str(self.mob)
		return rec
