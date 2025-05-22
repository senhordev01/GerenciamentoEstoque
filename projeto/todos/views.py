from django.shortcuts import render

# Create your views here.
def ver(request):
    msg = {
        'mensagem': 'olá'
    }
    return render(request, 'cadastro.html', msg)