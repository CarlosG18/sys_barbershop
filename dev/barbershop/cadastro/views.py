from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FormCliente, FormUser, FormGerente 

def cadastro(request):
    if request.method == "POST":
        form_user = FormUser(request.POST)
        form_cliente = FormCliente(request.POST,request.FILES)
        if form_cliente.is_valid() and form_user.is_valid():
            user = User.objects.create_user(username=form_user.cleaned_data["username"], email=form_user.cleaned_data["email"], password=form_user.cleaned_data["password"]) 
            user.save()
            cliente = form_cliente.save(commit=False)
            cliente.user = user
            cliente.type_cliente = 'cli'
            cliente.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form_user = FormUser()
        form_cliente = FormCliente()
    return render(request, "cadastro/cadastro.html",{
        "form_cliente": form_cliente,
        "form_user": form_user,
    })
  
def gerente(request):
    if request.method == "POST":
        form_user = FormUser(request.POST)
        form_gerente = FormGerente(request.POST,request.FILES)
        if form_gerente.is_valid() and form_user.is_valid():
            user = User.objects.create_user(username=form_user.cleaned_data["username"], email=form_user.cleaned_data["email"], password=form_user.cleaned_data["password"]) 
            user.save()
            gerente = form_gerente.save(commit=False)
            gerente.user = user
            gerente.type_cliente = 'ger'
            gerente.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form_user = FormUser()
        form_gerente = FormCliente()
    return render(request, "cadastro/gerente.html",{
        "form_gerente": form_gerente,
        "form_user": form_user,
    })
