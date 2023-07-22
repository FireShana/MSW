import random
from collections import Counter
import matplotlib.pyplot as plt

#Funkce, která ověří, jaká je líznutá kombinace
def liznuta_kombinace(liznute_karty):
    vysledek = ""
    mezery = 0
    barvy = []
    hodnosti = []
    pocet_hodnoty = []

    for karta in liznute_karty: #Projde všechny karty, které jsou líznuté
        hodnost, barva = karta #Rozdělí tuple
        hodnosti.append(hodnost)
        barvy.append(barva)
    
    pocet_stejnych_hodnosti = Counter(hodnosti) #Vytvoří slovník z listu hodnosti a přiřadí každé hodnotě, kolikrát se v listu objevilo
    serazene_hodnosti = sorted(hodnosti)

    if len(set(barvy)) != 1:  #Spustí se, když nemají všechny karty stejné barvy
        for pocet in pocet_stejnych_hodnosti.values(): #Projde values slovníku a každou hodnotu přiřadí do listu
            pocet_hodnoty.append(pocet)
        maximum = max(pocet_hodnoty)
        if len(pocet_stejnych_hodnosti) == 2 and maximum == 4:
            vysledek = "Čtveřice"
        elif len(pocet_stejnych_hodnosti) == 2 and maximum == 3:
            vysledek = "Trojice a Dvojice"
        elif len(pocet_stejnych_hodnosti) == 3 and maximum == 3:
            vysledek = "Trojice"
        elif len(pocet_stejnych_hodnosti) == 3 and maximum == 2:
            vysledek = "Dvojice"
        elif len(pocet_stejnych_hodnosti) == 4:
            vysledek = "Pár"
        elif serazene_hodnosti == [2, 3, 4, 5, 14]:  #Speciální případ postupky, kdy se A=1
                vysledek = "Postupka"
        else:
            for i in range(len(serazene_hodnosti) - 1): #Kontroluje, jestli mezi sebou čísla mají mezery
                mezera = serazene_hodnosti[i + 1] - serazene_hodnosti[i]
                mezery += mezera
                if mezery == 4:
                    vysledek = "Postupka"
                else:
                    vysledek = "Žádná kombinace" 
    elif len(set(barvy)) == 1:  #Spustí se, když mají všechny karty stejné barvy
        if serazene_hodnosti == [2, 3, 4, 5, 14]:  #Speciální případ postupky, kdy se A=1
            vysledek = "Čistá postupka"
        else:
            for i in range(len(serazene_hodnosti) - 1): #Kontroluje, jestli mezi sebou čísla mají mezery
                mezera = serazene_hodnosti[i + 1] - serazene_hodnosti[i]
                mezery += mezera
                if mezery == 4:
                    vysledek = "Čistá postupka"
                else:
                    vysledek = "Barva"
    else:
        vysledek = "Žádná kombinace"

    return vysledek
    
#Funkce, která vypočítá pravděpodobnost líznutí každé možné kombinace v Pokeru
def monte_carlo(pocet_iteraci):
    cista_postupka = 0
    ctverice = 0
    trojice_a_dvojice = 0
    barva5 = 0
    postupka = 0
    trojice = 0
    dvojice = 0
    par = 0
    zadna_kombinace = 0

    balicek = [(hodnost, barva) for hodnost in range(2, 15) for barva in ['Piky', 'Srdce', 'Káry', 'Kříže']] #J=11, Q=12, K=13, A=14
    for i in range(pocet_iteraci):
        random.shuffle(balicek)
        liznute_karty = balicek[:5] #Vezme prvních 5 karet z balíčku
        if liznuta_kombinace(liznute_karty) == "Čistá postupka":
            cista_postupka += 1
        if liznuta_kombinace(liznute_karty) == "Čtveřice":
            ctverice += 1
        if liznuta_kombinace(liznute_karty) == "Trojice a Dvojice":
            trojice_a_dvojice += 1
        if liznuta_kombinace(liznute_karty) == "Barva":
            barva5 += 1
        if liznuta_kombinace(liznute_karty) == "Postupka":
            postupka += 1
        if liznuta_kombinace(liznute_karty) == "Trojice":
            trojice += 1
        if liznuta_kombinace(liznute_karty) == "Dvojice":
            dvojice += 1
        if liznuta_kombinace(liznute_karty) == "Pár":
            par += 1
        if liznuta_kombinace(liznute_karty) == "Žádná kombinace":
            zadna_kombinace += 1

    pr_cista_postupka = cista_postupka / pocet_iteraci
    pr_ctverice = ctverice / pocet_iteraci
    pr_trojice_a_dvojice = trojice_a_dvojice / pocet_iteraci
    pr_barva = barva5 / pocet_iteraci
    pr_postupka = postupka / pocet_iteraci
    pr_trojice = trojice / pocet_iteraci
    pr_dvojice = dvojice / pocet_iteraci
    pr_par = par / pocet_iteraci
    pr_zadna_kombinace = zadna_kombinace / pocet_iteraci
    return pr_cista_postupka, pr_ctverice, pr_trojice_a_dvojice, pr_barva, pr_postupka, pr_trojice, pr_dvojice, pr_par, pr_zadna_kombinace

pocet_iteraci = 1000000

pr_cista_postupka, pr_ctverice, pr_trojice_a_dvojice, pr_barva, pr_postupka, pr_trojice, pr_dvojice, pr_par, pr_zadna_kombinace = monte_carlo(pocet_iteraci) #Rozdělení tuple z returnu funkce monte_carlo

print(f"Pravděpodobnost líznutí čisté postupky při počtu iterací {pocet_iteraci} je {pr_cista_postupka * 100:.4f}%.")
print(f"Pravděpodobnost líznutí čtveřice při počtu iterací {pocet_iteraci} je {pr_ctverice * 100:.4f}%.")
print(f"Pravděpodobnost líznutí trojice a dvojice při počtu iterací {pocet_iteraci} je {pr_trojice_a_dvojice * 100:.4f}%.")
print(f"Pravděpodobnost líznutí barvy při počtu iterací {pocet_iteraci} je {pr_barva * 100:.4f}%.")
print(f"Pravděpodobnost líznutí postupky při počtu iterací {pocet_iteraci} je {pr_postupka * 100:.4f}%.")
print(f"Pravděpodobnost líznutí trojice při počtu iterací {pocet_iteraci} je {pr_trojice * 100:.4f}%.")
print(f"Pravděpodobnost líznutí dvojice při počtu iterací {pocet_iteraci} je {pr_dvojice * 100:.4f}%.")
print(f"Pravděpodobnost líznutí páru při počtu iterací {pocet_iteraci} je {pr_par * 100:.4f}%.")
print(f"Pravděpodobnost líznutí žádné kombinace při počtu iterací {pocet_iteraci} je {pr_zadna_kombinace * 100:.4f}%.")

#Uloží pravděpodobnosti a názvy kombinací do dvou listů
pravdepodobnosti = [pr_cista_postupka * 100, pr_ctverice * 100, pr_trojice_a_dvojice * 100, pr_barva * 100, pr_postupka * 100, pr_trojice * 100, pr_dvojice * 100, pr_par * 100, pr_zadna_kombinace * 100]
kombinace = ['Čistá postupka', 'Čtveřice', 'Trojice a Dvojice', 'Barva', 'Postupka', 'Trojice', 'Dvojice', 'Pár', 'Žádná kombinace']

#Vytvoří graf
plt.bar(kombinace, pravdepodobnosti)
plt.title(f"Pravděpodobnost líznutí kombinací při {pocet_iteraci} iteracích")
plt.xlabel("Kombinace")
plt.ylabel("Pravděpodobnost v %")

#Upraví názvy kombinací a přidá nejvyšší hodnotu na jednotlivých sloupcích
plt.xticks(rotation = 90)
for i, pravdepodobnost in enumerate(pravdepodobnosti):
    plt.annotate(f"{pravdepodobnost:.2f}%", (i, pravdepodobnost), ha = "center", va = "bottom", fontsize = 8)

plt.tight_layout()
plt.show()
