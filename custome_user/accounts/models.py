# import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.urls import reverse
# Create your models here.

# create user
# create superuser
# For managing the Account(user registration model) table
class MyAccountManager(BaseUserManager):
    
    def create_user(self,email,contact,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        # if not username:
        #     raise ValueError("Users must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            # username = username,
            contact = contact,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # in password u can use set_password to save password or password=password
    
    def create_superuser(self,email,contact,password):
         user = self.create_user(
             email = self.normalize_email(email),
            #  username = username,
             password = password,
             contact = contact,
             
         )
         
         user.is_admin = True
         user.is_superuser = True
         user.is_staff = True
         user.save(using=self._db)
         return user
         


# Before profile image is uploaded making sure to rename it,
# by creating a folder with the registered user id in profile_image folder
# then rename as profile_image.png
def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}' 

# default image to upload if user does'nt upload profile image
def get_default_profile_image():
    return "p/p.png" 


# Instead of using django in build User model, we rather customize.
# because we wanted to use email for registring of Users rather than using django username
# user registration database model (Table)
class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',unique=True,max_length=70)
    contact = models.CharField(max_length=15 , null=True , blank=True)
    usertype = models.CharField(max_length=30 )
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    # profile_image = models.ImageField(default=get_default_profile_image , max_length=100, upload_to=get_profile_image_filepath, null=True , blank=True)
 
    # taying the account model to user the custom manager
    objects = MyAccountManager()
 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact']
    
    def __str__(self):
        return self.email
    
    # to get the name of the profile image user uploaded,to make sure it is
    # renamed profile_image
    # def get_profile_image_filename(self):
    #     return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
        
    
    # if user has permission to do some admin things if their are admin then yes
    def has_perm(self,perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    
    
    
# The Student Profile(Alumni Profile) database model (Table)
class StudentProfile(models.Model):
    GENDER_CHOICES = [
    ('Male', 'male'),
    ('Female', 'female'),    
    ]
    
    NATIONALITY = [
        ('GH', 'Ghanaian'),
        # ('', 'female'), 
    ]
    
    CENTER = [
        ('OpenLabs Tamale', 'OpenLabs Tamale'),
        ('OpenLabs Kumasi', 'OpenLabs Kumasi'),
        ('OpenLabs Accra', 'OpenLabs Accra'),
        # ('', 'female'), 
    ]
    
    REGION = [
        ('north', 'Northen Region'),
        ('ashanti', 'Ashanti Region'),
        ('accra', 'Greater Accra'),
        # ('', 'female'), 
    ]
    
    
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250 , default='None')
    last_name = models.CharField(max_length=250, default='None')
    # email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=250 ,choices=NATIONALITY, default=None, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='None')
    current_region = models.CharField(max_length=250, choices=REGION , null=True, blank=True , default='None')
    location = models.CharField(max_length=250, choices=NATIONALITY , null=True, blank=True , default='Ghanaian')
    center = models.CharField(max_length=250, choices=CENTER , default='None')
    profile_image = models.ImageField(default=get_default_profile_image , max_length=100, upload_to=get_profile_image_filepath, null=True , blank=True)
    cv = models.FileField(max_length=100, upload_to='cv', default='text.txt')
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
     
    
    
    
    # */to get the name of the profile image user uploaded,to make sure it is
    # renamed profile_image */    
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
      



# The Employer Profile(Company Profile) database model (Table)
class EmployerProfile(models.Model):   
    INDUSTRY_CHOICES = [
        ('IT & Telecoms', 'IT & Telecoms'),
        ('Automative & Aviation', 'Automative & Aviation'),    
        ('Real Estate', 'Real Estate'),    
    ]
    
    COUNTRY = [
        ('Ghana', 'Ghana'),
        # ('Ni', 'Ni'),    
        # ('Real Estate', 'Real Estate'), 
    ]
    
    REGION = [
        ('Northern Region', 'Northern Region'),
        ('Greater Accra', 'Greater Accra'),    
        ('Ashanti Region', 'Ashanti Region'), 
    ]
    
    user = models.OneToOneField(Account, on_delete=models.CASCADE) 
    company_name = models.CharField(max_length=250 , default='None')
    industry = models.CharField(max_length=200, choices=INDUSTRY_CHOICES , null=True, blank=True , default='Choose')
    country = models.CharField(max_length=200, choices=COUNTRY , null=True, blank=True , default='Ghana')
    region  = models.CharField(max_length=200, choices=REGION , null=True, blank=True , default='Choose')
    address  = models.TextField(max_length=300, null=True, blank=True , default='Choose')    
    website =  models.CharField(max_length=550, null=True, blank=True)
    profile_image = models.ImageField(default=get_default_profile_image , max_length=100, upload_to=get_profile_image_filepath, null=True , blank=True)
          
    def __str__(self):
        return self.company_name
    
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    
    
    
    
# posting jobs database model (Table)
class PostJob (models.Model)  :
    CATEGORY= [
        ('Category', 'Category'),
        ('Full Time', 'Full Time'),    
        ('Part Time', 'Part Time'), 
        ('Intenship', 'Intenship'), 
    ]
    
    company = models.ForeignKey(Account ,  on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)  
    location = models.CharField(max_length=100)
    allowance = models.CharField(max_length=200, null=True , blank=True)
    job_description = models.TextField()
    requirement = models.TextField()
    category = models.CharField(max_length=200, choices=CATEGORY )
    date_posted = models.DateField(auto_now_add=True)
    
    
    
    def __str__(self):
        
        return self.job_title
    
    def get_absolute_url(self):
        # Because we are using in build django Class base view to create a from
        # using this model, we will have to tell django where to redirect to after
        # data from form sumbited is add to the model
        
        # what should happen when Employer post a job/intenship
        # It should go to PostDetail page with that post id
        # self.pk get that post id then store in the key pk
        
        # we use reverse indtead of redirect
        return reverse('postDetail', kwargs={'pk': self.pk})
   
   
# Applying for job database model (Table)   
class AppliedJobs(models.Model):
    CERTIFICATE= [
        ('Phd', 'Phd'),
        ('diploma', 'diploma'),    
        ('degreee', 'degreee'), 
         
    ]
    posted_job = models.ForeignKey(PostJob , on_delete=models.CASCADE)     
    user = models.ForeignKey(Account ,  on_delete=models.CASCADE)
    certificate = models.CharField(max_length=250, choices=CERTIFICATE, null=True , blank=True)
    experience = models.TextField( null=True , blank=True)
    date_applied = models.DateField(auto_now_add=True)
    
    def __str__(self) :
        return self.posted_job.job_title
    
    
    
#Add Career development data model(database table)   
# CareerDev(Career Development)
class CareerDev(models.Model) :
    career_link = models.TextField(null=True , blank=True)
    Career_description = models.TextField(null=True , blank=True)
    
    def __str__(self):
        
        return self. career_link
    
    def get_absolute_url(self):
        # Because we are using in build django Class base view to create a from
    # using this model, we will have to tell django where to redirect to after
    # data from form sumbited is add to the model
    
    # what should happen when Employer post a job/intenship
    # It should go to PostDetail page with that post id
    # self.pk get that post id then store in the key pk
    
    # we use reverse indtead of redirect
        return reverse('addCareer')