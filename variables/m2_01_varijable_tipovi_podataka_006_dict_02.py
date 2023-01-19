"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    DICTIONARY - rjecnik
                    ZADATAK
"""


vozni_park = {
    1: ["Kamion", "Iveco", "OS 001 ZZ", 2015, 45000.00],
    2: ["Kamion", "Iveco", "OS 002 ZZ", 2015, 47000.00],
    3: ["Tegljač", "MAN", "RI 001 ZZ", 2018, 78000.00],
    4: ["Tegljač", "MAN", "RI 002 ZZ", 2020, 97000.00],
    5: ["Kombi", "Mercedes Benz", "ST 001 ZZ", 2013, 12000.00],
    6: ["Kombi", "Volkswagen", "ST 002 ZZ", 2021, 35000.00],
    7: ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", 2010, 9000.00],
    8: ["Dostavno vozilo", "Volkswagen", "ZG 002 ZZ", 2010, 9300.00],
}


# HEADER ROW
header_top_row = f"ID\tTip\t\tProizvodac\t\tRegistarska\t\tGodina prve\t\tCijena"
header_bottom_row = f"  \t   \t\t          \t\toznaka\t\t\tregistracije\t\t(EUR)"
header_line = "_" * 105
print(header_top_row, header_bottom_row, header_line, sep="\n")


# TABLE BODY
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")
    print(f"{vrijednost}")
    print(
        f"{vrijednost[0]}\t\t{vrijednost[1]}\t\t{vrijednost[2]}\t\t{vrijednost[3]}\t\t{vrijednost[4]}"
    )
    for element in vrijednost:
        print(f"{element}", end="\t\t")
    print()


header_top_row = f"ID\tTip\t\tProizvođač\t\tRegistarska\t\tGodina prve\t\tCijena"
header_bottom_row = f"  \t   \t\t          \t\toznaka\t\t\tregistracije\t\t(EUR)"
header_line = "_" * 100
print(header_top_row, header_bottom_row, header_line, sep="\n")
