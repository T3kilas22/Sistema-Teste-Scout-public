from django.shortcuts import render, redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from app.models import Evento, Equipe, Round
from datetime import datetime

# Create your views here.

def index(request):
    try:
        eventos = Evento.objects.filter(usuario=request.user)
        return render(request, 'index.html', {'eventos': eventos})
    except:
        return render(request, 'index.html')

def entrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username=nome, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            return render(request, 'entrar.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'entrar.html')

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        try:
            usuario = User.objects.get(username=nome)
            return render(request, 'cadastrar.html', {'erro': 'Usuário já cadastrado'})
        except:
            usuario = User.objects.create_user(username=nome, password=senha)
            usuario.save()
            return redirect('entrar')
    return render(request, 'cadastrar.html')

def sair(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/entrar/')
def adicionar_evento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        evento = Evento(nome=nome, data= datetime.today(), usuario=request.user)
        evento.save()
        return redirect('index')
    return render(request, 'adicionar_evento.html')

@login_required(login_url='/entrar/')
def informacoes_evento(request, id):
    evento = Evento.objects.get(id=id)
    equipes = Equipe.objects.filter(evento=evento)
    if request.user != evento.usuario:
        return redirect('index')
    if request.method == 'POST':
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        equipe = Equipe(nome=nome, evento=evento, foto=foto)
        equipe.save()
        return redirect('informacoes_evento', id)
    return render(request, 'informacoes_evento.html', {'evento': evento, 'equipes': equipes})

@login_required(login_url='/entrar/')
def editar_evento(request, id):
    evento = Evento.objects.get(id=id)
    if request.user != evento.usuario:
        return redirect('index')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        evento.nome = nome
        evento.save()
        return redirect('informacoes_evento', id)
    return render(request, 'editar_evento.html', {'evento': evento})

@login_required(login_url='/entrar/')
def excluir_evento(request, id):
    evento = Evento.objects.get(id=id)
    if request.user != evento.usuario:
        return redirect('index')
    evento.delete()
    return redirect('index')

@login_required(login_url='/entrar/')
def adicionar_equipe(request, id):
    evento = Evento.objects.get(id=id)
    if request.user != evento.usuario:
        return redirect('index')
    if request.method == 'POST':
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        print(foto)
        equipe = Equipe(nome=nome, evento=evento, foto=foto)
        equipe.save()
        return redirect('informacoes_evento', id)
    return render(request, 'adicionar_equipe.html', {'evento': evento})

@login_required(login_url='/entrar/')
def informacoes_equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    evento = equipe.evento
    rounds = Round.objects.filter(equipe=equipe)
    if request.user != evento.usuario:
        return redirect('index')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        round_obj = Round(nome=nome, equipe=equipe)
        round_obj.save()
        return redirect('informacoes_equipe', id)
    return render(request, 'informacoes_equipe.html', {'equipe': equipe, 'rounds': rounds})

@login_required(login_url='/entrar/')
def excluir_equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    evento = equipe.evento
    if request.user != evento.usuario:
        return redirect('index')
    equipe.delete()
    return redirect('informacoes_evento', evento.id)

@login_required(login_url='/entrar/')
def excluir_round(request, id):
    round_obj = Round.objects.get(id=id)
    evento = round_obj.equipe.evento
    if request.user != evento.usuario:
        return redirect('index')
    round_obj.delete()
    return redirect('informacoes_equipe', round_obj.equipe.id)

@login_required(login_url='/entrar/')
def editar_equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    evento = equipe.evento
    if request.user != evento.usuario:
        return redirect('index')
    if request.method == 'POST':
        equipe.nome = request.POST.get('nome')
        equipe.autonomo_foco = request.POST.get('autonomo_foco')
        equipe.autonomo_pontuacao = request.POST.get('autonomo_pontuacao')
        equipe.teleoperado_foco = request.POST.get('teleoperado_foco')
        equipe.teleoperado_pontuacao = request.POST.get('teleoperado_pontuacao')
        equipe.save()
        return redirect('informacoes_equipe', id)
    return render(request, 'informacoes_equipe.html', {'equipe': equipe})

@login_required(login_url='/entrar/')
def informacoes_round(request, id):
    round_obj = Round.objects.get(id=id)
    evento = round_obj.equipe.evento
    equipe = round_obj.equipe
    if request.user != evento.usuario:
        return redirect('index')
    if request.method == 'POST':
        round_obj.autonomo_foco = request.POST.get('autonomo_foco')
        round_obj.autonomo_pontuacao = request.POST.get('autonomo_pontuacao')
        round_obj.teleoperado_foco = request.POST.get('teleoperado_foco')
        round_obj.teleoperado_pontuacao = request.POST.get('teleoperado_pontuacao')
        round_obj.save()
        return redirect('informacoes_equipe', equipe.id)
    return render(request, 'informacoes_round.html', {'round': round_obj, 'equipe': equipe})

@login_required(login_url='/entrar/')
def visao_geral_evento(request, id):
    evento = Evento.objects.get(id=id)
    equipes = Equipe.objects.filter(evento=evento)
    rounds = Round.objects.filter(equipe__evento=evento)
    if request.user != evento.usuario:
        return redirect('index')
    return render(request, 'visao_geral_evento.html', {
        'evento': evento,  # Adicionado para corrigir o erro
        'equipes': equipes,
        'rounds': rounds
    })