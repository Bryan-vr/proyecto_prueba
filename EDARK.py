#DATOS ADMINISTRADOR
import sys
usuarioad = "admin"
contrasenia = "admin1028"

lista = list()

class Consumidores:
    def __init__(self): #Utilizamos el metodo init 
        self.nom_usuario= ("")
        self.num_identificacion=() 
        self.clave=("")
        self.edad=()

#metodo menu
def menu():
    Decisión= 0
#Decisión distinta a 11, continuara
    while Decisión!= 11:
        print ("-------------------------------------------------------")
        print ("Bienvenidos a la plataforma EDARK")
        print ("EDARK-----EDARK-----EDARK-----EDARK-----EDARK-----EDARK")
        print ("Eliga la opción que desee")
        print ("-------------------------------------------------------")
        print ("1. REGISTRARSE")
        print ("2. HACER UNA COMPRA")
        print ("3. SEGUIMIENTO")
        print ("4. ENVIAR UNA PQRS")
        print ("5. REPORTE DE VENTAS **Exclusivamente para administrador**")
        print ("6. ¿QUIERES SABER TU TALLAJE?")
        print ("7. BUSCAR PRODUCTOS")
        print ("8. BUSCAR INFORMACIÓN DE CONSUMIDORES **Exclusivamente para administrador**")
        print ("9. MIRA LOS ULTIMOS PRODUCTOS DE EDARK")
        print ("10. ¿QUIERES PEDIR UN REEMBOLSO?")
        print ("11. SALIR DE LA PLATAFORMA")

        Decisión= int (input("Eliga una opción: "))
#Funciones
        if Decisión == 1:
            registrar ()
        elif Decisión == 2:
            comprar ()
        elif Decisión == 3:
            seguimiento ()
        elif Decisión == 4:
            pqrs ()
        elif Decisión == 5:
            reporte ()
        elif Decisión == 6:
            tallaje ()
        elif Decisión == 7:
            buscar ()
        elif Decisión == 8:
            info_consumidores ()
        elif Decisión == 9:
            ultimos_productos ()
        elif Decisión == 10:
            reembolso ()
        elif Decisión == 11:
            salir ()

#Definimos funciones

def registrar ():
    print ("Has seleccionado registrar, a continuación te podras registrar a nuestra plataforma")
#Usuario tomara las propiedades de la clase consumidores 
    usuario=Consumidores()
    usuario.nom_usuario= input ("Ingresa el nombre de usuario")
    usuario.num_identificacion= int (input ("Ingresa tu numero de cedula"))
    usuario.clave= input ("Ingrese la clave")
    usuario.edad= int (input("Ingresa tu edad"))

    lista.append(usuario) 
def comprar ():
    print ("Has seleccionado comprar, ahora elegi que producto deseas")

def seguimiento ():
    print ("Has seleccionado seguimiento, ahora podras observar en que estado esta tu paquete")

def pqrs ():
    print ("Has seleccionado pqrs, ahora puedes digitar tu mensaje")

def reporte ():
    print ("Has seleccionado reportes, debes de ingresar un usuario de administrador")
    for i in range (2):
        user = input ("ingrese su usuario: ")
        if user == usuarioad:
            for i in range(2):
                passw = input ("dame la contraseña: ")
                if passw == contrasenia:
                    print("Bienvenido, a continuación se mostrara el reporte semanal")
                    sys.exit()
                else:
                    print ("Error")
        else:
            print("Error de usuario")

def tallaje ():
    print ("Has seleccionado tallaje")
    print ("**RECUERDA**: por el momento solo manejamos la sugerencia de tallaje en la prenda camisa")

    def determinar_talla(medidas):
        contorno_pecho = float(medidas)  # Convertir la entrada a un número decimal

    # Definir los rangos para cada talla en base al contorno de pecho
        rangos_tallas = {'XS': (35, 80), 'S': (80, 90), 'M': (90, 100), 'L': (100, 110), 'XL': (110, float('inf'))}

    # Comparar el contorno de pecho con los rangos de cada talla y determinar la talla correspondiente
        for talla, (min_valor, max_valor) in rangos_tallas.items():
            if contorno_pecho >= min_valor and contorno_pecho < max_valor:
                return talla

    # Si no se encuentra ninguna talla adecuada, devolver None
        return None

    medidas = input("Ingresa el contorno de pecho en centímetros: ")
    talla = determinar_talla(medidas)

    if talla:
        print("Tu talla de contorno de pecho es:", talla)
    else:
        print("No se encontró una talla adecuada para el contorno de pecho ingresado.")

def buscar ():
    print ("Has seleccionado el buscador")

def info_consumidores ():

    print ("Has seleccionado informacion de consumidores, debes de ingresar un usuario de administrador")
    for i in range (2):
        user = input ("ingrese su usuario: ")
        if user == usuarioad:
            for i in range(2):
                passw = input ("dame la contraseña: ")
                if passw == contrasenia:
                    print("Bienvenido, a continuación se mostrara la información de los usuarios")
                    for usuario in lista:
                        print ("El consumidor se llama", usuario.nom_usuario,"su numero de identificación es", usuario.num_identificacion, "su clave es", usuario.clave, "y su edad es", usuario.edad)
                    sys.exit()
                else:
                    print ("Error")
        else:
            print("Error de usuario")

def ultimos_productos ():
    print ("Has seleccionado ultimos productos, a continuación te mostraremos el catálogo")

def reembolso ():
    print ("Has seleccionado reembolso")

def salir ():
    print ("¡¡¡Gracias por usar nuestra plataforma!!!")
    print ("VUELVE PRONTO") 
#-------------------------------------------------------------------------------------------------------------------
menu()