#Funktiot eli kysymykset

#Kysymys1
def kysymys1(kysymyslista):
    vastaus = input("Kysymys:\na)vaihtoehto\nb)vaihtoehto\nc)vaihtoehto\nVastauksesi: ").lower()
    if vastaus =="a" or vastaus=="b" or vastaus=="c":
        if vastaus =="a":
            oikeat_vastaukset +=1
    else:
        print("vastaa a, b tai c")
        # onko mikolla isot jalat:
        # a)on
        # b)on tosi isot
        # c)no ihan helvetin isot
        # d) pienet ja kauniit
#Kysymys2

#Kysymys3

#Kysymys4

#Kysymys5




oikeat_vastaukset = 0
kysymyslista = [1,2,3,4,5]
import random
random.shuffle(kysymyslista)


while True:
    kysymys = input("Hei haluatko pelata? Vastaa K(yllä) tai E(i): ").lower()
    if kysymys.startswith("k"):
        print("hep")
        #peli
    elif kysymys.startswith("e"):
        break
    else:
        print("Dude, pliis vastaa K tai E.")