"""A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a epulet.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki az épületek számát a mintának megfelelően a konzolra! (2p)
C.	Adja meg az 555 lábnál magasabb épületek számát, ha 1 m = 3.280839895 láb! (4p)
D.	Írassa ki konzolra a mintának megfelelően a legöregebb épület (ha több is van, akkor az első legöregebb adatait) országát. (4p)"""


from Epulet import Epulet
def fajlbeolvasas():
    epuletek_lista=[] #objektumok
    f=open("epulet.txt","r",encoding="utf-8")
    f.readline()
    fajl_lista=f.readlines()
    f.close()
    #print(fajl_lista[0])fájlnak az első sora a fejléc nélkül,
    for i in range(0,len(fajl_lista),1):
        aktsor=fajl_lista[i].replace(",",".").strip().split("$")
        epuletem=Epulet(aktsor[0],aktsor[1],aktsor[2],float(aktsor[3]),int(aktsor[4]),int(aktsor[5]))
        print(epuletem.nev,epuletem.varos,epuletem.orszag,epuletem.magassag,epuletem.em_szam,epuletem.epult)
        epuletek_lista.append(epuletem)

    return epuletek_lista
    

def epuletek_szama(lista):
    return len(lista)

def magas_epuletek_szama(lista):
    db:int=0
    for i in range(0,len(lista),1):
        if lista[i].magassag>(555/3.280839895 ):
            db+=1

    return db

def legoregebb_epulet(lista):
    max_index=0
    for i in range(0,len(lista),1):
        #összehasonlítom az aktuális elemet és az eddigi maximumot
        if lista[i].epult < lista[max_index].epult:
            max_index=i
        
        return max_index
    
   
"""A legtöbb emelettel rendelkező épület neve és városa"""
def legtöbb_em(lista):
    max_index=0
    for i in range(0,len(lista),1):
        if lista[i].em_szam > lista[max_index].em_szam:
            max_index=i
        
        return max_index



