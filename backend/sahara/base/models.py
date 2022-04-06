from calendar import TUESDAY, WEDNESDAY
from sqlite3 import Date
from django.db import models
from django.utils.text import slugify 
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Faculty(models.Model):
    
    facultyName=models.CharField(max_length=200,null=False)
    
    def __str__(self):
        return f'{self.facultyName}'

class School(models.Model):
    schoolName=models.CharField(max_length=200,null=False)
    faculty=models.ForeignKey(Faculty,on_delete=models.DO_NOTHING,blank=True)


    def __str__(self):
        return f'{self.schoolName}'

class Department(models.Model):
   
    departmentName=models.CharField(max_length=200,null=False)
    school=models.ForeignKey(School,on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'{self.departmentName}'

class Course(models.Model):
    
    courseName=models.CharField(max_length=200)
    department=models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    yearOfStudy=models.IntegerField()
    numberOfStudents=models.IntegerField()
    courseCode=models.CharField(max_length=5)

    def __str__(self):
        return f'{self.courseName}'

class Units(models.Model):
    
    unitName=models.CharField(max_length=200)
    unitCode=models.CharField(max_length=8)

    def __str__(self):
        return f'{self.unitName}'


class Lecturer(models.Model):
    firstname=models.CharField(max_length=50)
    othername=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    idnumber=models.IntegerField(unique=True)
    dateOfBirth=models.DateTimeField()
    department=models.ForeignKey(Department,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.firstname}'


class Student(models.Model):

    MALE="M"
    FEMALE="F"
    OTHER="O"
    GENDER_CHOICES=[
        (MALE,"Male"),
        (FEMALE,"Female"),
        (OTHER,"Other")
    ]
    id = models.AutoField(primary_key=True)
    # registrationNumber=models.CharField(max_length=10)
    firstname = models.CharField(max_length=50)
    othername = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    idnumber = models.IntegerField(unique=True)
    dateOfBirth = models.DateField()

    email = models.EmailField(unique=True)
    residence = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default=OTHER)
    avatar=models.CharField(max_length=200)
    faculty=models.ForeignKey(Faculty,on_delete=models.DO_NOTHING)
    school=models.ForeignKey(School,on_delete=models.DO_NOTHING)
    department=models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    regNumber = models.SlugField(blank=True,null=True,unique=True)
 
    def save(self, *args, **kwargs):
        # if self.department.departmentName == "IT":
        # self.regNumber = f'{self.course.courseCode}/{self.id}/{date.today().year}'
        self.department=self.course.department
        self.school=self.course.department.school
        self.faculty=self.course.department.school.faculty
        super().save(*args, **kwargs)

       
def student_post_save(sender,instance,created, *args,**kwargs):
    
     instance.regNumber = f'{instance.course.courseCode}/{"0"* (5-(len(str(instance.id))))}{instance.id}/{date.today().year}'
     if created:
       
        instance.save()

post_save.connect(student_post_save,sender=Student)

 
class Fees(models.Model):
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    student=models.ForeignKey(Student,on_delete=models.DO_NOTHING)

class Timetable(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)


class TimetableDay(models.Model):
    MONDAY="MONDAY"
    TUESDAY="TUESDAY"
    WEDNESDAY="WEDNESDAY"
    THURSDAY="THURSDAY"
    FRIDAY="FRIDAY"
    WEEKDAY_CHOICE=[
        (MONDAY,"MONDAY"),
        (TUESDAY,"TUESDAY"),
        (WEDNESDAY,"WEDNESDAY"),
        (THURSDAY,"THURSDAY"),
        (FRIDAY,"FRIDAY"),
    ]
    day=models.CharField(max_length=10,choices=WEEKDAY_CHOICE,blank=False)
    base=models.ForeignKey(Timetable,on_delete=models.DO_NOTHING)
    

class TimeTableEntity(models.Model):



    TIMESLOT_1="7:00-9:00"
    TIMESLOT_2="9:00-11:00"
    TIMESLOT_3="11:00-1:00"
    TIMESLOT_4="1:00-2:00"
    TIMESLOT_5="2:00-4:00"
    TIMESLOT_6="4:00-6:00"
    TIMESLOT_CHOICE=[
        (TIMESLOT_1,"7:00-9:00"),
        (TIMESLOT_2,"9:00-11:00"),
        (TIMESLOT_3,"11:00-1:00"),
        (TIMESLOT_4,"1:00-2:00"),
        (TIMESLOT_5,"2:00-4:00"),
        (TIMESLOT_6,"4:00-6:00"),
    ]
    entity=models.ForeignKey(Timetable,on_delete=models.DO_NOTHING)
    
   
    unit=models.ForeignKey(Units,on_delete=models.DO_NOTHING)
    lecturer=models.ForeignKey(Lecturer,on_delete=models.DO_NOTHING)
    time=models.CharField(max_length=20,choices=TIMESLOT_CHOICE)
    room=models.CharField(max_length=10)
    entity=models.ForeignKey(TimetableDay,on_delete=models.DO_NOTHING)

