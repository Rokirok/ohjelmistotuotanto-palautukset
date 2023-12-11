from abc import abstractmethod

from tuomari import Tuomari


class KPSBase:

    def __init__(self):
        self.tuomari = Tuomari()

    def pelaa(self):
        ekan_siirto = self.hae_ekan_siirto()
        tokan_siirto = self.hae_tokan_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

            ekan_siirto = self.hae_ekan_siirto()
            tokan_siirto = self.hae_tokan_siirto(ekan_siirto)

        print("Kiitos!")
        print(self.tuomari)

    def hae_ekan_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    @abstractmethod
    def hae_tokan_siirto(self, ekan_siirto):
        pass

    def _onko_ok_siirto(self, siirto):
        return siirto in ("k", "p", "s")
