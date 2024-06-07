print("1. oeufs")
print("2. crêpes")
print("3. gaufres")
print("4. fruits")

Mainchoice = int(input("Que voulez vous au petit-dejeuner ?"))

if (Mainchoice == 2): #1ere condition
    Meal = "crêpes"
elif (Mainchoice == 3):
    Meal = "gaufres"


if (Mainchoice == 1): #2eme condition
    print("1. galette au froment")
    print("2. beignet")
    print("3. galette au seigle")
    print("4. crêpe nature")
    pancake = int(input("choisissez votre accompagnement :"))

    if (pancake ==1):
        print("vous avez choisi des oeufs avec une galette au fromen !t")
    elif (pancake == 2):
        print("vous avez choisi des oeufs avec un beignet !")
    elif (pancake == 3) :
        print("vous avez choisi des oeufs avec une galette au seigle !")
    elif (pancake == 4):
        print("vous avez choisi des oeufs avec une crêpe nature !")
    else :
        print("Nous avons des oeufs mais pas de crêpes !")


elif(Mainchoice ==2) or (Mainchoice == 3):
    print("1. caramel")
    print("2. confiture")
    print("3. sucre en poudre")
    topping = int(input("choisissez votre garniture :"))

    if (topping == 1):
        print("vous avez choisi" + Meal + "au caramel !")
    elif (topping == 2):
        print("vous avez choisi" + Meal + "a la confiture !")
    elif (topping == 3):
        print("vous avez choisi" + Meal + "au sucre !")

elif (Mainchoice == 4):
    print("vous avez choisi des cereales !")

else :
    print("nous n'avons pas cela dans le menu !")