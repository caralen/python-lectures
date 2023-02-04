### KORISNIČKI DEFINIRANE FUNKCIJE ###



# kljucna rijec DEF
def pozdrav(ime):
    """
    Funkcija koja na konzolu ispisuje pozdravnu poruku osobi
    cije ime je proslijedeno u funkciju kao parametar
    """
    print(f'Dobar dan, {ime}. Kako ste danas?')

# POZIV FUNKCIJE
pozdrav('Petar')

# PRISTUP DOKUMENTACIJI FUNKCIJE - docstring
print(pozdrav.__doc__)
# Ovaj dio koda ispisuje tekst koji je naveden unutar docstring bloka prilikom deklaracije funkcije


import datetime 

# DEKLARACIJA FUNKCIJE
def pozdrav(ime):
    """
    Funkcija koja ovisno o dobu dana vrati pozivatelju pozdravnu poruku za osobu cije ime je proslijedeno u funkciju kao parametar.
    Ako je vrijeme poziva funkcije prijepodne poruka ce glasiti 'Dobro jutro, IME. Danas je novi dan.'
    Ako je vrijeme poziva funkcije poslijepodne poruka ce glasiti 'Dobar dan, IME. Dobro Vam ide, nastavite tako..'
    Ako je vrijeme poziva funkcije vecer poruka ce glasiti 'Dobra vece, IME. Danasnji dan je bio uspjesan.'
    """
    if datetime.datetime.now().hour < 12: 
        return f'\nDobro jutro, {ime}. Danas je novi dan.\n'
    elif datetime.datetime.now().hour > 12 and datetime.datetime.now().hour < 19: 
        return f'\nDobar dan, {ime}. Dobro Vam ide, nastavite tako.\n'
    else: 
        return f'\nDobra vece, {ime}. Danasnji dan je bio uspjesan.\n'


# POZIV FUNKCIJE
pozdravna_poruka = pozdrav('Petar')
print(pozdravna_poruka)
print(pozdrav.__doc__)




def sakrij_znakove(tekst):
    zasticeni_tekst = ''
    if len(tekst) <= 5:
        return f'Tekst {tekst} ima 5 ili manje znakova!'
    else:
        limit_zastite = len(tekst) - 4
        indeks = 0
        for znak in tekst:
            if indeks < limit_zastite:
                zasticeni_tekst += '#'
                indeks += 1
            else:
                zasticeni_tekst += znak
                indeks += 1
        
        return zasticeni_tekst


kartica = input('\nUpišite broj vaše krediten kartice:\t')

print(f'\nNEzaštićeni prikaz vašu kreditne kartice: {kartica}')
print(f'ZAŠTIĆENI prikaz vašu kreditne kartice: {sakrij_znakove(kartica)}\n')
