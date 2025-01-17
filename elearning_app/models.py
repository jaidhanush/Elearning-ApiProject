from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_cost = models.DecimalField(max_digits=10, decimal_places=2)
    course_duration = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tutor(models.Model):
    tutor_name = models.CharField(max_length=100)
    course_specialization = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tutor')

    def __str__(self):
        return self.tutor_name