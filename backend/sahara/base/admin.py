from django.contrib import admin

from base.models import Course, Department, Faculty, School, Student, Units

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['firstname','email','department','course']


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display=['schoolName','faculty']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display=['facultyName']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['departmentName','school']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['courseName','department','yearOfStudy','numberOfStudents']



@admin.register(Units)
class UnitAdmin(admin.ModelAdmin):
    list_display=['unitName','unitCode']

