from django.shortcuts import render
from .models import Professor 

# Create your views here.
def home(request):
    professores = Professor.objects.all()
    return render(request,'professor/home.html',{'professores':professores})