red = 3
stupac = 3
ploca = [1, 2, 3, 4, 5, 6, 7, 8, 9]
igrac1 = ""
igrac2 = ""
koordinata = 0


def stvori_plocu():
    for broj in range(9):
        ploca.append(broj)


def crtaj_plocu():
    print("  0     1     2")
    for i in range(red):
        for j in range(stupac):
            print(ploca[red], end=" ")
        print(" ", i)


def odabir_igraca():
    igrac1 = input("\nOdaberite Koji ste igrac - X ili O:   ").upper()
    if igrac1 == "X":
        igrac2 = "O"
    else:
        igrac2 = "X"

    print(f"Igrac 1 je: {igrac1} a igrac 2 je {igrac2}")


def odabir_pozicije():
    print("Pomoću koordinata odaberite poziciju na koju zelite staviti svoj znak!   ")
    koordinata = input("Unesite koordinate (npr 00 za prvu poziciju):  ")
    if koordinata == "00":
        pass


stvori_plocu()
# print(ploca)
crtaj_plocu()
# odabir_igraca()
# print(ploca)
# print(ploca)
