class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        arvo = 0

        try:
            arvo = int(self.lue_syote())
        except Exception:
            pass

        self.sovelluslogiikka.plus(arvo)