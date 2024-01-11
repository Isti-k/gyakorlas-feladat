import epuletek


epuletek_lista=epuletek.fajlbeolvasas()

epuletek.epuletek_szama(epuletek_lista)

hossza=epuletek.epuletek_szama(epuletek_lista)
print("III/A, B:")
print(f"\t Az épületek száma: {hossza}.")

db=epuletek.magas_epuletek_szama(epuletek_lista)
print("III/C:")
print(f"\t Az 555 lábnál magasabb épületek száma: {db}.")

legoregebb_index=epuletek.legoregebb_epulet(epuletek_lista)
print("III/D:")
print(f"\t A legöregebb épület országa: {epuletek_lista[legoregebb_index].orszag}.")

legtobb_em_szam=epuletek.legtöbb_em(epuletek_lista)
print("+ feladat:")
print(f"\t A legtöbb emelet száma: {epuletek_lista[legtobb_em_szam].nev} {epuletek_lista[legtobb_em_szam].em_szam}.")



