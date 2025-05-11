from django.urls import path
from .views import iniciar,iniciar_sesion, inicio, inicioadmin, perfiluser, registrar_m, registrarse, newProd,addprod,vistamod,eliminarProducto,menuadmin,micadmin,tecladoadmin,mouseAdmin,ramAdmin,graficaAdmin,procesadorAdmin,mostrarTeclado,teclado,mostrarMic,micro,mostrarMouse,mouse,mostrarGrafica,grafica,mostrarRam,ram,mostrarProcesador,procesador,carrito,perfilusuario,edicionProducto,editarProducto, mostrarperfil, modificarPerfil ,agregar_producto,eliminar_producto,restar_producto,limpiar_producto
from django.conf import settings
from django.conf.urls.static import static

from Inicio import views


urlpatterns = [

    #Pagina iniciar/ Solo carga pagina
    path('iniciar/',iniciar,name="iniciar"),
    
    #Valida usuario / Aqui tenemos las consultas
    #Sacamos datos de aqui d1
    path('iniciarsesion/',iniciar_sesion,name ="iniciarsesion"),

    # La pagina principal
    #Metemos datos aqui d1
    path('', inicio, name="inicio"),



    path('indexadmin',inicioadmin,name="indexadmin"),
    path('registrar/', registrar_m, name="registrar"),
    path('registrarse/',registrarse,name="registrarse"),
    #Pag agregar producto
    path('agregar2/',newProd,name ="addProd"),
    path('agregar/',addprod,name="agregarprod"),
    #modificar un producto
    path('modificar/',vistamod,name="modificar"),
    path('eliminarProducto/<idProducto>',eliminarProducto,name="eliminarProducto"),
    path('confirmar_eliminar/<int:producto_id>/', views.confirmar_eliminar, name='confirmar_eliminar'),
    

    #Pag menu admin
    path ('menuadmin/',menuadmin,name="menu_admin"),
    path('micadmin/<id>',micadmin,name="micadmin"),
    path('tecladoadmin/<id>',tecladoadmin,name="tecladoadmin"),
    path('mouseAdmin/<id>',mouseAdmin,name="mouseAdmin"),
    path('ramAdmin/<id>',ramAdmin,name="ramAdmin"),
    path('graficaAdmin/<id>',graficaAdmin,name="graficaAdmin"),
    path('procesadorAdmin/<id>',procesadorAdmin,name="procesadorAdmin"),
    
    #Mostrar productos
    # MICRÓFONOS
    path('microfonos/<str:id>', mostrarMic, name="mostrarMic"),
    path('microfono/<int:idmic>/<str:usuario>', micro, name="micro"),
    path('add/<int:idproducto>/<str:usuario>/', views.add_to_cart, name='Add'),
    path('mic-admin/<str:id>/', views.micadmin, name="micadmin"),
    

    # MOUSE
    path('mouses/<str:id>', mostrarMouse, name="mostrarMouse"),
    path('mouse/<int:idm>/<str:usuario>', mouse, name="mouse"),
    path('mouse-admin/<str:id>/', views.mouseAdmin, name="mouseAdmin"),
    path('mouse/<int:idmic>/<str:usuario>/', views.mouseAdmin, name='mouse'),


    # TECLADO
    path('teclados/<str:id>', mostrarTeclado, name="teclados"),
    path('teclado/<int:idk>/<str:usuario>', teclado, name="teclado"),
    path('teclado-admin/<str:id>/', views.tecladoadmin, name="tecladoadmin"),



    # GRAFICA
    path('graficas/<str:id>', mostrarGrafica, name="mostrarGrafica"),
    path('grafica/<int:idg>/<str:usuario>', grafica, name="grafica"),
    path('grafica-admin/<str:id>/', views.graficaAdmin, name="graficaAdmin"),



    # RAM
    path('rams/<str:id>', mostrarRam, name="mostrarRam"),
    path('ram/<int:idr>/<str:usuario>', ram, name="ram"),
    path('ram-admin/<str:id>/', views.ramAdmin, name="ramAdmin"),


    # PROCESADOR
    path('procesadores/<str:id>', mostrarProcesador, name="mostrarProcesador"),
    path('procesador/<int:idp>/<str:usuario>', procesador, name="procesador"),
    path('procesador-admin/<str:id>/', views.procesadorAdmin, name="procesadorAdmin"),



    #Carrito
    path('carrito/<id>',carrito, name="carrito"),
    path('agregar3/<int:idProducto>/<str:usuario>',agregar_producto,name="Add"),
    path('eliminar/<int:idProducto>/<str:usuario>',eliminar_producto,name="Del"),
    path('restar/<int:idProducto>/<str:usuario>',restar_producto,name="Sub"),
    path('limpiar/<str:usuario>',limpiar_producto,name="CLS"),
    #Usuario
    path('miperfil/<id>',perfilusuario, name="miperfil"),
    path ('mostrarperfil/<id>', mostrarperfil, name="mostrarperfil"),
    path('modificarperfil/<str:username>/', views.modificarPerfil, name='modificarPerfil'),
    path('recuperar-contrasenia/', views.recovery_pass, name='recuperar_contrasenia'),    
    path('buscar-compra/', views.buscar_compra, name='buscar_compra'),
    path('edicionProducto/<idProducto>', edicionProducto, name="edicionProducto"),
    path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),
    path('historial-compra<str:id>/', views.historial_compra, name='historial_compra'),
    path('index/<id>',perfiluser, name="index"),
    path('index/<str:id>/', inicio, name="index"),
    path('editar-producto/<int:idproducto>/', views.editarProducto, name='editar_producto'),


    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)