from pyexpat import model
from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline, site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from base.models import Course, Department, Faculty, Lecturer, School, Student, TimeTableEntity, Timetable, TimetableDay, Units

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['firstname','surname','course','department','regNumber','school','faculty']
    readonly_fields = ('regNumber','department','school','faculty',)


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
    list_display=['unitName','unitCode',]

class TimeTableDayAdmin(SuperInlineModelAdmin, TabularInline):
    model=TimeTableEntity
    extra=1


class TimetableInlineAdmin(SuperInlineModelAdmin, StackedInline):
    model=TimetableDay
    inlines=(TimeTableDayAdmin,)
    
    extra=1
    


@admin.register(Timetable)
class TimeTableAdmin(SuperModelAdmin):
    inlines=(TimetableInlineAdmin,)
    list_display=['course','year_of_study','department']


    def year_of_study(self,timetable):
        return timetable.course.yearOfStudy

    def department(self,timetable):
        return timetable.course.department



@admin.register(Lecturer)
class LectureAdmin(admin.ModelAdmin):
   
    list_display=['firstname','surname','department']