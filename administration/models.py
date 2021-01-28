import datetime as dt
from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=50)
    hod = models.OneToOneField('Teacher', on_delete=models.SET_NULL, related_name='hod_of', null=True, blank=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    class Semester(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4
        FIFTH = 5
        SIXTH = 6
        SEVENTH = 7
        EIGHTH = 8

    semester = models.IntegerField(choices=Semester.choices)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.branch} - {self.semester} semester"

class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    admission_date = models.DateField()
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.fname} {self.lname} [{self.section}]"


class Teacher(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30)
    qualification = models.CharField(max_length=100)
    joining_date = models.DateField()
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.fname} {self.lname} [{self.branch}]"