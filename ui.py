class FelhasznaloiInterfesz:
    def __init__(self, legi_tarsasag, foglalasi_rendszer):
        self.legi_tarsasag = legi_tarsasag
        self.foglalasi_rendszer = foglalasi_rendszer

    def menu(self):
        print("\nRepülőjegy Foglalási Rendszer")
        print("1. Járatok listázása")
        print("2. Jegy foglalása")
        print("3. Foglalás lemondása")
        print("4. Foglalások listázása")
        print("0. Kilépés")

    def jaratok_listazasa(self):
        print("\nElérhető járatok:")
        for jarat in self.legi_tarsasag.jaratok:
            print(f"{jarat.jaratszam} - {jarat.celallomas} ({jarat.jarat_tipusa()}) - {jarat.jegyar} HUF")

    def jegy_foglalasa(self):
        nev = input("Adja meg a nevét: ")
        jaratszam = input("Adja meg a járatszámot: ")
        jarat = next((j for j in self.legi_tarsasag.jaratok if j.jaratszam == jaratszam), None)
        if jarat:
            print(self.foglalasi_rendszer.jegy_foglalasa(nev, jarat))
        else:
            print("Nincs ilyen járat!")

    def foglalas_lemondasa(self):
        nev = input("Adja meg a nevét: ")
        jaratszam = input("Adja meg a járatszámot: ")
        print(self.foglalasi_rendszer.foglalas_lemondasa(nev, jaratszam))

    def foglalasok_listazasa(self):
        print("\nAktuális foglalások:")
        print(self.foglalasi_rendszer.foglalasok_listazasa())

    def fut(self):
        while True:
            self.menu()
            valasztas = input("Választás: ")
            if valasztas == "1":
                self.jaratok_listazasa()
            elif valasztas == "2":
                self.jegy_foglalasa()
            elif valasztas == "3":
                self.foglalas_lemondasa()
            elif valasztas == "4":
                self.foglalasok_listazasa()
            elif valasztas == "0":
                print("Kilépés a rendszerből.")
                break
            else:
                print("Érvénytelen választás")
