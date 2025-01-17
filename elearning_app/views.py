from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Course, Student, Tutor
from .serializers import CourseSerializer, StudentSerializer, TutorSerializer


# def all_course(request):
#     course = Course.objects.all()
#     return render(request, 'elearning_app/all_course.html', {'course': course})

# def all_students(request):
#     student = Student.objects.all()
#     return render(request, 'elearning_app/all_students.html', {'student': student})

# def all_tutor(request):
#     tutor = Tutor.objects.all()
#     return render(request, 'elearning_app/all_tutor.html', {'tutor': tutor})


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    
