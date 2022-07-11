from django.shortcuts import render,redirect
from pkg_resources import require
from .models import Computador, Raton, Teclado,Monitor,Computador,Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login 


@login_required
def home(request):
    listados = Raton.objects.all()
    return render(request,"index.html",{"Entradas":listados})

def salir(request):
    logout(request)
    return redirect('/')

def Inicio(request):
    listados = Raton.objects.all()
    return render(request,"indexhome.html",{"Entradas":listados})

def Teclados(request):
    listados = Teclado.objects.all()
    return render(request,"teclado.html",{"Entradas":listados})

#def ListaTeclado(request):
    #listados = Teclado.objects.all()
    #return render(request,"computador.html",{"Teclado":listados})

def Monitores(request):
    listados = Monitor.objects.all()
    return render(request,"monitor.html",{"Entradas":listados})

def Computadores(request):
    listados = Computador.objects.all()
    return render(request,"computador.html",{"Entradas":listados})


#Regitar los datos
def registrarEntradas(request):
    id_entrada= request.POST['txtNumero']
    entrada = request.POST['txtTipo']
    marca = request.POST['txtMarca']
    entradas = Raton.objects.create(id=id_entrada, tipoEntrada=entrada, marca=marca)
    return redirect('/')

def registrarHome(request):
    id_entrada= request.POST['txtNumero']
    entrada = request.POST['txtTipo']
    marca = request.POST['txtMarca']
    entradas = Raton.objects.create(id=id_entrada, tipoEntrada=entrada, marca=marca)
    return redirect('/home/')
#Teclado
def registrarTeclados(request):
    id_entrada= request.POST['txtNumero']
    entrada = request.POST['txtTipo']
    marca = request.POST['txtMarca']
    entradas = Teclado.objects.create(id=id_entrada, tipoEntrada=entrada, marca=marca)
    return redirect('/teclado/')
#Monitor
def registrarMonitor(request):
    id_monitor= request.POST['txtNumero']
    marca = request.POST['txtMarca']
    tamaño = request.POST['txtTamaño']
    monitores = Monitor.objects.create(id=id_monitor, marca=marca, tamaño=tamaño)
    return redirect('/monitor/')

def registrarCompu(request):
    id_computador= request.POST['txtNumero']
    nombre = request.POST['txtNombre']
    monitor = request.POST['txtMonitor']
    teclado=request.POST['txtTeclado']
    raton=request.POST['txtRaton']
    computadores = Computador.objects.create(id=id_computador, nombre=nombre, monitor=monitor, teclado = teclado, raton=raton)
    return redirect('/computador/')

#llamar al template para la edicion
def edicionEntradas(request,codigo):
    valor= Raton.objects.get(id=codigo)
    return render(request,"edicion.html",{"entrada": valor})

def edicionHome(request,codigo):
    valor= Raton.objects.get(id=codigo)
    return render(request,"edicionH.html",{"entrada": valor})

def edicionTeclado(request,codigo):
    valor= Teclado.objects.get(id=codigo)
    return render(request,"edicionT.html",{"entrada": valor})

def edicionMonitor(request,codigo):
    valor= Monitor.objects.get(id=codigo)
    return render(request,"edicionM.html",{"entrada": valor})

def edicionCompu(request,codigo):
    valor = Computador.objects.get(id = codigo)
    return render (request,"edicionC.html",{"entrada": valor})
#Editar los datos
def editarCurso(request):
    id_numero= request.POST['txtNumero']
    entrada = request.POST['txtTipo']
    marcas = request.POST['txtMarca']
    
    entradas= Raton.objects.get(id=id_numero)
    entradas.tipoEntrada= entrada
    entradas.marca = marcas
    entradas.save()
    return redirect('/')

def editarH(request):
    id_numero= request.POST['txtNumero']
    entrada = request.POST['txtTipo']
    marcas = request.POST['txtMarca']
    
    entradas= Raton.objects.get(id=id_numero)
    entradas.tipoEntrada= entrada
    entradas.marca = marcas
    entradas.save()
    return redirect('/home/')

def editarT(request):
    id_numero= request.POST['txtNumero']
    entrada = request.POST['txtTipo']
    marcas = request.POST['txtMarca']
    
    entradas= Teclado.objects.get(id=id_numero)
    entradas.tipoEntrada= entrada
    entradas.marca = marcas
    entradas.save()
    return redirect('/teclado/')

def editarM(request):
    id_monitor= request.POST['txtNumero']
    marca = request.POST['txtMarca']
    tamaño = request.POST['txtTamaño']
    
    entradas= Monitor.objects.get(id=id_monitor)
    entradas.marca= marca
    entradas.tamaño = tamaño
    entradas.save()
    return redirect('/monitor/') 

def editarC(request):
    id_computador= request.POST['txtNumero']
    nombre = request.POST['txtNombre']
    monitor = request.POST['txtMonitor']
    teclado=request.POST['txtTeclado']
    raton=request.POST['txtRaton']
    
    entradas= Computador.objects.get(id=id_computador)
    entradas.nombre= nombre
    entradas.monitor = monitor
    entradas.teclado = teclado
    entradas.raton = raton
    entradas.save()
    return redirect('/computador/')    

#Eliminacion de los datos
def eliminacionEntradas(request,codigo):
    entrada= Raton.objects.get(id=codigo)
    entrada.delete()
    return redirect('/')

def eliminarHome(request,codigo):
    entrada= Raton.objects.get(id=codigo)
    entrada.delete()
    return redirect('/home/')

def eliminarTeclado(request,codigo):
    entrada = Teclado.objects.get(id=codigo)
    entrada.delete()
    return redirect('/teclado/')

def eliminarMonitor(request,codigo):
    entrada = Monitor.objects.get(id=codigo)
    entrada.delete()
    return redirect('/monitor/')

def eliminarComputador(request,codigo):
    entrada = Computador.objects.get(id=codigo)
    entrada.delete()
    return redirect('/computador/')

#Resgistrar un suario
def registro(request):
    data ={
        'form': CustomUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            #messages.success(request, "Te has registrado exitosamente")
            return redirect('/home/')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

#Ver usuario
def usuarios(resquest):
    valor = Post.objects.all()
    return render(resquest,"user.html",{"Entrada":valor})
