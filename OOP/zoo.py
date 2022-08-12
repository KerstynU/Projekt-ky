class Zvire:
    def __init__(self, barva, pocet_nohou):
        self.barva = barva
        self.pocet_nohou = pocet_nohou

    def vydej_zvuk(self):
        raise Exception("nejsem žádné konkrétní zvíře")


class Pes(Zvire):
    def __init__(self, barva, rasa):
        super().__init__(barva, 4)
        self.rasa = rasa

    def hlidej(self):
        return "pokoušu vás"

    def vydej_zvuk(self):
        return "haf haf haf"

    def __repr__(self):
        return f"{self.barva} {self.rasa}"


class Had(Zvire):
    def __init__(self, barva, delka):
        super().__init__(barva, 0)
        self.delka = delka

    def vyhrivej_se_na_slunicku(self):
        return "to je teplo"

    def vydej_zvuk(self):
        return "sssssssss"

    def __repr__(self):
        return f"had barvy {self.barva}"


class Klec:
    def __init__(self):
        self.zvirata = []

    def pridej_zvire(self, zvire):
        if isinstance(zvire, Zvire):
            self.zvirata.append(zvire)
        else:
            raise Exception("přidáváš do klece něco, co není zvíře")

    def pridej_zvirata(self, *args):
        for zvire in args:
            self.pridej_zvire(zvire)

    def __repr__(self):
        return ", ".join([str(zvire) for zvire in self.zvirata])


class Zoo:
    def __init__(self):
        self.klece = []

    def pridej_klec(self, klec):
        if isinstance(klec, Klec):
            self.klece.append(klec)
        else:
            raise Exception("přidáváš do zoo něco, co není klec - to tam nepatří")

    def pridej_klece(self, *args):
        for klec in args:
            self.pridej_klec(klec)

    def vypis_podle_barvy(self, barva):
        print(f"Vypisuju zvířata s barvou {barva}:")
        for klec in self.klece:
            for zvire in klec.zvirata:
                if zvire.barva == barva:
                    print(zvire)
        print()

    def spocitej_nohy(self):
        print("Počítám počet nohou pro sponzora...")
        vysledek = 0
        for klec in self.klece:
            for zvire in klec.zvirata:
                vysledek += zvire.pocet_nohou
        print(f"Prosíme tě o {vysledek} ponožek.")

    def __repr__(self):
        return "---".join(str(klec) for klec in self.klece)

erik = Had("červená", 5)
kolumbus = Had("hnědá", 7)

alik = Pes("bílý", "labrador")
rex = Pes("černý", "vlčák")

seznam = [erik, kolumbus, alik, rex, Had("žlutý", 7), Pes("červený", "akita")]

for zvire in seznam:
    print(zvire.vydej_zvuk())




klec1 = Klec()

klec1.pridej_zvire(erik)
klec1.pridej_zvire(kolumbus)

print(klec1.zvirata)

klec2 = Klec()

klec2.pridej_zvirata(alik, rex, Pes("hnědá", "shiba"))

print(klec2.zvirata)

zoo = Zoo()

zoo.pridej_klece(klec1, klec2)

print(zoo)

zoo.vypis_podle_barvy("bílý")
zoo.vypis_podle_barvy("hnědá")

zoo.spocitej_nohy() 