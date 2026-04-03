from django.shortcuts import render
# importacao para definir que uma função só será acessível para usuarios autenticados
from django.contrib.auth.decorators import login_required
# home do sistema
@login_required(login_url='/login/')
def home(request):
    # se 
    if request.user.is_authenticated:
        return render(request,'sisifba/home.html')        
    else:
        return render(request,'login/login.html')