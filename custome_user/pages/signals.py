from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Account
from accounts.models import StudentProfile , EmployerProfile

# from accounts.models import 

@receiver(post_save, sender=Account)
def create_student_profile(sender,instance,created, **kwargs):
    if created:
        if instance.usertype == 'Student' :
            StudentProfile.objects.create(user=instance)
        elif instance.usertype == 'Alumni' :
            StudentProfile.objects.create(user=instance)
        elif instance.usertype == 'Admin' :
            EmployerProfile.objects.create(user=instance)
        else :
            EmployerProfile.objects.create(user=instance)
      
     
# Catch signal sent and save the new student profile
# @receiver(post_save, sender=Account)
# def save_student_profile(sender, instance, **kwargs):
#     instance.studentprofile.save()            
        

 
# signal for employer        

# @receiver(post_save, sender=Account)
# def create_employer_profile(sender,instance,created, **kwargs):
#     if created:
#         EmployerProfile.objects.create(user=instance)
        
     
     
# Catch signal sent and save the new student profile
# @receiver(post_save, sender=Account)
# def save_employer_profile(sender, instance, **kwargs):
#     instance.employerprofile.save()  