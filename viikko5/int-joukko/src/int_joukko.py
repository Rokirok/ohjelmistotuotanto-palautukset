KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def on_positiivinen_luku(self, luku):
        return isinstance(luku, int) and luku >= 0

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not self.on_positiivinen_luku(kapasiteetti):
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")

        if not self.on_positiivinen_luku(kasvatuskoko):
            raise Exception("Kasvatuskoon tulee olla positiivinen kokonaisluku")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def indeksi(self, luku):
        for i in range(0, self.alkioiden_lkm):
            if luku == self.ljono[i]:
                return i
        return -1

    def kuuluu(self, n):
        return self.indeksi(n) != -1

    def kasvata_listaa(self):
        taulukko_old = self.ljono
        self.kopioi_lista(self.ljono, taulukko_old)
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.ljono)

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.ljono):
                self.kasvata_listaa()
            return True

        return False

    def poista(self, n):
        if not self.kuuluu(n):
            return False

        kohta = self.indeksi(n)
        apu = 0
        self.ljono[kohta] = 0

        for j in range(kohta, self.alkioiden_lkm - 1):
            apu = self.ljono[j]
            self.ljono[j] = self.ljono[j + 1]
            self.ljono[j + 1] = apu

        self.alkioiden_lkm = self.alkioiden_lkm - 1
        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
