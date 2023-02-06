# def distance(vrijednost, vrsta_konverzije):
#     """Funkcije za konverziju udaljenosti iz kilometara u milje ili milja u kilometre"""
#     if vrsta_konverzije == 0:
#         rezultat = vrijednost * 1.609344
#         print(rezultat)
#     elif vrsta_konverzije == 1:
#         # dijeli s brojem
#         pass
#     else:
#         print("greska")


# odabir_tipa_jedinice_za_konverziju = int(
#     input(
#         "Odaberite vrstu konverzije: Distance=0/Temperatur=1/Weight=2/Volume=3/Power=4: "
#     )
# )
# odabir_vrste_konverzije = int(
#     input(
#         "Odaberite konverziju: Km_Mi=0/Mi_Km=1,F_C=2/C_F=3/Po_Kg=4/Kg_Po=5/Gal_L=6/L_Gal=7/Kw_Ks=8/Ks_Kw=9: "
#     )
# )
# vrijednost_za_konverziju = int(input("Upisište vrijednost koju želite konveritrati: "))
# print(odabir_tipa_jedinice_za_konverziju)
# print(odabir_vrste_konverzije)
# print(vrijednost_za_konverziju)


# if odabir_tipa_jedinice_za_konverziju == 0:
#     distance(vrijednost_za_konverziju, odabir_vrste_konverzije)
# elif odabir_tipa_jedinice_za_konverziju == 1:
#     # temperature()
#     pass


# def kmm(unos):
#     return unos * 1000


# def mkm(unos):
#     return unos / 1000


# def eurkn(unos):
#     return unos * 7.53450


# def kneur(unos):
#     return unos / 7.53450


# print(
#     "Ovo je mali program za pretvaranje km u m i eur i kune i obrnuto.\n Za izlazak iz programa upisite x kod odabira"
# )

# while True:
#     unos = int(input("Unesite vrijednost koju zelite pretvoriti:  "))
#     odabir = input(
#         "Odaberite sto ste unijeli - 'km', 'm', 'eur','kn' ili 'x':  "
#     ).lower()

#     if odabir == "km":
#         print(f"{unos} km je {kmm(unos)} metara")
#     elif odabir == "m":
#         print(f"{unos} m je {mkm(unos)} kilometara")
#     elif odabir == "eur":
#         print(f"{unos} eura je {round(eurkn(unos),2)} kuna")
#     elif odabir == "kn":
#         print(f"{unos} kuna je {round(kneur(unos),2)} eura")
#     elif odabir == "x":
#         print("Izlaz iz programa")
#         break
#     else:
#         print("Neispravan odabir!!!")


# def lista_teksta(neki_tekst):
#     """Iz teksta izbacujemo točke, zareze , pretvaramo sva slova u mala,
#     zatim taj tekst pretvaramo u listu riječi"""
#     neki_tekst_lower = neki_tekst.lower()
#     neki_tekst_lower = neki_tekst_lower.replace(",", "")
#     neki_tekst_lower = neki_tekst_lower.replace(".", "")
#     lista_od_teksta = neki_tekst_lower.split()
#     return lista_od_teksta


# def brojac_rijeci(rijec_za_provjeru, text):
#     """Funkcija vraća koliko se puta neka riječ ponavlja u tekstu"""
#     brojac = 0
#     for rijec in lista_teksta(text):
#         if rijec == rijec_za_provjeru:
#             brojac += 1
#     return brojac


# tekst = "lorem ipsum lorem"
# trazena_rijec = input("Unesite traženu riječ:").lower()
# print(f"Vaša riječ se ponavlja {brojac_rijeci(trazena_rijec, tekst)} puta")


# tekst = "1345786240782435"

# novi_string = ""
# novi_string += "#"


# indeks = 0
# while indeks < len(tekst):
#     print(tekst[indeks])
#     indeks += 1


# def maskiranje_kartice(kartica, maska):
#     zamjenski_string = maska * (len(kartica) - 4)
#     kartica = kartica.replace(kartica[0:-4], zamjenski_string)
#     return kartica


# print(maskiranje_kartice("134245657854", "#"))


def generiraj_akord(pocetni_ton, tonovi):
    indeks_pocetnog_tona = tonovi.index(pocetni_ton)
    print(indeks_pocetnog_tona)


tonovi = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "H"]


while True:
    pocetni_ton = input("Upisite pocetni ton: ").upper()
    generiraj_akord(pocetni_ton, tonovi)
