
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
 
from accounts.models import Account

class UserRegistration(UserCreationForm):
    email = forms.EmailField(max_length=70, help_text="Required. Add a valid email address.")
    contact = forms.CharField(max_length=15)
    usertype = forms.CharField()
    class Meta:
        model = Account 
        fields = ('email' , 'contact', 'password1','password2' , 'usertype')
        
        
        
               
    # creating funtion for form validation
    # django will no to use this function if the form is submitted
    # do this for model fields which have unique
    def clean_email(self):
        email  = self.cleaned_data['email'].lower()
        # so now checking if account exit then they cant use it
        try:
            # use get for single row just like primary key
            # use filter for multiple row, it returns a queryset
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use.')
         
        
class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput , label="password")
    
    class Meta :
        model = Account
        fields = ('email' , 'password')     
         
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']        
            password = self.cleaned_data['password']       
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")
             
    # def save(self,request):
    #     email = self.cleaned_data['email']       
    #     password = self.cleaned_data['password']      
    #     user = authenticate(email=email , password=password) 
    #     if user :
    #         login(request , user);