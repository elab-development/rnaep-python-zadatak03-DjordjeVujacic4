# Đorđe Vujačić 2022/0401 - RNAEP python domaći

import random
import math

proizvodi = ["Laptop", "Miš", "Tastatura", "Monitor", "Slušalice", "Web kamera", "USB memorija", "Štampač"]
cene = {
    "Laptop": 950.99,
    "Miš": 19.99,
    "Tastatura": 45.50,
    "Monitor": 189.99,
    "Slušalice": 79.99,
    "Web kamera": 55.75,
    "USB memorija": 14.99,
    "Štampač": 129.4
}

print("Svi proizvodi i njihove cene:")
for proizvod in proizvodi:
    print(f"{proizvod} - {cene[proizvod]:.2f} €")

print()

# 4. Unos budžeta
budzet = float(input("Unesite vaš budžet u evrima: "))
print("Proizvodi koje možete da priuštite:")
ima_nesto = False

for proizvod in proizvodi:
    if cene[proizvod] <= budzet:
        print(f"{proizvod} - {cene[proizvod]:.2f} €")
        ima_nesto = True

if not ima_nesto:
    print("Nažalost, nijedan proizvod nije u okviru vašeg budžeta.")

print()

# 5. Funkcija koja vraća najskuplji proizvod
def najskuplji_proizvod(recnik_cena):
    return max(recnik_cena, key=recnik_cena.get)

najskuplji = najskuplji_proizvod(cene)
print(f"Najskuplji proizvod je: {najskuplji} - {cene[najskuplji]:.2f} €")

print()

# 6. Nasumičan proizvod koji je privukao pažnju korisnika
nasumican_proizvod = random.choice(proizvodi)
print(f"Korisniku je privukao pažnju proizvod: {nasumican_proizvod}")

print()

# 7. Prosečna cena svih proizvoda
prosek = sum(cene.values()) / len(cene)
prosecna_cena = math.floor(prosek * 100 + 0.5) / 100
print(f"Prosečna cena svih proizvoda je: {prosecna_cena:.2f} €")

print()

# 8. Broj prodatih komada svakog proizvoda i ukupan prihod
prodati_komadi = [5, 20, 12, 7, 10, 6, 30, 4]

ukupan_prihod = 0
for i in range(len(proizvodi)):
    ukupan_prihod += cene[proizvodi[i]] * prodati_komadi[i]

print(f"Ukupan prihod od prodaje je: {ukupan_prihod:.2f} €")

print()

# 9. Dodavanje novog proizvoda
novi_proizvod = "Tablet"
nova_cena = 299.99

proizvodi.append(novi_proizvod)
cene[novi_proizvod] = nova_cena

print("Ažurirana lista proizvoda:")
for proizvod in proizvodi:
    print(f"{proizvod} - {cene[proizvod]:.2f} €")

print()

# 10. Sortiranje proizvoda po ceni
print("Proizvodi sortirani od najjeftinijeg ka najskupljem:")
sortirani_proizvodi = sorted(cene, key=cene.get)

for proizvod in sortirani_proizvodi:
    print(f"{proizvod} - {cene[proizvod]:.2f} €")