print("")
print("===MačaciaKaviaren u Claudiky===")
print("")

celkom = 0 

objednavka = input("Mochito máte?")
print("Máme 😁 ") 
objednavka = input("Kolko stojí?")
print("4 eurá")

objednavka = input("Čo si dáte?: ")

while True:
    if objednavka == "čaj":
     celkom = celkom + 2 
    elif objednavka == "káva":
       celkom = celkom + 3
    elif objednavka == "voda":
       celkom = celkom + 1
    elif objednavka == "limonáda":
       celkom = celkom + 2
    elif objednavka == "neskafe":
        celkom = celkom + 3.50
    elif objednavka == "džús":
        celkom = celkom + 3.20 
    elif objednavka == "mochito":
        celkom = celkom + 4
    elif objednavka == "pivo":
        celkom = celkom + 1.50       
    else:
       print("Toto nemáme !")     

    objednavka = input("Dáte si ešte niečo?: ")
    if objednavka == "nie":
       break

print(f"celkom: {celkom} Eur")
