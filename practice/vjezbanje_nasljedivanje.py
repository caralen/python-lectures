class Osoba:
    def __init__(self, ime, oib, adresa):
        self.ime = ime
        self.oib = oib
        self.adresa = adresa


class Tvrtka(Osoba):
    def __init__(self, ime, oib, adresa, broj_djelatnika, pravni_oblik):
        Osoba.__init__(self, ime, oib, adresa)
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik


class Djelatnik(Osoba):
    def __init__(self, ime, oib, adresa, radno_mjesto):
        Osoba.__init__(self, ime, oib, adresa)
        self.radno_mjesto = radno_mjesto


djelatnik1 = Djelatnik("David", "4324324", "Zagreb", "Informatičar")


print(djelatnik1.ime)
