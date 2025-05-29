from django.shortcuts import render, redirect
from .models import Dados, Produto
from django.contrib.auth.hashers import make_password, check_password
from .forms import PagamentoForm


def ver(request):
    if request.method == "POST":
        nome = request.POST.get('Nome')
        email = request.POST.get('Email')
        confirmar_email = request.POST.get('Confirmar_Email')
        senha = request.POST.get('Senha')
        confirmar_senha = request.POST.get('Confirmar_Senha')

        if email != confirmar_email or senha != confirmar_senha:
            return render(request, 'cadastro.html')
        
        senha_criptografada = make_password(senha)
        Dados.objects.create(usuario=nome, email=email, senha=senha_criptografada)

        return redirect('entrar_site')

    return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
        try:
            usuario = Dados.objects.get(email=email)
        except Dados.DoesNotExist:
            return render(request, 'login.html')
        
        if check_password(senha, usuario.senha):
            request.session['email_usuario_logado'] = usuario.email
            request.session['usuario_logado'] = usuario.usuario
            return redirect('site_primario')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

def lista_produtos(request):
    produtos = Produto.objects.filter(estoque__gt=0, disponivel=True)
    return render(request, 'site.html', {'produtos': produtos})



def pagar_produto(request):
    produtos = Produto.objects.filter(estoque__gt=0, disponivel=True)
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            email_logado = request.session.get('email_usuario_logado')
            if not email_logado:
                return redirect('entrar_site') 

            pagamento = form.save(commit=False)
            pagamento.usuario = Dados.objects.get(email=email_logado)

            produto = pagamento.produto
            quantidade_comprada = pagamento.quantidade

            if produto.estoque >= quantidade_comprada:
                produto.estoque -= quantidade_comprada
                produto.save()

                pagamento.total = produto.preco * quantidade_comprada
                pagamento.save()

                return redirect('pagamento_sucesso')
            else:
                form.add_error(None, 'Estoque insuficiente para esse produto.')
    else:
        form = PagamentoForm()

    return render(request, 'site.html', {'form': form, 'produtos': produtos})

def pagamento_sucesso(request):
    return render(request, 'pagamento_sucesso.html')  


