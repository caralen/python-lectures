import os


def otvaranje_racuna():
    pass


def prikaz_stanja_racuna():
    pass


def prikaz_prometa_po_racunu():
    pass


def polog_novca():
    pass


def podizanje_novca():
    pass


# izbornik
def izbornik():
    os.system("clear")

    while True:
        print("Dobrodosli u izbornik banke")
        print("Upisite 1 za kreiranje racuna")
        print("Upisite 2 za prikaz stanja racuna")
        print("Upisite 3 za prikaz prometa po racunu")
        print("Upisite 4 za polog novca")
        print("Upisite 5 za podizanje novca")
        print("Upisite 0 za izlaz")
        odgovor = int(input("- "))
        if odgovor == 0:
            break

        # provjera za svaku od opcija pa zovi funkciju

    print("Hvala sto ste koristili ovaj program, aj bok")


izbornik()
