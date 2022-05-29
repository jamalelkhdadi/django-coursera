from django.urls import path

from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    CourseUserListView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    path('course/', views.course, name='course'),
    path('course/new/', CourseCreateView.as_view(), name='course-create'),
    path('course/user/<str:username>', CourseUserListView.as_view(), name='user-courses'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),

    path('course/all', views.course_all, name='course-all'),
   
]
