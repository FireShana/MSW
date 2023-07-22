import pyautogui
import time
import random

#Najde pozici myši
def pozice_mysi():
    x, y = pyautogui.position()
    return x, y

#Vygeneruje náhodné číslo
def generator_nahodneho_cisla():
    pozice = []
    minula_pozice = pozice_mysi()
    
    while True:
        momentalni_pozice = pozice_mysi()
        if momentalni_pozice != minula_pozice: #Zařídí, aby se generovala nová pozice pouze při pohybu myši
            pozice.append(momentalni_pozice)
            minula_pozice = momentalni_pozice

        time.sleep(0.1) #Počká 0.1 sekundy než vezme další pozici

        if len(pozice) == 10:
            break

    #Vygeneruje náhodné číslo na základě pozice myši a náhodné čísla z modulu random
    nahodne_cislo = random.randint(0, 10000)
    for x, y in pozice:
        nahodne_cislo ^= (x ^ y) * 10 #Provede operaci XOR mezi x a y, vynásobí 10, a poté znovu XOR mezi nahodným číslem a výsledkem, uloží a opakuje
    
    return nahodne_cislo

#Použití a testování
seznam_nahodnych_cisel = []
seznam_stejnych_cisel = {}
pocet_nahodnych_cisel = 100

for i in range(pocet_nahodnych_cisel): 
    nahodne_cislo = generator_nahodneho_cisla()
    if nahodne_cislo in seznam_nahodnych_cisel:
        if nahodne_cislo in seznam_stejnych_cisel:
            seznam_stejnych_cisel[nahodne_cislo] += 1
        else:
            seznam_stejnych_cisel[nahodne_cislo] = 2
    else:
        seznam_nahodnych_cisel.append(nahodne_cislo)

print(f"Seznam náhodných čísel: {seznam_nahodnych_cisel}")
print(f"Seznam stejných náhodných čísel: {seznam_stejnych_cisel}")