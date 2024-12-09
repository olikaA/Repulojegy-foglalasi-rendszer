from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipusa(self):
        pass

class BelfoldiJarat(Jarat):
    def jarat_tipusa(self):
        return "Belföldi járat"

class NemzetkoziJarat(Jarat):
    def jarat_tipusa(self):
        return "Nemzetközi járat"

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

class JegyFoglalas:
    def __init__(self, foglalo_nev, jarat, foglalas_datuma):
        self.foglalo_nev = foglalo_nev
        self.jarat = jarat
        self.foglalas_datuma = foglalas_datuma

    def __str__(self):
        return f"Foglalás: {self.foglalo_nev} - {self.jarat.celallomas} ({self.jarat.jaratszam}) - {self.jarat.jegyar} HUF"

class FoglalasiRendszer:
    def __init__(self):
        self.foglalasok = []

    def jegy_foglalasa(self, foglalo_nev, jarat):
        most = datetime.now()
        jarat_elerhetoseg_vege = most + timedelta(days=30)
        if most > jarat_elerhetoseg_vege:
            return "A járat már nem elérhető foglalásra!"
        foglalas = JegyFoglalas(foglalo_nev, jarat, most)
        self.foglalasok.append(foglalas)
        return f"Foglalás sikeres! Ár: {jarat.jegyar} HUF"

    def foglalas_lemondasa(self, foglalo_nev, jaratszam):
        for foglalas in self.foglalasok:
            if foglalas.foglalo_nev == foglalo_nev and foglalas.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(foglalas)
                return "Foglalás törölve!"
        return "Foglalás nem található!"

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."
        return "\n".join([str(foglalas) for foglalas in self.foglalasok])
