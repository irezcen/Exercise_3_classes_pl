class Parking:
    def __init__(self, liczba_miejsc, zajete_miejsca, utarg):
        self.liczba_miejsc = liczba_miejsc
        self.zajete_miejsca = zajete_miejsca
        self.utarg = utarg
        self.wszystkie_numery_osobowe = []
        self.wszystkie_numery_ciezarowe = []
        self.wszystkie_numery_jednosladowe = []
        self.aktualne_numery = []

    def wjazd(self, typ, numer):
        if self.zajete_miejsca == self.liczba_miejsc:
            print('brak wolnych miejsc')
            return
        self.zajete_miejsca = self.zajete_miejsca + 1
        mnoznik_ceny = 1
        if numer in self.aktualne_numery:
            print('ten pojazd jest juz na parkingu')
            return
        else:
            self.aktualne_numery.append(numer)
        if typ == 'jednoslad':
            if numer in self.wszystkie_numery_jednosladowe:
                pass
            else:
                self.wszystkie_numery_jednosladowe.append(numer)
            mnoznik_ceny = mnoznik_ceny * 0.5
        elif typ == 'ciezarowy':
            if numer in self.wszystkie_numery_ciezarowe:
                pass
            else:
                self.wszystkie_numery_ciezarowe.append(numer)
            mnoznik_ceny = mnoznik_ceny * 3
        else:
            if numer in self.wszystkie_numery_osobowe:
                pass
            else:
                self.wszystkie_numery_osobowe.append(numer)
        self.utarg = self.utarg + 10 * mnoznik_ceny

    def wyjazd(self, numer):
        if numer in self.aktualne_numery:
            self.zajete_miejsca = self.zajete_miejsca - 1
            self.aktualne_numery.remove(numer)
        else:
            print('tego pojazdu nie ma na parkingu')


class Samochod:
    def __init__(self, numer_rejestracyjny, kolor, typ):
        self.numer_rejestracyjny = numer_rejestracyjny
        self.kolor = kolor
        self.typ = typ

    def wjazd_na_parking(self):
        return self.typ, self.numer_rejestracyjny
        # parking.wjazd(self.typ, self.numer_rejestracyjny)

    def wyjazd_z_parkingu(self):
        return self.numer_rejestracyjny

    # def wysw_informacje(self):
    #    print(self.typ, self.numer_rejestracyjny, self.kolor)


def test():
    parking = Parking(5, 0, 0)
    samochod1 = Samochod('KRA 012J8', 'bialy', 'jednoslad')
    samochod2 = Samochod('KRA 352JH', 'czerwony', 'jednoslad')
    samochod3 = Samochod('KRA 82BCK', 'zolty', 'osobowy')
    samochod4 = Samochod('KCH 01953', 'czarny', 'osobowy')
    samochod5 = Samochod('RJS U76K1', 'bialy', 'ciezarowy')
    samochod6 = Samochod('GD 5HC3', 'niebieski', 'ciezarowy')
    parking.wjazd(samochod1.wjazd_na_parking()[0], samochod1.wjazd_na_parking()[1])
    parking.wjazd(samochod2.wjazd_na_parking()[0], samochod2.wjazd_na_parking()[1])
    parking.wjazd(samochod3.wjazd_na_parking()[0], samochod3.wjazd_na_parking()[1])
    parking.wyjazd(samochod2.wyjazd_z_parkingu())
    print('wjechaly samochody 1,2,3 i wyjechal samochod 2\nzajete miejsca i utarg: ')
    print(parking.zajete_miejsca)
    parking.wjazd(samochod2.wjazd_na_parking()[0], samochod2.wjazd_na_parking()[1])
    parking.wjazd(samochod4.wjazd_na_parking()[0], samochod4.wjazd_na_parking()[1])
    parking.wjazd(samochod5.wjazd_na_parking()[0], samochod5.wjazd_na_parking()[1])
    print('wjechaly samochody 2,4,5\nutarg i zajete miejsca: ')
    print(parking.zajete_miejsca, parking.utarg)
    parking.wjazd(samochod6.wjazd_na_parking()[0], samochod6.wjazd_na_parking()[1])
    parking.wyjazd(samochod1.wyjazd_z_parkingu())
    parking.wjazd(samochod6.wjazd_na_parking()[0], samochod6.wjazd_na_parking()[1])
    print('samochod 6 probowal wjechac na parking, wyjechal samochod 1, wjechal samochod 6\nzajete miejsca i utarg: ')
    print(parking.zajete_miejsca, parking.utarg)
    parking.wyjazd(samochod2.wyjazd_z_parkingu())
    parking.wyjazd(samochod3.wyjazd_z_parkingu())
    parking.wyjazd(samochod4.wyjazd_z_parkingu())
    parking.wyjazd(samochod5.wyjazd_z_parkingu())
    parking.wyjazd(samochod6.wyjazd_z_parkingu())
    print('wszystkie samochody wyjechaly z parkingu\nzajete miejsca i utarg: ')
    print(parking.zajete_miejsca, parking.utarg)
    print('wszystkie numery:\n', parking.wszystkie_numery_osobowe,
          parking.wszystkie_numery_ciezarowe, parking.wszystkie_numery_jednosladowe)
    print('numery pojazdow ciezarowych\n', parking.wszystkie_numery_ciezarowe)


test()
