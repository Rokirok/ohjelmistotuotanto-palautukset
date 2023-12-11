from kivi_paperi_sakset import KPSBase
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPSBase):

    def __init__(self):
        super().__init__()
        self.tekoaly = TekoalyParannettu(10)

    def hae_tokan_siirto(self, ekan_siirto):
        self.tekoaly.aseta_siirto(ekan_siirto)
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
