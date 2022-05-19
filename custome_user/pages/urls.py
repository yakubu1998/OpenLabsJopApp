from django.urls import path, include

from django.contrib.auth import views as auth_views
# importing the class base views from pages views.py
from .views import (
    jobsIntenships,
    PostJobView,
    PostDetailView, 
    PostListView,
    PostUpdateView , 
    PostDeleteView,
    StudentProfile,
    EmployerProfile,
)    

# importing the functinal base views from pages views.py
from . import views

urlpatterns = [
    # path('', views.home , name='home'),
    path('register/' , views.registerUser , name='registerUser' ), 
    path('' , PostListView.as_view() , name='home'),  
    # path('feedback/' , views.feedback , name='home'), 
    path('login/' , views.loginUser , name='loginUser'),
    path('logout/' , views.logoutUser , name='logoutUser'),
    path('jobs_intenships/' , jobsIntenships.as_view() , name='jobsIntenships'),
    
    path('studentProfile/about/<int:pk>' , StudentProfile.as_view() , name='studentProfile'),
    path('editStudentProfile/' , views.editStudentProfile , name='editStudentProfile'),
    
    path('registerEmp/' , views.registerEmp , name='registerEmp'),
    path('employerProfile/about-us/<int:pk>' , EmployerProfile.as_view() , name='employerProfile'),
    path('employerProfile/uploaded-jobs/<int:pk>' ,views.EmployerPostListView , name='employerProfileJobs'),
    path('employerProfile/uploaded-intenships/<int:pk>' ,views.EmployerIntenshipListView , name='employerProfileIntenships'),
    path('editEmployerProfile/' , views.editEmployerProfile , name='editEmployerProfile'),
    
    path('postJob/new/' , PostJobView.as_view() , name='postNewJob'),
    # path('postJob/<int:pk>/' , PostDetailView.as_view() , name='postDetail'),
    path('postJob/<int:pk>/' , views.PostDetailView , name='postDetail'),
    path('postJob/<int:pk>/update' , PostUpdateView.as_view() , name='postJobUpdate'),
    path('postJob/<int:pk>/delete' , PostDeleteView.as_view() , name='postJobDelete'),
    
    # Password reset view
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='pages/password_reset.html') , name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='pages/password_reset_done.html') , name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='pages/password_reset_confirm.html') , name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='pages/password_reset_complete.html') , name='password_reset_complete'),
    
    
]