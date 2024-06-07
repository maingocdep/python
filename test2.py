#fonction de IF
testMe = 6
if testMe == 6:
    print("testMe est egal a 6 !")

value = int(input("Taper un nombre entre 1 et 10 : "))
if (value >0) and (value <=10):
    print("vous avez tape : ",value)

# fonction IF ELSE
testFo = int(input("Taper un nombre entre 1 et 10 : "))
if (testFo >0) and (testFo <=10):
    print("vous avez tape : ",testFo)
else:
    print("ERREUR : veuillez recommencer !")

# fonction IF ELIF
print("1. rouge")
print("2. orange")
print("3. jaune")
print("4. vert")
print("5. bleu")
print("6. violet")

choice = int(input("Choissez votre couleur favorite :"))
if (choice == 1):
    print("vous avez choisi rouge !")
elif (choice == 2):
    print("vous avez choisi orange !")
elif (choice == 3):
    print("vous avez choisi jaune !")
elif (choice == 4):
    print("vous avez choisi vert !")
elif (choice == 5):
    print("vous avez choisi bleu !")
elif (choice == 6):
    print("vous avez choisi violet !")

# IF ou IF ELSE multiples
one = int(input("tapez un nombre entre 1 et 10 :"))
two = int(input("tapez un nombre entre 1 et 10 :"))

if (one >= 1) and (one <=10): #ATTENTION aux tabulations
    if (two >=1) and (two <=10):
        print("votre code secret est :", one, two)
    else :
        print("la seconde valeur est incorrecte !")
else :
    print("la premiere valeur est incorrecte !")