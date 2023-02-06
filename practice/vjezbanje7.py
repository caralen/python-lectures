baza_korisnika = {"admin": ["admin", "admin", "password123"]}


def unos_korisnickog_imena():
    while True:
        korisnicko_ime = input("Unesite korisnicko ime: ")
        if korisnicko_ime in baza_korisnika:
            break
        else:
            print("Uneseno korisnicko ime ne postoji u bazi, molimo pokusajte ponovno")
    return korisnicko_ime


korisnicko_ime = unos_korisnickog_imena()
print("bok", korisnicko_ime)
