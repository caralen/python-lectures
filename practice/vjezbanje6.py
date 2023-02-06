tablica_rijecnik = {
    "7": " ",
    "8": " ",
    "9": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "1": " ",
    "2": " ",
    "3": " ",
}

brojevi_tablice = []

for kljuc in tablica_rijecnik:
    brojevi_tablice.append(kljuc)


def printanje_tablice(tablica):
    print(tablica["7"] + "|" + tablica["8"] + "|" + tablica["9"])
    print("-+-+-")
    print(tablica["4"] + "|" + tablica["5"] + "|" + tablica["6"])
    print("-+-+-")
    print(tablica["1"] + "|" + tablica["2"] + "|" + tablica["3"])


tablica = printanje_tablice(tablica_rijecnik)


def igra():
    simbol = "X"
    brojac = 0

    for i in range(10):
        printanje_tablice(tablica)
        print("Tvoj je potez," + simbol + ".Gdje ces ga postaviti?")

        potez = input()

        if tablica_rijecnik[potez] == " ":
            tablica_rijecnik[potez] = simbol
            brojac += 1
        else:
            print("Ovo mjesto je popunjeno.\nGdje ces ga postaviti?")
