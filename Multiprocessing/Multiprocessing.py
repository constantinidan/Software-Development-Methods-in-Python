# -*- coding: utf-8 -*-

import sys, os, json
from multiprocessing import Pool
from collections import Counter


class AllFiles():
	def __init__(self):
		self.Dico = {"nom_comm": "communes", "nom_dept": "départements",
					"nom_region": "régions"}
		Dir = 'data/'
		p = Pool(4)
		listComm_temp = []
		for x, y, z in os.walk(Dir):
			for i in range(len(z)):
				listComm_temp.append(str(x) + '/' + str(z[i]))
		listComm = listComm_temp[1:]
		# The first element is data/.
		self.Files = p.map(self.Tache, listComm)


	def Tache(self, path):
		with open(path) as fichier: 
			doc = json.load(fichier)
			return doc


	def Tache2(self, i):
		return self.Files[i]["fields"]['statut']


	def statusNumber(self):
		p1 = Pool(4)
		statut = p1.map(self.Tache2, [i for i in range(len(self.Files))])
		Names = list(Counter(statut).keys())
		Numbers = list(Counter(statut).values())
		print("Il y a " + str(len(Names)) + " statuts différents.")
		for i in range(len(Names)):
			print(str(Names[i]) + " : " + str(Numbers[i]))


	### 
	# Je n'ai pas modifié cette fonction pour qu'elle marche sur 
	# plusieurs coeurs.

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

	###


	def Tache4(self, i):
		return self.Files[i[0]]["fields"][i[1]]

	def nombresMoyens(self, nom1, nom2):
		p3 = Pool(4)
		listeDeNom1 = p3.map(self.Tache4, 
							[(i, nom1) for i in range(len(self.Files))])

		Names1 = list(Counter(listeDeNom1).keys())
		p4 = Pool(4)
		listeDeNom2 = p4.map(self.Tache4, 
							[(i, nom2) for i in range(len(self.Files))])
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

### Remarque : le fichier multiprocessing prend beaucoup plus de temps que 
### le fichier normal.



