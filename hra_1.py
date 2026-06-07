import random

cislo = random.randint(1, 10)

tip = int(input("Hádaj číslo (1-10): "))

if tip == cislo:
    print("🎉 👌 Uhadol si!")
else:
    print("❌ Neuhádol si. Číslo bolo:", cislo)