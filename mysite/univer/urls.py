from . import views
from django.urls import path


urlpatterns = [
    path('university/', views.UniversityView.as_view()),
    path('university/<int:pk>/', views.UniversityView.as_view()),
    path('faculties/', views.FacultiesView.as_view()),
    path('faculties/<int:pk>/', views.FacultiesView.as_view()),
    path('students/', views.StudentsView.as_view()),
    path('students/<int:pk>/', views.StudentsView.as_view())
]