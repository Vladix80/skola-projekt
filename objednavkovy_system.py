line = "========================"
print(line)
print("Reštauracia u Pythona")
print(line)
print("")
print("1. PIzza - 150 Kč")
print("2. Hamburger = 120 Kč")
print("3. Salát - 90 Kč")
print("")
print(line)

# získanie informacii od zákazníka
objednavka = input("Čo si dáte?")
meno = input("Vaše meno:")
adresa = input("Doručovacia adresa:")

# potvrdenie objednávky
print ("")
print("========================")
print("Dakujeme"  + meno + "!")
print("Vaša objednavka:" + objednavka)
print("Doručíme na:"  + adresa)
print("====================")