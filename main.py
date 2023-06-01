from evidence import EvidencePojisteni

def main():
    evidence = EvidencePojisteni()

    while True:
        print("\n1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

        volba = input("Zadej volbu: ")

        if volba == "1":
            evidence.vytvor_pojisteneho()
        elif volba == "2":
            evidence.seznam_pojistenych()
        elif volba == "3":
            evidence.najdi_pojisteneho()
        elif volba == "4":
            break
        else:
            print("Neplatná volba.")

if __name__ == "__main__":
    main()