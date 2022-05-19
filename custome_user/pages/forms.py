
from dataclasses import fields
from django import forms 
from accounts.models import StudentProfile
from accounts.models import Account
from accounts.models import EmployerProfile
from accounts.models import AppliedJobs
# from accounts.models import PostJob

class AccountForm(forms.ModelForm) :
    class Meta:
        model = Account
        fields = ['email','contact']
    


class StudentDetails(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'male'),
        ('Female', 'female'),
    
    ]
    NATIONALITY = [
        ('GH', 'Ghanaian'),
        # ('h', 'female'), 
    ]   
    
    nationality = forms.CharField(
        max_length=250,
        widget=forms.Select(choices=NATIONALITY),
    )
    
    gender = forms.CharField(
        max_length=6,
        widget=forms.Select(choices=GENDER_CHOICES),
    )
    
    date_of_birth = forms.DateField(required=False , widget=forms.DateInput)
    
    class Meta:
        model = StudentProfile
        exclude = ['user']
  
class ApplyJobForm(forms.ModelForm) :
    CERTIFICATE= [
        ('Phd', 'Phd'),
        ('diploma', 'diploma'),    
        ('degreee', 'degreee'),         
    ]      
    
    certificate = forms.CharField(
        max_length=250,
        widget=forms.Select(choices=CERTIFICATE),
    )
    
    class Meta:
        model = AppliedJobs
        fields =['certificate','experience']
        
        
        
class EmployerDetails(forms.ModelForm):
             
    class Meta:
        model = EmployerProfile
        # fields ='__all__'
        exclude = ['user']
        

# class PostJobForm(forms.ModelForm) :
#     class Meta:
#         model = PostJob
#         fields ='__all__'
#         # exclude = ['company']       
        