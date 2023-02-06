def zbroji_dva_broja(prvi_broj, drugi_broj):
    """
    Funkcija zbraja dva broja, ocekuje da to budu brojevi po tipu podataka
    """
    zbroj = prvi_broj + drugi_broj
    return zbroj


def zbroji_brojeve(brojevi):
    zbroj = sum(brojevi)
    return zbroj


# lista_brojeva = [1, 2, 3, 4, 5]
# zbroj = zbroji_brojeve(lista_brojeva)
# print(zbroj)


prvi_broj = int(input("Upisite prvi broj: "))
drugi_broj = int(input("Upisite drugi broj: "))
suma = zbroji_dva_broja(prvi_broj, drugi_broj)
print(suma)
