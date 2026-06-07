import random

while True:

    cislo = random.randint(1, 10)


    while True:

             pokusy +=1

             tip = int(input("Hadaj cislo (1-10):"))


             if tip == cislo:
                print(f"Uhadol si na {pokusy} pokusov ✌️ !")
    
             elif tip < cislo:
                print("Daj viac")
    
             else:
                print("Daj menej")
    
             print("Čislo bolo:", cislo)
             
    znova = input               
   
    
 

