import random


# def playing_grid():
#     print("_" + "|" + "_" + "|" + "_")
#     print("_" + "|" + "_" + "|" + "_")
#     print(" " + "|" + " " + "|" + " ")


# def izbor_znakova_za_igrace(znak_igraca_a, znak_igraca_b):
#     for znak in znak_igraca_a:
#         znak_igraca_a = random.choice(lista_znakova_za_igrače)
#     for znak in znak_igraca_a:
#         znak_igraca_b = random.choice(lista_znakova_za_igrače)

#     print(f"Igrač A ima znak {znak_igraca_a}")
#     print(f"Igrač B ima znak {znak_igraca_b}")


# def definicija_igracih_simbola():
#     lista_znakova_za_igrače = ["X", "O"]
#     znak_kompa = random.choice(lista_znakova_za_igrače)
#     if znak_kompa == "X":
#         znak_korisnika = "O"
#     else:
#         znak_korisnika = "X"
#     return znak_kompa, znak_korisnika


# znak_kompa, znak_korisnika = definicija_igracih_simbola()
# print("znak_kompa", znak_kompa)
# print("znak_korisnika", znak_korisnika)


# playing_grid()
# izbor_znakova_za_igrace()


lista = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

for red in lista:
    for element in red:
        print(element, end=" ")
    print()


print(lista[0], "|", lista[1], "|", lista[2])
print(lista[0], "|", lista[1], "|", lista[2])
print(lista[0], "|", lista[1], "|", lista[2])
