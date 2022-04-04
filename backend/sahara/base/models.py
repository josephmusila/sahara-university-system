from django.db import models

# Create your models here.



class Faculty(models.Model):
    
    facultyName=models.CharField(max_length=200,null=False,default="aaaa")
    
    def __str__(self):
        return f'{self.facultyName}'


class School(models.Model):
    schoolName=models.CharField(max_length=200,null=False,default="aaaa")
    faculty=models.ForeignKey(Faculty,on_delete=models.DO_NOTHING,blank=True)


    def __str__(self):
        return f'{self.schoolName}'

   

class Department(models.Model):
   
    departmentName=models.CharField(max_length=200,null=False,default="aaa")
    school=models.ForeignKey(School,on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'{self.departmentName}'



class Course(models.Model):
    
    courseName=models.CharField(max_length=200)
    department=models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    yearOfStudy=models.IntegerField()
    numberOfStudents=models.IntegerField()


    def __str__(self):
        return f'{self.courseName}'


class Units(models.Model):
    course=models.ManyToManyField(Course)
    unitName=models.CharField(max_length=200)
    unitCode=models.CharField(max_length=8)


class Lecturer(models.Model):
    firstname=models.CharField(max_length=50)
    othername=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    idnumber=models.IntegerField(unique=True)
    dateOfBirth=models.DateTimeField()
    department=models.ManyToManyField(Department)



class Student(models.Model):

    MALE="M"
    FEMALE="F"
    OTHER="O"
    GENDER_CHOICES=[
        (MALE,"Male"),
        (FEMALE,"Female"),
        (OTHER,"Other")
    ]

    






    firstname = models.CharField(max_length=50)
    othername = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    idnumber = models.IntegerField(unique=True)
    dateOfBirth = models.DateTimeField()

    email = models.EmailField(unique=True)
    residence = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default=OTHER)
    avatar=models.CharField(max_length=200)
    faculty=models.ForeignKey(Faculty,on_delete=models.DO_NOTHING)
    school=models.ForeignKey(School,on_delete=models.DO_NOTHING)
    department=models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)

 
class Fees(models.Model):
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    student=models.ForeignKey(Student,on_delete=models.DO_NOTHING)

