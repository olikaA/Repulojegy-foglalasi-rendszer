from models import LegiTarsasag, BelfoldiJarat, NemzetkoziJarat, FoglalasiRendszer
from ui import FelhasznaloiInterfesz

def adat_inicializalas():
    wizzair = LegiTarsasag("WizzAir")

    jarat1 = BelfoldiJarat("B001", "Budapest", 15000)
    jarat2 = NemzetkoziJarat("N001", "London", 45000)
    jarat3 = NemzetkoziJarat("N002", "New York", 120000)

    wizzair.jarat_hozzaadasa(jarat1)
    wizzair.jarat_hozzaadasa(jarat2)
    wizzair.jarat_hozzaadasa(jarat3)

    foglalasi_rendszer = FoglalasiRendszer()

    return wizzair, foglalasi_rendszer

if __name__ == "__main__":
    wizzair, foglalasi_rendszer = adat_inicializalas()
    ui = FelhasznaloiInterfesz(wizzair, foglalasi_rendszer)
    ui.fut()
