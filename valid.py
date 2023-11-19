def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7)); c=input("Escribí solo 'n' o 's', según tu necesidad")
    return(c)