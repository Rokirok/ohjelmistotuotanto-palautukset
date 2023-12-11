from src.kivi_paperi_sakset import KPSBase
from tekoaly import Tekoaly


class KPSTekoaly(KPSBase):

    def __init__(self):
        super().__init__()
        self.tekoaly = Tekoaly()

    def hae_tokan_siirto(self, ekan_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
