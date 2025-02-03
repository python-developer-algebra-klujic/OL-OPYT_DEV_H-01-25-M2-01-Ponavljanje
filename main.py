'''
Kreirajte varijable (imenujte ih i dodijelite im odgovarajuću vrijednost)
te ispišite na ekran odgovarajuće vrijednosti, za:
    Imate 10000 kn i možete zaboraviti na njih na 15 godina.
    Ako Vam banka nudi 2.5% godišnju kamatu za taj iznos,
    koliko ćete zaraditi nakon 15 godina. Jednostavni kamatni račun k = C * p * t
    k = iznos kamata odnosno prinos
    C = iznos glavnice
    p = godišnja kamatna stopa – NAPOMENA: 5% = 5 / 100 = 0.05
    t = vrijeme u godinama
'''

# Deklaracije i unos vrijednosti

main_amount = 20000
yearly_interest = (5 / 100)
time = 25


# Glavni dio programa - izracuni i manipulacija podacima

income = main_amount * yearly_interest * time


# Prikaz podataka

print(income)
print(income + main_amount)
