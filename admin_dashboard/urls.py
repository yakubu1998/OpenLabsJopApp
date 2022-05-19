from django.urls import path, include
from . import views

# because AddCareerDev view is a class base view can't import it like functional views
# but rather import it as
from .views import (
    AddCareerDev,
    ListOfCareerDev,
)     
urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('studentList/' , views.studentList , name='studentList'),
    path('aluminList/' , views.aluminList , name='aluminList'),
    path('employerList/' , views.employerList , name='employerList'),
    path('jobUploaded/' , views.jobUploaded , name='jobUploaded'),
    path('jobApplied/' , views.jobApplied , name='jobApplied'),
    path('uploadedIntenships/' , views.uploadedIntenships , name='uploadedIntenships'),
    path('addCareer/' , AddCareerDev.as_view() , name='addCareer'),
    path('careerList/' , ListOfCareerDev.as_view() , name='listCareer'),
    
    
]