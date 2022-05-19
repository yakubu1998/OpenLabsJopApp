from django.shortcuts import redirect, render

def main(request): 
    
    return render(request , 'accounts/main.html')