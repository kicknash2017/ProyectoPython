#usuarios = [
#    ("Marcelo",6789,"Marcelo Ramirez"),
#    ("Jefferson",5678,"Jefferson Huaman"),
#    ("Camila",1234,"Camila Gonzales"),
#    ("Martha",2345,"Martha Benites"),
#    ("Anabel",3456,"Anabel Alcocer"),
#    ("Daniela",4567,"Daniela Silva"),
#    ("Victor",5678,"Victor Calixtro"),
#    ("Felix",7890,"Felix Solano"),
#    ("Jordan",8901,"Jordan Cuellar")
#    ]

#Cajero Automatica Simulador
import random


#Ingrese el usuario
#Ingrese su contraseña

def aceptar_login(cred, usr, psw):
    # Verifica si el usuario esta en el diccionario (cred)
    tipoError = ""
    if usr in cred:
        # Verificar si el password coincide
        if cred[usr] == psw:
            return True, None


    return False, tipoError

credentiales = {"Victor":"201720003",
                "Jefferson":"201720006",
                "Marcelo":"201720011",
                "Camila":"201720021"}

while True:
    user = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")

    EsValido, tipoError = aceptar_login(credentiales, user, password)
    if EsValido != True:
        if tipoError == "P":
            print("Contraseña Invalida")
        elif tipoError == "U":
            print("Usuario Invalido")
        else:
            print("Credencial Invalido")
    else:
        break

print("Usuario Valido")

electro={
    'terma': 1500,
    'olla arrocera': 1000,
    'electrobomba 1/2 HP': 375,
    'computadora':300,
    'microondas': 1100,
    'licuadora': 300,
    'cafetera': 800,
    'ducha electrica': 3500,
    'ventilador':50,
        'refrigeradora':350,
    'cocina electrica':4500,
'aspiradora': 600,
    'equipo de sonido':80,
    'plancha':1000,
    'lavadora':500,
    'DVD':20,
    'televisor20':120,
    'celular': 10,
    'secadora': 1200
}

#Profe el 2 y 3 y 4 estan en proceso
#Por el momento solo funciona el 1 y el 0
wh=0.44
while EsValido  == True:
    print("Bienvenido", user)
    print("¿Que operacion desea utilizar?:")
    print("1.- Ingresar nuevo consumo")
    print("2.- Consulta de saldo")
    print("3.- Cambiar de usuario")
    print("4.- Crear un nuevo usuario")
    print("0.- Para cerrar la operación")
    choi=int(input("Ingrese opcion:"))
    if choi==1:
            num_art = int(input("Cantidad de artefactos a ingresar:"))
            registro = []
            for i in range(num_art):
                equipo=input("Ingrese artefacto electrico:")
                horas=int(input("Ingrese numero de horas:"))
                if equipo in electro:
                    for x in electro:
                        if x == equipo:
                            n = electro[equipo]
                    def calculo_kwh(equipo,horas):
                        consumo=equipo/1000*horas
                        return (consumo)
                    s=calculo_kwh(n,horas)
                    p = s*wh

                    print ("Usted consumio ",s,"kW/h")
                    print ("Valor en soles: s/.",p)
                    registro.append(p)
                else:
                    print("Artefacto invalido")

    if choi==2:
        suma = 0
        for i in registro:
            suma += i
        print ("Su consumo es: s/.",suma)
    elif choi==3:
        print ("Su saldo es:Falta")
    elif choi==4:
        print("Crear usuario")
    elif choi==0:
        print("Transacción Finalizada")
        print("Que tenga buen dia")
        break
