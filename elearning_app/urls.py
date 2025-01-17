from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, StudentViewSet, TutorViewSet,all_course,all_students,all_tutor

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('students', StudentViewSet)
router.register('tutors', TutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('course/', all_course, name='all_course'),
    # path('student/', all_students, name='all_students'),
    # path('tutor/', all_tutor, name='all_tutor'),
]
