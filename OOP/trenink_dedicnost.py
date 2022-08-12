class Clovek:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni

    def jdi_do_prace(self):
        print("Těším se, jaké nové hodnoty dnes vytvořím.")

    def jdi_do_kavarny(self):
        print("Dám si kávu a dort.")

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Programator(Clovek):
    def __init__(self, jmeno, prijmeni, jazyk):
        super().__init__(jmeno, prijmeni)
        self.jazyk = jazyk

    def programuj(self):
        print("Použiju dnes cyklus for nebo while?")

    def jdi_do_kavarny(self):
        super().jdi_do_kavarny()
        print("Je lepší Python nebo Java? V kavárně to vyřešíme.")

    def __str__(self):
        return f"Rád programuji v jazyce {self.jazyk}"

class Manazer(Clovek): 
    def vyhod_zamestnance(self):
        print("Tak koho dnes vyhodíme?? :)")

    def jdi_do_kavarny(self):
        print("Dnes v kavárně probereme výsledky za minulý měsíc.")

karel = Clovek("Karel", "Novák")
jakub = Programator("Jakub", "Starosta", "Python")
michal = Manazer("Michal", "Novotný")

lidi = [karel, jakub, michal]

for clovek in lidi:
    print()
    print(clovek)
    clovek.jdi_do_kavarny()


class Clovek:
    pocet_vytvorenych_lidi = 0

    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.__class__.pocet_vytvorenych_lidi += 1

    @staticmethod
    def vytiskni_pocet_lidi_staticky():
        return f"Už bylo vytvořeno {Clovek.pocet_vytvorenych_lidi} lidí. - statická metoda"

    @classmethod
    def vytiskni_pocet_lidi_pomoci_classmethod(cls):
        return f"Už bylo vytvořeno {cls.pocet_vytvorenych_lidi} lidí. - třídní metoda"

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

adam = Clovek("Adam", "Novák")
karel = Clovek("Karel", "Černý")

print(Clovek.vytiskni_pocet_lidi_staticky())
print(Clovek.vytiskni_pocet_lidi_pomoci_classmethod())