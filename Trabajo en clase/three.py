'''
@file three.py
@author RonaldJapon
@email ronald.japon@unl.edu.ec
@nota tratamiento de cadenas de caracteres
'''
nombre= input("dijite su nombre: ")
longitud=len(nombre)
print(longitud)
#Realiza la impresión del primer caracter.
print(nombre[0:1])
#Realiza la impresión del ultimo caracter.
print(nombre[-1:longitud])
contar=0
for c in nombre:
#    print(c)
    if c== "a" or c== "A":
        contar=contar+1
print(contar)