import unittest, random, sys, os, qc, string

N = 10


class tasBinaire():
	def __init__(self):
		self.tas = []

	def insertion(self, value):
		self.tas.append(value)
		idx = len(self.tas) - 1
		while (idx != 0  and self.tas[idx] > self.tas[int(idx/2)]):
			temp = self.tas[idx]
			self.tas[idx] = self.tas[int(idx/2)]
			self.tas[int(idx/2)] = temp
			idx = int(idx/2)

	def __repr__(self):
		print(self.tas)




class CasDeTest(unittest.TestCase):
	def test_un(self):
		A = tasBinaire()
		for i in range(100):
			A.insertion(random.randint(0, 200))
		print(A.tas)
		self.assertEqual(max(A.tas), A.tas[0])
	def test_deux(self):
		B = tasBinaire()
		for i in range(100):
			B.insertion(random.randint(-100, 100))
		print(B.tas)
		self.assertEqual(max(B.tas), B.tas[0])



# Le module qc ne comporte pas d'attributs forall. J'ai du installer le 
# mauvais package qc.
# @qc.forall(tries = 100, x = [qc.floats() for i in range(100)])


class FilePriorite():
	def __init__(self, chemin):
		self.fichier = open(chemin, "r")
		self.dico = dict()
		self.T = tasBinaire()

	def lireFichier(self):
		liste = []
		for line in self.fichier:
			if (": " in line):
				temp = [s for s in line.split(": ")]
				if (temp[0].isdigit() or temp[0].lstrip('-').isdigit()):
					# J'associe à une key plusieurs valeurs, dans le cas ou
					# plusieurs urgences auraient la meme valeur.
					if temp[0] in self.dico:
						self.dico[int(temp[0])].append(temp[1])
					else:
						self.dico[int(temp[0])] = [temp[1]]
		#print(self.dico)

	def formeTasBinaire(self):
		[self.T.insertion(e) for e in self.dico]
		#print(T.tas)
		#print(self.dico)
		print(self.dico[self.T.tas[0]])



					
class CasDeTest2(unittest.TestCase):
	def test_un(self):
		f = open("test.txt", "a")
		for i in range(20):
			f.write(str(random.randint(-200,200)) + ": " + 
					''.join(random.choice(string.ascii_uppercase + 
						string.digits) for _ in range(N)) + "\n")
		f.close()
		F = FilePriorite("test.txt")
		F.lireFichier()
		F.formeTasBinaire()
		self.assertEqual(F.T.tas[0], max(F.T.tas))



def main():
	unittest.main()
if __name__ == '__main__':
	main()




