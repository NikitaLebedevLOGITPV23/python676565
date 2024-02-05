nimed=["Mati","Kati","Mati","Kati","Kadri"]
while True:
    valik=input("Andmete lisamine-add\nAndmete näitamine-show\nAndmete kustutamine-del\nJärjendi pööramine-rev\nAndmete kustutamine-clear\nAndmete sortamine-sort\nAndmete otsing-ots\n")
    if valik=="add":
        valik=input("Kas lisame mitu inimest(mitu) või positsioonile(pos)")
        if valik=="mitu":
            mitu=int(input("Mitu inimest lisame?"))
            for i in range(mitu):
                nimi=input("Sisesta nimi: ")
                nimed.append(nimi)
        else:
            indeks=int(input("Kuhu lisamine? "))
            nimi=input("Mis nimi: ")
            nimed.insert(indeks-1,nimi)
    elif valik=="del":
        valik=input("Kas kustutamine nimi või indeksu järgi (ind)?")
        if valik=="nimi":
            nimi=input("Mis nimi on vaja kustutada? ")
            kogus=nimed.count(nimi)
            if kogus>0:
                for i in range(kogus):
                    nimed.remove(nimi)
            else:
                print(f"Nimi {nimi} ei ole nimekirjas")
        else:
            indeks=int(input("Mis on järjekorranumber"))
            nimed.pop(indeks-1) 
    elif valik=="show":
        print(nimed)
    elif valik=="rev": #Разворачивает список
        print(nimed.reverse())
    elif valik=="sort": #list.sort([key = функция]) Сортирует список на основе функции
        print(nimed.sort())
    elif valik=="clear": #Очищает список
        print(nimed.clear())
    elif valik=="ots":
        ind=-1
        nimi=input("Mis nime otsime? ")
        if nimed.count(nimi)>0:
            for nim in nimed:
                if nim==nimi:
                    ind=nimed.index(nimi,ind+1)
                    print(f"{nimi} on indeksiga {ind}")
        else:
            print(f"{nimi} ei ole nimekirjas")