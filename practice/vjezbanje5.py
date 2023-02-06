import random

opcije = ["x", "o"]
trenutni_igrac = random.choice(opcije)
igra_aktivna = True
pobjednik = None

ploca = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def ispis_ploce(ploca):
    brojac = 1
    for i in ploca:
        if brojac % 3 == 0:
            print(i)
        else:
            print(i, end=" ")
        brojac += 1


def igra():
    global pobjednik
    ispis_ploce(ploca)
    while igra_aktivna:
        igrac_na_redu(trenutni_igrac)
        # provjeri_kraj()
    if pobjednik == "x" or pobjednik == "o":
        print(f'Pobjednik je "{pobjednik}".')
    elif pobjednik == None:
        print("Neriješeno.")


def igrac_na_redu(igrac):
    global igra_aktivna
    if igra_aktivna == True:
        print(f"Na redu je {igrac}")
        polje = input("Upišite broj od 1 do 9 za željeno polje: ")
        polje = int(polje) - 1  # ovo ce puknut ako je upisao nesto sto nije broj

        if polje >= len(ploca):
            print("Unijeli ste krivi unos")
            return

        if ploca[polje] == "-":  # TU JE PROBLEM
            ploca[polje] = igrac

        elif ploca[polje] not in range(0, 9):
            print("Neispravan unos, upišite broj od 1 do 9.")
            igrac_na_redu()
        else:
            print("Odaberite drugo polje.")
            igrac_na_redu()


# promijeni_igraca()
ispis_ploce(ploca)
