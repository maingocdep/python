# entiers numérique
test = 0b100
print("100 binaire:", test)

test = 0o100
print("100 octal:", test)

test = 100
print("100 décima:", test)

test = 0x100
print("100 hexadecimal:", test)

print(bin(test))
print(oct(test))
print(hex(test))

# flottante

test = 255.0
print("affectation directe:", test)

test = 2.55e2
print("notation scientifique:", test)

test = 2.55e-2
print("exposant negatif:", test)

#convertir une chaine en nombre 
print(ord("A"))
# attention A = 65  a = 97
monInt = int ("123")
print(monInt)

#convertir un nombre en chaine
machaine = str(1234.56)
print(machaine)

#obtenir une date/heuure
import datetime
print(datetime.datetime.now()) #affiche 2024-06-06 19:46:00.799494
#pour une date plus lisible
print(str(datetime.datetime.now().date())) #affiche 2024-06-06

#définir une fonction
def hello():
    print("ceci est ma premeiere fonction python !")
hello()

def Addit(valeur1, valeur2):
    print(valeur1, "+", valeur2, "=", (valeur1 + valeur2))
Addit(2,3) #affiche 2 + 3 = 5

def hello2(salutation):
    print(salutation) # argument doit être le même
hello2(1234) #affiche 1234

def hello3(bonjour):
    print(bonjour)
hello3(5+3) #affiche 8

def hello4(byebye):
    print(byebye)
hello4("ceci est une chaine")
hello4(5)
hello4(2+7)

# plusieurs argument
def hello5(Argcount, *Varargs):
    print("vous avez passé", Argcount, "argument(s).")
    for Arg in Varargs:
        print(Arg)
hello5(1,"chaine test")
hello5(3,"un","deux","trois")

#fonction de retour
def DoAdd (valeur1, valeur2):
    return valeur1 + valeur2
print("la somme de 3+4 est", DoAdd(3,4)) #affiche la somme de 3+4 est 7
print("3+4 égale 2+5 est", (DoAdd(3,4)==DoAdd(2,5))) # 3+4 égale 2+5 esty true

#récupere les saisis
nom = input("Quel est votre nom ?")
print("Bonjour", nom) #affiche bonjour toto