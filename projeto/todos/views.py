from django.shortcuts import render

# Create your views here.
def ver(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')