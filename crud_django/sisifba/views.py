from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        return render(request,'sisifba/home.html')        
    else:
        return render(request,'login/login.html')