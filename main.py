#Funktiot eli kysymykset
oikeat_vastaukset = 0
kysymyslista = [1,2,3,4,5]
import random
random.shuffle(kysymyslista)

#Kysymys1
def kysymys1(kysymyslista, oikeat_vastaukset):
    vastaus = input("Onko EC2 Amazonin palvelu?:\na)Ehkä\nb)Kyllä\nc)Ei\nVastaa a, b tai c: ").lower()
    if vastaus =="a" or vastaus=="b" or vastaus=="c":
        if vastaus =="b":
            oikeat_vastaukset =oikeat_vastaukset + 1
            print("Vastasit oikein")
    else:
        print("vastaa a, b tai c")

#Kysymys2

while True:
    kysymys = input("Hei haluatko pelata? Vastaa K(yllä) tai E(i): ").lower()
    if kysymys.startswith("k"):
        for numero in kysymyslista:
            if numero == 1:
                kysymys1(kysymyslista, oikeat_vastaukset)
            elif numero == 2:
                kysymys2(kysymyslista, oikeat_vastaukset)
            elif numero == 3:
                kysymys3(kysymyslista, oikeat_vastaukset)
            elif numero == 4:
                kysymys4(kysymyslista, oikeat_vastaukset)
            elif numero == 5:
                kysymys5(kysymyslista, oikeat_vastaukset)
            else:
                break

        print(f'Hieno homma, vastasit onnistuneesti yhteensä {oikeat_vastaukset} kysymykseen.')
        lopeta = input('Paina Enter ja poistu pelistä.')
    elif kysymys.startswith("e"):
        break
    else:
        print("Dude, pliis vastaa K tai E.")
    break