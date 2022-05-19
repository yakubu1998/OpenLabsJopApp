from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponse
 
from accounts.models import EmployerProfile, PostJob , Account , AppliedJobs
from accounts.forms import UserRegistration
from accounts.forms import UserLogin
from .forms import StudentDetails , AccountForm, EmployerDetails, ApplyJobForm

# views for posting new job , listing the posted jobs, Details of the posted Jobs
#updating the job and also Deleting the job.
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)    


# Create your views here.
# regiter new user view
def registerUser (request, *args, **kwargs):
    
    current_User = request.user
    if current_User.is_authenticated:
        return HttpResponse(f'You are already authenticated as {current_User}')
    context = {}
     
    # now log for submitting form and others
    if request.POST:
        # create a new for object for new form detail coming in
        form_submitted = UserRegistration(request.POST)
        # now checking if that form is valid
        if form_submitted.is_valid(): 
            # # saving the form will execute all the form validations including those in forms.py
            # that is clean_email() 
            form_submitted.save()
            
            # now login user when save 
            email = form_submitted.cleaned_data.get('email').lower()
            raw_password = form_submitted.cleaned_data.get('password1')
            account = authenticate(email=email , password=raw_password)
            login(request , account)
            
            if request.user.usertype == "Student" :
                return redirect("editStudentProfile")
            elif request.user.usertype == "Alumni" :
                return redirect("editStudentProfile")
            elif request.user.usertype == "Admin" :
                return redirect("editEmployerProfile")
            else :
                return redirect("editEmployerProfile")
            
         
        else :
            # so if the form is not valid, it will return the form back to the template
            # bundle with the error messages
            context['UserRegistration_error'] = form_submitted

              
            
            
    
    # now log for submitting form and others
    
    
    return render(request , 'pages/register.html' , context)
  




def home(request):
    
    return render(request , 'pages/index.html')


# def feedback(request):
    
#     return render(request , 'pages/feedback.html')



def loginUser(request , *args, **kwargs):
    
    context = {}
    if request.POST : 
        login_submitted = UserLogin(request.POST)
        if login_submitted.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email , password=password)
            if user:
                login(request , user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('home')
                
        else:
            context['userLoginErrors']  =   login_submitted
                # return redirect('home')
            
    
    return render(request , 'pages/login.html', context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
           redirect = str(request.GET.get("next"))
    return redirect        



def logoutUser(request) :
    logout(request)  
      
    return redirect('home')


class StudentProfile(DetailView) :   
    model = Account
    template_name = 'pages/studentProfile.html'


def editStudentProfile(request , *args, **kwargs):
    
    if request.method == 'POST':        
        updateUser = AccountForm( request.POST ,instance=request.user)
        updateform = StudentDetails(request.POST , request.FILES , instance=request.user.studentprofile)

        if updateUser.is_valid() and updateform.is_valid() :
            updateUser.save()
            updateform.save()
            messages.success(request, f'Your account has been updated successfully')
            return redirect('studentProfile')
            
    else :
        updateUser = AccountForm(instance=request.user)
        updateform = StudentDetails(instance=request.user.studentprofile)
            
        
    context = {
        'updateform': updateform ,
        'updateUser': updateUser,
    } 
      
        
    
    
    
    return render(request , 'pages/editStudentProfile.html', context)   



class PostJobView (LoginRequiredMixin, CreateView):
    
    model = PostJob
    fields = ['job_title','location','allowance','job_description','requirement','category']
    template_name = 'pages/postjob_form.html'
    
    def form_valid(self , form) :
        form.instance.company = self.request.user
        return super().form_valid(form)
    
    # django will pass a form in context to the view template  
    

class jobsIntenships(ListView):    
    model = PostJob
    template_name = 'pages/jobs_intenships.html'
    context_object_name = 'posts'
    ordering = ['-id']
    paginate_by = 5

    # django will pass a context Called object to the view template  
    # but we use context_object_name to change it to posts




def registerEmp(request):    
    current_User = request.user
    if current_User.is_authenticated:
        return HttpResponse(f'You are already authenticated as {current_User}')
    context = {}
    
    # now log for submitting form and others
    if request.POST:
        # create a new for object for new form detail coming in
        form_submitted = UserRegistration(request.POST)
        # now checking if that form is valid
        if form_submitted.is_valid():
            # # saving the form will execute all the form validations including those in forms.py
            # that is clean_email() 
            form_submitted.save()
            
            # now login user when save 
            email = form_submitted.cleaned_data.get('email').lower()
            raw_password = form_submitted.cleaned_data.get('password1')
            account = authenticate(email=email , password=raw_password)
            login(request , account)
             
            return redirect("home")
        
        else :
            # so if the form is not valid, it will return the form back to the template
            # bundle with the error messages
            context['UserRegistration_error'] = form_submitted

              
            
            
    
    
    
    
    
    
    
    return render(request , 'pages/registerEmp.html' , context)


class EmployerProfile(DetailView) :
    model = Account
    template_name = 'pages/employerProfile.html'
    
    



def editEmployerProfile(request) :
    
    if request.method == 'POST':        
        updateUser = AccountForm( request.POST ,instance=request.user)
        updateform = EmployerDetails(request.POST , request.FILES , instance=request.user.employerprofile)

        if updateUser.is_valid() and updateform.is_valid() :
            updateUser.save()
            updateform.save()
            messages.success(request, f'Your account has been updated successfully')
            return redirect('employerProfile',request.user.id)
            
    else :
        updateUser = AccountForm(instance=request.user)
        updateform = EmployerDetails(instance=request.user.employerprofile)

            
        
    context = {
        'updateform': updateform ,
        'updateUser': updateUser,
    } 
      
    
    return render(request , 'pages/editEmployerProfile.html' , context)



class PostListView(ListView):
    model = PostJob
    template_name = 'pages/index.html'
    context_object_name = 'posts'
    ordering = ['-id']
    # paginate_by = 5
    
    
def EmployerIntenshipListView(request, pk):
    currentUser = Account.objects.filter(id=pk).first
    posts = PostJob.objects.filter(company=pk)
    
    context = {
        'posts':posts,
        'user':currentUser
    }
    
    return render(request , 'pages/employerProfileIntenship.html', context)
    
def EmployerPostListView(request, pk):
    currentUser = Account.objects.filter(id=pk).first
    posts = PostJob.objects.filter(company=pk)
    
    context = {
        'posts':posts,
        'user':currentUser
    }
    
    return render(request , 'pages/employerProfileJobs.html', context)
    
    
    
    
def PostDetailView(request , pk) :    

    post_detail = PostJob.objects.get(id=pk)
    # context = { 
    #    'object' : post_detail
    # }
        
    if request.method == 'POST' :
        applyForm = ApplyJobForm(request.POST)
        
        if applyForm.is_valid():
            AppliedJobs = applyForm.save(commit=False)
            AppliedJobs.posted_job = post_detail
            AppliedJobs.user = request.user
            AppliedJobs.save()
            
            redirect('jobsIntenships')
    else : 
        applyForm = ApplyJobForm()    
        
    context = {
       'object' : post_detail,
       'applyForm' :applyForm
    }        
        
        
        
        
    return render(request , 'pages/postDetail.html', context)  



      
        

class PostUpdateView (LoginRequiredMixin,UserPassesTestMixin , UpdateView):
    
    model = PostJob
    fields = ['job_title','location','allowance','job_description','requirement','category']
    template_name = 'pages/postjob_form.html'
    
    def form_valid(self , form) :
        form.instance.company = self.request.user
        return super().form_valid(form)

    def test_func(self) :
        post = self.get_object()
        if self.request.user == post.company :
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostJob
    template_name = 'pages/postDelete.html'
    success_url = '/employerProfile/uploaded-jobs/'
    
    
    def test_func(self) :
        post = self.get_object()
        if self.request.user == post.company :
            return True
        return False
    
    