import random
from random import randint

with open("d.csv", encoding='utf-8') as f: # fail sisaldab kõikide Orkla Eesti ja Maiasmoka töötajate
    f.readline()            # nimesid, üksusi, tervisekontrolli kp, bak analüüsi kp, 
    töötajate_nimekiri=[]                # röntgeni kp, hügieenikoolituse kp ja lepingu seisu  ehk
                            # 7 elementi töötaja kohta, mis on komaga eraldatud

    for i in f:
        j = i.split(",")
        töötajate_nimekiri.append(j)

random.shuffle(töötajate_nimekiri) # paiska töötajate nimekiri segamini

#TLPLHP lapsehoolduspuhkusel
#TLPHD sünnituspuhkusel

i=3 # loosime 3 SPA paketti nendele, kes pole lapsehooldus- ega sünnituspuhkusel
järjekord=1 # sea esimese võitja järjekorra numbriks 1

while i > 0: 
    juhuslik_arv = randint(0, len(töötajate_nimekiri)) # sjuhuslik arv nullist kuni max töötajate arvuni (töötajaid on kokku üks
                                                          # rohkem kui nimekirja pikkus, sest nimekirja esimene on indeksiga null)
    juhuslik_töötaja = töötajate_nimekiri.pop(juhuslik_arv)  # võta nimekirjast juhuslik töötaja koos tema andmetega ja eemalda ta edasisest loosimisest
    
    if juhuslik_töötaja[6].rstrip("\n") != "TLPLHP" and juhuslik_töötaja[6].rstrip("\n") != "TLPHD": # ära arvesta neid, kes on sünnitus- või lapsehoolduspuhkusel
        print("Õnnelik võitja number",järjekord) # prindi enne võitjad tema järjekorra nr ja tekst "õnnelik võitja"
        print(juhuslik_töötaja[0], juhuslik_töötaja[2], sep="\n") # prindi õnneliku võitja nimi ja osakond
        i -= 1 # vähenda loositavate pakettide arvu
        järjekord+=1 # suurenda võitja järjekorra numbrit
