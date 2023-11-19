import subprocess
from valid import ns, OKI
import random
import string

while True:

    print("--> --> Generador de contraseñas <-- <--")
    minus=OKI(input("Cantidad mínima de minusculas: "))
    mayus=OKI(input("Indique número mínimo de mayúsculas: "))
    num=OKI(input("Indique cantidad mínima de números: "))
    longitud=OKI(input("Indique longitud de la contraseña: "))
    suma=minus+mayus+num
    while longitud<suma:
        longitud=OKI(input("Longitud inadecuada: "))
    caract=string.ascii_letters+string.digits
    while True:
        contraseña=("").join(random.choice(caract) for i in range(longitud))
        #print(contraseña)
        if(sum(c.islower() for c in contraseña)>=minus
           and sum(c.isupper() for c in contraseña)>=mayus
           and sum(c.isdigit() for c in contraseña)>=num):
            break
    print("")
    print("Su contraseña es: ", contraseña)
    print("")

    conti=ns(input("¿Desea continuar? s/n: "))
    if conti==("n"):
        break 
    try:
        subprocess.call(["cmd.exe", "/C", "cls"])
    except:
        continue