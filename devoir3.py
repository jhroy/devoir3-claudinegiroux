#coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

url = "https://www.pbo-dpb.gc.ca/fr/blog/news/archive/"

fichier ="rapportFinal.csv"
rapportFinal=[]
#J'ai tenté d'aller chercher les rapports sur le site du Directeur parlementaire du budget

entetes ={
    "User-Agent": "Claudine Giroux, étudiante en journalisme"
    }

annee = list(range(2012,2021))
rapportFinal.append(annee)

mois= list(range(1,13))
rapportFinal.append(mois)
#J'ai créé des listes de range pour le mois et l'année. Les archives débutent en 2012, j'ai donc débuté ma recherche en 2012

n=0

for date in annee:
    date= str(date)

    for dates in mois:
        if dates < 10:
            dates= "0" + str(dates)
        urlDuJour= url+ str(date) +"/"+str(dates)

        rapportFinal.append(urlDuJour)

        site = requests.get(urlDuJour, headers=entetes)

        # print(site.status_code)

        page = BeautifulSoup(site.text, "html.parser")

        #J'ai réussi à imprimer chacune des url des archives

        # print(page)

        print(urlDuJour)
        print()

        rapports= page.find_all("h2", class_="post-title")
        #Je veux imprimer chacune des url qui se trouve dans la section d'un mois et d'une année spécifique

        for rapport in rapports:
            print(rapport.find("a")["href"])
            #j'ai réussi à imprimer les url. Je veux ensuite imprimer la date de la publication du rapport, le résumé et ses auteurs

            dates= page.find("div", class_="date").text.strip()
            print(dates)
            rapportFinal.append(dates)

            extrait=page.find("div", class_="post-abstract").text.strip()
            print(extrait)
            rapportFinal.append(extrait)

            auteur=page.find("div", class_="author").text.strip()
            print(auteur)
            print()
            rapportFinal.append(auteur)

            #J'ai réussi à imprimer toutes les informations voulues, il me reste seulement à créer un fichier csv



        print("."*10)



        dead= open(fichier,"a")
        obies=csv.writer(dead)
        obies.writerow(rapportFinal)
