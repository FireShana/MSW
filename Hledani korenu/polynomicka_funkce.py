import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import time

#Definice polynomické funkce
def f(x):
    return -x**3 + 3*x**2 + x - 3

#Graf funkce
x = np.linspace(-4, 4, 100)
plt.plot(x, f(x))
plt.axhline(0, color = "black")
plt.axvline(0, color = "black")
plt.grid()
plt.show()

#Definice Bisekce
def bisekce(a, b, tolerance):
    while abs(a - b) >= tolerance:
        c = (a + b) / 2 #Rozdělení intervalu
        vzorec = f(a) * f(c) #Dosazení do vzorce
        if vzorec >= tolerance:
            a = c #Posunutí začátečního intervalu
        else:
            b = c #Posunutí konečného intervalu
    return c

#Definice Newton metody
def newton(a, b, tolerance):
    x_sym = sp.Symbol("x") #Převod "x" na matematickou proměnou
    f_sym = -x_sym**3 + 3*x_sym**2 + x_sym - 3 #Převod funkce na symbolickou funkci
    f_num = sp.lambdify(x_sym, f_sym, "numpy") #Převod funkce na numerickou funcki

    def df(x, h = 1E-3): #Derivace funkce
        return (f_num(x + h) - f_num(x - h)) / (2 * h)

    c = (a + b) / 2 #Rozdělení intervalu
    while abs(c - a) >= tolerance:
        a = c
        c = a - f_num(a) / df(a) #Dosazení do vzorce
    return c

#Použití Bisekce
zacatek_bisekce = time.time()
koren1 = bisekce(-5, 0, 1e-8)
koren2 = bisekce(0, 2, 1e-8)
koren3 = bisekce(2, 5, 1e-8)
cas_bisekce = (time.time() - zacatek_bisekce) * 1000  #Převede na milisekundy

print(f"Metoda Bisekce - Kořen 1: {koren1}")
print(f"Metoda Bisekce - Kořen 2: {koren2}")
print(f"Metoda Bisekce - Kořen 3: {koren3}")
print(f"Čas nalezení kořenů (Metoda Bisekce): {cas_bisekce:.6f} milisekundy")

#Použití Newton metody
zacatek_newton = time.time()
koren1 = newton(-5, 0, 1e-8)
koren2 = newton(0, 2, 1e-8)
koren3 = newton(2, 5, 1e-8)
cas_newton = (time.time() - zacatek_newton) * 1000  #Převede na milisekundy

print(f"Newton metoda - Kořen 1: {koren1}")
print(f"Newton metoda - Kořen 2: {koren2}")
print(f"Newton metoda - Kořen 3: {koren3}")
print(f"Čas nalezení kořenů (Newton metoda): {cas_newton:.6f} milisekundy")

#Graf, který porovnává rychlost metod
metody = ["Bisekce", "Newton metoda"]
casy = [cas_bisekce, cas_newton]

plt.bar(metody, casy)
plt.title("Porovnání rychlosti metody Bisekce a Newton")
plt.xlabel("Metoda")
plt.ylabel("Čas (v ms)")
plt.show()