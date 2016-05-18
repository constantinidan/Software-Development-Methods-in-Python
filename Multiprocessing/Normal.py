# -*- coding: utf-8 -*-

import sys, os, json
from collections import Counter


class AllFiles():
    def __init__(self):
        self.Dico = {"nom_comm": "communes", "nom_dept": "départements",
                     "nom_region": "régions"}
        self.Files = []
        Dir = 'data/'
        for x, y, z in os.walk(Dir):
            for i in range(1,len(z)):
                with open(str(x) + '/' + str(z[i])) as fichier:
                    doc = json.load(fichier)
                    self.Files.append(doc)


    def statusNumber(self):
        statut = []
        for i in range(len(self.Files)):
            statut.append(self.Files[i]["fields"]['statut'])
        Names = list(Counter(statut).keys())
        Numbers = list(Counter(statut).values())
        print("Il y a " + str(len(Names)) + " statuts différents.")
        for i in range(len(Names)):
            print(str(Names[i]) + " : " + str(Numbers[i]))


    def population(self, nom):
        Count = Counter()
        for i in range(len(self.Files)):
            Count[self.Files[i]["fields"][nom]] += self.Files[i]["fields"][
                        "population"]
        Numbers = list(Count.values())
        Names = list(Count.keys())
        print("Le nombre d'habitants pour les " + self.Dico[nom] + " est : \n")
        for i in range(len(Names)):
            print(str(Names[i]) + " : " + str(int(Numbers[i])))


    def nombresMoyens(self, nom1, nom2):
        listeDeNom1 = []
        for i in range(len(self.Files)):
            listeDeNom1.append(self.Files[i]["fields"][nom1])
        Names1 = list(Counter(listeDeNom1).keys())
        listeDeNom2 = []
        for i in range(len(self.Files)):
            listeDeNom2.append(self.Files[i]["fields"][nom2])
        Names2 = list(Counter(listeDeNom2).keys())
        print("Le nombre moyen de " + self.Dico[nom1] +" par " +
              self.Dico[nom2] + " est : " + str(int(len(Names1)/len(Names2))))


A = AllFiles()
A.statusNumber()
A.population("nom_region")
A.population("nom_dept")
A.nombresMoyens("nom_comm", "nom_dept")
A.nombresMoyens("nom_dept", "nom_region")
A.nombresMoyens("nom_comm", "nom_region")


