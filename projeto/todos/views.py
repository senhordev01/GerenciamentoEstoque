from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from todos.forms import UserRegistry, PedidoForm, ProdutoForm
from todos.models import Produto, Pedido
from django.shortcuts import redirect

@login_required
def index(request):
    orders_user = Pedido.objects.all()
    users = User.objects.all()[:2]
    orders_adm = Pedido.objects.all()[:2]
    products = Produto.objects.all()[:2]
    reg_users = len(User.objects.all())
    all_prods = len(Produto.objects.all())
    all_orders = len(Pedido.objects.all())
    context = {
        "title": "Home",
        "orders": orders_user,
        "orders_adm": orders_adm,
        "users": users,
        "products": products,
        "count_users": reg_users,
        "count_products": all_prods,
        "count_orders": all_orders,
    }
    return render(request, "todos/index.html", context)

@login_required
def produtos(request):
    produtos = Produto.objects.all()
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProdutoForm()
    context = {"title": "Produtos", "produtos": produtos, "form": form}
    return render(request, "todos/products.html", context)


@login_required
def pedidos(request):
    pedidos = Pedido.objects.all()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            produto = instance.produto
            pedidoQuantidade = instance.pedidoQuantidade

            if produto.estoque >= pedidoQuantidade:
                produto.estoque -= pedidoQuantidade
                produto.save()
                instance.criado_por = request.user
                instance.save()
                return redirect("orders")
            else:
                    form.add_error('pedidoQuantidade', 'Not enough stock available.')

    else:
        form = PedidoForm()
    context = {"title": "Pedidos", "pedidos": pedidos, "form": form}
    return render(request, "todos/orders.html", context)

@login_required
def users(request):
    users = User.objects.all()
    context = {"title": "Users", "users": users}
    return render(request, "todos/users.html", context)

def register(request):
    if request.method == "POST":
        form = UserRegistry(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistry()
    context = {"register": "Register", "form": form}
    return render(request, "todos/register.html", context)

@login_required
def user(request):
    context = {"profile": "User Profile"}
    return render(request, "todos/user.html", context)

@login_required
def deletar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    if request.user == pedido.criado_por or request.user.is_superuser:
        produto = pedido.produto
        produto.estoque += pedido.pedidoQuantidade
        produto.save()
        pedido.delete()

    return redirect('orders') 

@user_passes_test(lambda u: u.is_superuser)
def aumentar_estoque(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        try:
            quantidade = int(request.POST.get("quantidade"))
            if quantidade > 0:
                produto.estoque += quantidade
                produto.save()
        except:
            pass
    return redirect("products")

@user_passes_test(lambda u: u.is_superuser)
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.delete()
    return redirect("products")


#def ver(request):
#    if request.method == "POST":
#        nome = request.POST.get('Nome')
#        email = request.POST.get('Email')
#        confirmar_email = request.POST.get('Confirmar_Email')
#        senha = request.POST.get('Senha')
#        confirmar_senha = request.POST.get('Confirmar_Senha')

#        if email != confirmar_email or senha != confirmar_senha:
#            return render(request, 'cadastro.html', {'erro': 'Erro na confirmação'})
        
#        senha_criptografada = make_password(senha)
#        Dados.objects.create(nome=nome, email=email, senha=senha_criptografada)

#        return redirect('entrar_site')  # ou render(...)

#    return render(request, 'cadastro.html')


#def login(request):
#    if request.method == 'POST':
#        email = request.POST.get('email')
#        senha = request.POST.get('senha')
    
#        try:
#            usuario = Dados.objects.get(email=email)
#        except Dados.DoesNotExist:
#            return render(request, 'login.html', {'erro': 'Email não encontrado'})
        
#        if check_password(senha, usuario.senha):
#            return redirect('site_primario')
#        else:
#            return render(request, 'login.html', {'erro': 'Senha incorreta'})

#    return render(request, 'login.html')

#def lista_produtos(request):
#    produtos = Produto.objects.filter(estoque__gt=0, disponivel=True)
#    return render(request, 'site.html', {'produtos': produtos})