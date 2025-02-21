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

CHAR = 85


# Uvodni ekran
print()
print('\tPython Interest Calculator')
print()
print('#'*CHAR)
print()

# Deklaracije i unos vrijednosti

main_amount = int(input('Unesite iznos glavnice: ')) # 30000
yearly_interest = float(input('Unesite iznos godisnje kamatne stope (npr. 3.5): ')) # 3.5
time = int(input('Unesite vrijeme roka orocavanja: ')) # 20


# Glavni dio programa - izracuni i manipulacija podacima

income = main_amount * (yearly_interest / 100) * time
total_income = income + main_amount


# Prikaz podataka
print()
print(f'Nakon {time} godina, prihod od {main_amount} EUR, uz kamatnu stopu {yearly_interest}%, je: {income} EUR.')
print()
print(f'Nakon {time} godina, UKUPNI prihod od {main_amount} EUR, uz kamatnu stopu {yearly_interest}%, je: {total_income} EUR.')

print()
print('#'*CHAR)
print()

# message = 'Nakon {} godina prihod od {} EUR uz kamatnu stopu {}% je: {} EUR.'.format(time, main_amount, yearly_interest, income)
# print(message)
