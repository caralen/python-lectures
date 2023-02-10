# def povratak(user):
#     print()
#     unos = input('Upišite "0" za povratak u glavni izbornik:')

#     while True:
#         if unos == "0":
#             return
#         else:
#             print('Pogrešan unos, upišite "0" za povratak na glavni izbornik.')
#             povratak()
#             print("NAKON POZIVA POVRATAK")


# def izbornik():
#     print("izbornik")
#     return


# # glavni program
# izbornik()


# zbroj = 0


# # rekurzija
# def zbrajaj():
#     global zbroj
#     zbroj += 1
#     zbrajaj()


# zbrajaj()


def zbroji(a, b):
    zbroj = a + b
    print(zbroj)
    while True:
        print()
        if 5 < 6:
            break
        else:
            print("Laz")


def izbornik():
    zbroji(1, 5)
