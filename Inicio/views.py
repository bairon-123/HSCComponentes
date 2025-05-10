from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from Inicio.forms import ProductoForm
from .models import (
    Compra, Usuario, Direccion, Comuna, Region,
    Producto, Marca, Categoria, Tipoprod, Tipousuario, Detalle
)
from .Carrito import Carrito
from Inicio import models


# Create your views here.
def inicio(request):

    return render(request,'Inicio/index.html')
def inicioadmin(request):

    return render(request,'Inicio/index_admin.html') 
def vistamod(request):
    
    return render(request,'Inicio/modificar_producto.html')

def inicio(request, id=None):
    if id:
        usuario = Usuario.objects.get(username=id)
        contexto = {"usuario": usuario}
        return render(request, 'Inicio/index.html', contexto)
    else:
        return redirect('iniciar')
def addprod(request):
    tipoprod = Tipoprod.objects.all()
    marca = Marca.objects.all()
    contexto = {"TipoProd": tipoprod, "Marca": marca}
    return render(request, 'Inicio/agregar_producto.html', contexto)


def iniciar(request):

    return render(request,'Inicio/inicio_sesion.html')



def menuadmin(request):

    return render(request,'Inicio/dashboard-admin.html')

def perfiluser(request, id):
    try:
        usuario = Usuario.objects.get(username=id)
        return render(request, 'Inicio/index.html', {'usuario': usuario})
    except Usuario.DoesNotExist:
        return redirect('iniciar')

def carrito(request,id):
    usuario = Usuario.objects.get(username=id)
    contexto = {"usuario":usuario}
    return render(request,'Inicio/carrito.html', contexto)

def perfilusuario(request,id):
    usuario = Usuario.objects.get(username=id)
    contexto = {"usuario":usuario}

    return render(request,'Inicio/perfil-user.html',contexto)



def recovery_pass(request):
    return render(request, 'Inicio/recovery_pass.html')

def mostrarperfil(request, id):
    usuario = Usuario.objects.get(username=id)
    try:
        direccion = Direccion.objects.get(usuario=usuario)
    except Direccion.DoesNotExist:
        direccion = None

    region = Region.objects.all()
    comuna = Comuna.objects.all()
    contexto = {
        "usuario": usuario,
        "direccion": direccion,
        "region": region,
        "comuna": comuna
    }
    return render(request, 'Inicio/perfil_usuario.html', contexto)




def modificarPerfil(request, username):
    usuario = get_object_or_404(Usuario, username=username)

    try:
        direccion = Direccion.objects.get(usuario=usuario)
    except Direccion.DoesNotExist:
        direccion = Direccion(usuario=usuario)

    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre', '').strip()
        usuario.apellido = request.POST.get('apellido', '').strip()
        usuario.email = request.POST.get('email', '').strip()
        
        direccion.descripciondir = request.POST.get('direccion', '').strip()

        region_id = request.POST.get('region')
        comuna_id = request.POST.get('comuna')

        if region_id:
            direccion.region_id = int(region_id)
        if comuna_id:
            direccion.comuna_id = int(comuna_id)

        # Guardar los cambios
        usuario.save()
        direccion.save()

        messages.success(request, "Perfil actualizado correctamente.")
        return redirect('miperfil', id=usuario.username)
        

    # Mostrar el formulario si es GET
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

    return render(request, 'Inicio/perfil_usuario.html', {
        'usuario': usuario,
        'direccion': direccion,
        'region': regiones,
        'comuna': comunas
    })



# -------------------- PRODUCTOS --------------------
# MICROFONOS
def mostrarMic(request,id):
    micros = Producto.objects.filter(tipoprod=1)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mic": micros,"usuario":usuario}
    return render(request, "Inicio/microfonos.html",contexto)

def micadmin (request,id):
    micros = Producto.objects.filter(tipoprod=1)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mic": micros,"usuario":usuario}
    return render (request,'Inicio/micadmin.html',contexto) 


def micro(request, idmic, usuario):
    productos = get_object_or_404(Producto, idproducto=idmic)  # ✅ corregido aquí
    username = get_object_or_404(Usuario, username=usuario)
    contexto = {"prod": productos, "usuario": username}
    return render(request, "Inicio/mic1.html", contexto)

    

# TECLADOS
def mostrarTeclado(request, id):
    teclados = Producto.objects.filter(tipoprod=2)
    usuario = Usuario.objects.get(username=id)
    contexto= {"teclado": teclados,"usuario":usuario}
    return render(request, "Inicio/teclados.html",contexto)

def tecladoadmin (request,id):
    teclados = Producto.objects.filter(tipoprod=2)
    usuario = Usuario.objects.get(username=id)
    contexto = {"teclado": teclados,"usuario":usuario}
    return render (request,'Inicio/tecladoadmin.html',contexto) 

def teclado(request,idk, usuario):
    productos = Producto.objects.get(idproducto = idk)
    username = Usuario.objects.get(username=usuario)
    contexto = {"prod": productos,"usuario":username}
    return render(request, "Inicio/mic1.html",contexto)

# MOUSES
def mostrarMouse(request,id):
    mouses = Producto.objects.filter(tipoprod=5)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mouse": mouses,"usuario":usuario}
    return render(request, "Inicio/mouses.html",contexto)

def mouseAdmin (request,id):
    mouses= Producto.objects.filter(tipoprod=5)
    usuario = Usuario.objects.get(username=id)
    contexto = {"mouse": mouses,"usuario":usuario}
    return render (request,'Inicio/mouseAdmin.html',contexto) 
    
def mouse(request,idm,usuario):
    usuario = Usuario.objects.get(username=usuario)
    productos = Producto.objects.get(idproducto = idm)
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto)    

# GRAFICAS
def mostrarGrafica(request,id):
    graficas = Producto.objects.filter(tipoprod=3)
    usuario = Usuario.objects.get(username= id)
    contexto = {"grafica": graficas,"usuario":usuario}
    return render(request, "Inicio/graficas.html",contexto)

def graficaAdmin (request,id):
    graficas= Producto.objects.filter(tipoprod=3)
    usuario = Usuario.objects.get(username=id)
    contexto ={"grafica": graficas,"usuario":usuario}
    return render (request,'Inicio/graficaAdmin.html',contexto) 
    
def grafica(request,idg,usuario):
    productos = Producto.objects.get(idproducto = idg)
    usuario = Usuario.objects.get(username= usuario)
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto)    

# PROCESADORES
def mostrarProcesador(request,id):
    procesadores = Producto.objects.filter(tipoprod=6)
    usuario = Usuario.objects.get(username= id)
    contexto = {"procesador": procesadores,"usuario":usuario}
    return render(request, "Inicio/procesadores.html",contexto)

def procesadorAdmin (request,id):
    procesadores= Producto.objects.filter(tipoprod=6)
    usuario = Usuario.objects.get(username= id)
    contexto = {"procesador": procesadores,"usuario":usuario}
    return render (request,'Inicio/procesadorAdmin.html',contexto) 
    
def procesador(request,idp,usuario):
    productos = Producto.objects.get(idproducto = idp)
    usuario = Usuario.objects.get(username= usuario)
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto)  



# RAMS
def mostrarRam(request,id):
    rams = Producto.objects.filter(tipoprod=4)
    usuario = Usuario.objects.get(username= id)
    contexto = {"ram": rams,"usuario":usuario}
    return render(request, "Inicio/rams.html",contexto)

def ramAdmin (request,id):
    rams= Producto.objects.filter(tipoprod=4)
    usuario = Usuario.objects.get(username= id)
    contexto = {"ram": rams,"usuario":usuario}
    return render (request,'Inicio/ramAdmin.html',contexto) 
    
def ram(request,idr,usuario):
    productos = Producto.objects.get(idproducto = idr)
    usuario = Usuario.objects.get(username= usuario)
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto )    




def buscar_compra(request):
    return render(request, 'pages/buscar_compra.html')







def registrarse(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    contexto = {"comunas_m": comunas,"regiones_m": regiones}
    return render(request,"Inicio/registrarse.html",contexto)

def registrar_m (request):
    user = request.POST['usuario']
    contra = request.POST['contra']
    correo = request.POST['email']
    region = request.POST['region']
    direccion = request.POST['direccion']
    comuna = request.POST['comuna']
    nombree = request.POST['nombre']
    apellido = request.POST['apellido']
    comuna2 = Comuna.objects.get(idcomuna=comuna)
    region2 = Region.objects.get(idregion=region)
    tipousuario2 = Tipousuario.objects.get(idtipousuario=2)
    existe = None
    try:
        existe = Usuario.objects.get(username=user)
        messages.error(request,'El usuario ya existe')
        return redirect ('registrarse')
    except:
        Usuario.objects.create(username = user , contrasennia = contra, nombre = nombree, apellido = apellido, email = correo,tipousuario = tipousuario2)
        x = Usuario.objects.get(username = user)
        Direccion.objects.create(descripciondir=direccion, usuario=x, region=region2, comuna=comuna2)
        return redirect ('iniciar')
    

        
def iniciar_sesion(request):
    if request.method == 'POST':
        usuario1 = request.POST.get('usuario')
        contra1 = request.POST.get('contra')

        try:
            usuario2 = Usuario.objects.get(username=usuario1, contrasennia=contra1)

            # Redirige según el tipo de usuario
            if usuario2.tipousuario.idtipousuario == 1:
                return redirect('menu_admin')
            else:
                return redirect('miperfil', usuario2.username)

        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario o la contraseña son incorrectos')
            return redirect('iniciar')
    else:
        return redirect('iniciar')

    
def newProd(request):
    nombre = request.POST['nomprod']
    TipoProd = request.POST['TipoProd']
    marca = request.POST['marcaprod']
    stock = request.POST['stockprod']
    imagen = request.FILES['imgprod']
    desc = request.POST['descprod']
    precio = request.POST['precio']
    
    idProd2 = TipoProd.objects.get(idTiporod = TipoProd)
    marca2 = Marca.objects.get(idMarca = marca)
    existe = None
    try:
        existe = Producto.objects.get(nombreProducto = nombre)
        messages.error(request,'El producto ya existe')
        return redirect ('addprod')
    except:
        Producto.objects.create(nombreProducto = nombre,precioProducto = precio,especificacionProd = desc,stockProd =stock,imagenProd = imagen,tipoprod = idProd2,marca = marca2)
        return redirect ('menu_admin')
    

def eliminarProducto(request, idProducto):
    producto= Producto.objects.get(idProducto=idProducto)
    producto.delete()

    messages.success(request, '¡Producto Eliminado!')

    return redirect('indexadmin')


 
def edicionProducto(request, idProducto):
    Tipoprod = Tipoprod.objects.all()
    marca = Marca.objects.all()
    producto = Producto.objects.get(idProducto=idProducto)

    return render(request,'Inicio/edicionProducto.html', {"producto": producto, "Tipoprod":Tipoprod,"Marca":marca})


def editarProducto(request, idproducto):
    producto = get_object_or_404(Producto, idproducto=idproducto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            # Si no se sube nueva imagen, mantener la existente
            
            if 'imgprod' in request.FILES and request.FILES['imgprod']:
                producto.imagenprod = request.FILES['imgprod']
            form.save()
            messages.success(request, 'Producto actualizado correctamente')
            return redirect('lista_productos')  # Ajusta según tu vista
        else:
            messages.error(request, 'Por favor corrige los errores')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'Inicio/edicionProducto.html', {
        'form': form,
        'producto': producto,
        'Marca': Marca.objects.all(),
        'Tipoprod': Tipoprod.objects.all(),
        'marca_actual': producto.marca,
        'tipo_actual': producto.tipoprod,
    })




def confirmar_eliminar(request, producto_id):
    producto = get_object_or_404(Producto, idProducto=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente')
        return redirect('lista_productos')  # Redirige a donde necesites
    
    return render(request, 'confirmar_eliminar.html', {'producto': producto})



 

def agregar_producto(request, idProducto, usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = idProducto)
    contexto = {"producto":producto,"usuario":usuario2}
    carrito.agregar(producto)
    return render(request,'Inicio/carrito.html',contexto)

def eliminar_producto(request, idProducto,usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = idProducto)
    contexto = {"producto":producto,"usuario":usuario2}
    carrito.eliminar(producto)
    return render(request,'Inicio/carrito.html',contexto)

def restar_producto(request, idProducto,usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = idProducto)
    contexto = {"producto":producto,"usuario":usuario2}
    carrito.restar(producto)
    return render(request,'Inicio/carrito.html',contexto)

def limpiar_producto(request,usuario):
    usuario2 = Usuario.objects.get(username=usuario)
    carrito = Carrito(request)
    contexto = {"usuario":usuario2}
    carrito.limpiar()
    return render(request,'Inicio/carrito.html',contexto)






def historial_compra(request, id):
    try:
        usuario = Usuario.objects.get(username=id)
        return render(request, 'Inicio/historial_compra.html', {'usuario': usuario})
    except Usuario.DoesNotExist:
        return redirect('iniciar')



def add_to_cart(request, idproducto, usuario):
    # Obtener usuario y producto
    user = get_object_or_404(Usuario, username=usuario)
    producto = get_object_or_404(Producto, idproducto=idproducto)

    # Crear o actualizar el carrito
    carrito_item, created = Carrito.objects.get_or_create(
        usuario=user,
        producto=producto,
        defaults={'cantidad': 1}
    )

    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()

    messages.success(request, f"{producto.nombreproducto} añadido al carrito.")
    return redirect('mostrarMic', usuario.username)

