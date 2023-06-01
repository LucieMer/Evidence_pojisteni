from pojisteny import Pojisteny

class EvidencePojisteni:
    def __init__(self):
        self.pojisteni = []

    def vytvor_pojisteneho (self):
        jmeno = input("Zadej jméno: ")
        prijmeni = input("Zadej příjmení: ")
        vek = input("Zadej věk: ")
        telefon = input("Zadej telefonní číslo: ")
        pojisteny = Pojisteny (jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)

    def seznam_pojistenych (self):
        print("Seznam pojištěných: ")
        for pojisteny in self.pojisteni:
            print(pojisteny)

    def najdi_pojisteneho (self):
        jmeno = input("Zadej jméno pojištěného: ")
        prijmeni = input("Zadej příjmení pojištěného: ")
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                print(pojisteny)
                return
        print("Pojištěný nenalezen.")