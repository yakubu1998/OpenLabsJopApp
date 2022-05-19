from django.shortcuts import render
# django in build views 
# am using it to add carreer development links
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)   

from accounts.models import CareerDev


# custome views for admin dashboard
from accounts.models import StudentProfile
from accounts.models import EmployerProfile
from accounts.models import PostJob
from accounts.models import AppliedJobs

# Create your views here.
def dashboard(request): 
    
    return render(request , 'admin_dashboard/dashboard.html')

# list of student 
def studentList(request):
    list_of_students = StudentProfile.objects.all()
    
    context = {
        'list_of_students':list_of_students
    }
    
    return render(request , 'admin_dashboard/studentList.html', context)


# list of Alumins 
def aluminList(request):
    list_of_alumnis = StudentProfile.objects.all()
    
    context = {
        'list_of_alumnis':list_of_alumnis
    }
    
    return render(request , 'admin_dashboard/aluminList.html',context)



# list of Employer 
def employerList(request):
    list_of_employers = EmployerProfile.objects.all()
    
    context = {
        'list_of_employers':list_of_employers
    }
    
    return render(request , 'admin_dashboard/employerList.html' , context)



# list of Jobs Uploaded 
def jobUploaded(request):
    
    list_of_jobs_uploaded = PostJob.objects.all()
    
    context = {
        'list_of_jobs_uploaded':list_of_jobs_uploaded
    }
    
    return render(request , 'admin_dashboard/jobUploaded.html', context)


# list of Jobs Applied 
def jobApplied(request):
    list_of_jobs_applied = AppliedJobs.objects.all()
    
    context = {
        'list_of_jobs_applied':list_of_jobs_applied
    }
    
    return render(request , 'admin_dashboard/jobApplied.html', context)



# list of Uploaded Intenships 
def uploadedIntenships(request):
    list_of_internships_uploaded = PostJob.objects.all()
    
    context = {
        'list_of_internships_uploaded':list_of_internships_uploaded
    }
    
    return render(request , 'admin_dashboard/uploadedIntenships.html' , context)


#Add Career development using django in build class views CreateView
class AddCareerDev(CreateView) :
    model = CareerDev
    fields = ['career_link','Career_description']
    template_name = 'admin_dashboard/addCareer.html '
    
    
#Add Career development using django in build class views ListVi ew 
# To list all added career Development from the CareerDev Model  (database table)
class ListOfCareerDev(ListView) :
    model = CareerDev
    template_name = 'admin_dashboard/careerList.html'
    context_object_name = 'careerPosts'
    ordering = ['-id']
    paginate_by = 5

    # django will pass a context Called object to the view template  
    # but we use context_object_name to change it to careerPosts    
    