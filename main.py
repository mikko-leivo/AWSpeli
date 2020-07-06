#Funktiot eli kysymykset
oikeat_vastaukset = []
kysymyslista = [1,2,3,4,5]
import random
random.shuffle(kysymyslista)

#Kysymys1
def kysymys1(kysymyslista, oikeat_vastaukset):
    vastaus = input("Millä toiminnolla saat kaksi VPC:tä kommunikoimaan keskenään?:\na)Endpoint\nb)NAT Gateway\nc)Peering Connection\nVastauksesi: ").lower()
    if vastaus =="a" or vastaus=="b" or vastaus=="c":
        if vastaus =="c":
            oikeat_vastaukset.append(1)
            print("Vastasit oikein")
    else:
        print("vastaa a, b tai c")

#Kysymys2
def kysymys2(kysymyslista, oikeat_vastaukset):
    vastaus = input("Millä komennolla listaat tiedostoja s3 bucketista Puttyssa?:\na)ls -la\nb)ls\nc)list\nVastauksesi: ").lower()
    if vastaus =="a" or vastaus=="b" or vastaus=="c":
        if vastaus =="b":
            oikeat_vastaukset.append(1)
            print("Vastasit oikein")
    else:
        print("vastaa a, b tai c")

#Kysymys3
def kysymys3(kysymyslista, oikeat_vastaukset):
    vastaus = input("Onko EC2 Amazonin palvelu?:\na)Ehkä\nb)Kyllä\nc)Ei\nVastaa a, b tai c: ").lower()
    if vastaus =="a" or vastaus=="b" or vastaus=="c":
        if vastaus =="b":
            oikeat_vastaukset.append(1)
            print("Vastasit oikein")
    else:
        print("vastaa a, b tai c")

#Kysymys4
def kysymys4(kysymyslista, oikeat_vastaukset):
    vastaus = input("Kysymys:Väite: Julkinen aliverkko on saavutettavissa internetyhteyden kautta ja yksityinen ei ole\na) Kyllä\nb) Ei kaikki verkot ovat internetin välityksellä\nc) Ei mikään aliverkko ei ole saavutettavissa internetin välityksellä\nVastauksesi: ").lower()
    if vastaus =="a" or vastaus=="b" or vastaus=="c":
        if vastaus =="a":
            oikeat_vastaukset.append(1)
            print("Vastasit oikein")
    else:
        print("vastaa a, b tai c")

#Kysymys5
def kysymys5(kysymyslista, oikeat_vastaukset):
    vastaus = input("Kysymys:Onko S3 Amazonin palvelu?\na) Ei\nb) Kyllä\nc) En tiedä\nVastauksesi: ").lower()
    if vastaus =="a" or vastaus=="b" or vastaus=="c":
        if vastaus =="b":
            oikeat_vastaukset.append(1)
            print("Vastasit oikein")
    else:
        print("vastaa a, b tai c")



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
        x = len(oikeat_vastaukset)
        print(f'Hieno homma, vastasit onnistuneesti yhteensä {x} kysymykseen.')
        lopeta = input('Paina Enter ja poistu pelistä.')
    elif kysymys.startswith("e"):
        break
    else:
        print("Dude, pliis vastaa K tai E.")
    break