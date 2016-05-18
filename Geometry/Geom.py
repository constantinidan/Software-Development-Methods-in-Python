
# -*- coding: utf-8 -*-

# CONSTANTINI Dan


import sys

import math

class point:
    def __init__(self, x0, y0):
        self.x = x0
        self.y = y0
    def __eq__(self, point):
        if self.x == point.x and self.y == point.y:
            return True
        else:
            return False
        
    def translation(self, dx, dy):
        self.x += dx
        self.y += dy
    def translation2(self, dx, dy):
        point_translate = point(0, 0)
        point_translate.x = self.x + dx
        point_translate.y = self.y +dy
        return point_translate
    def to_string(self):
        string = ""
        string = str(self.x) + " " + str(self.y) + " "
        return string
    def affiche(self):
        print(self.to_string())
        
        
class disque(point):                       # Translation method called in point
    def __init__(self, Centrex, Centrey, R):
        super().__init__(Centrex, Centrey)
        self.rayon = R
        if self.rayon < sys.float_info.epsilon:
            print("The disk must not be reduced to a point.")
    def perimetre(self):
        print(2*3.14*self.rayon)
    def to_string(self):
        return "DISQUE " + super().to_string() + str(self.rayon)
    def affiche(self):
        print(self.to_string())
    def test_si_point_dans_disque(self, point_a_tester):
        if (self.rayon - distance(point(self.x, self.y), point_a_tester) 
        >= 0):
            print("(" + str(point_a_tester.x) + "," + str(point_a_tester.y) + 
                    ") is inside the " + self.to_string() )
        else:
            print("(" + str(point_a_tester.x) + "," + str(point_a_tester.y) + 
                    ") is outside the " + self.to_string() )
    

def distance(point1, point2):
    return math.sqrt(((point2.x-point1.x)**2 + (point2.y-point1.y)**2))


def calcul_point_dintersection(droite1_point1, droite1_point2, droite2_point1,
                       droite2_point2, i):
    # Soient v et u les vecteurs directeurs des deux droites.
    v1 = (droite1_point2.x - droite1_point1.x)
    v2 = (droite1_point2.y - droite1_point1.y)  
    u1 = (droite2_point2.x - droite2_point1.x)
    u2 = (droite2_point2.y - droite2_point1.y)
    Det = (v2*(-u1)) - ((-v1)*u2)
    Booleen = True
    if abs(Det) <= sys.float_info.epsilon:
        string = ("The lines are parallel. number :" + str(i))     
        print(string)
        return Booleen
    
    else:
        intersectionx = (((v2*droite1_point1.x - v1*droite1_point1.y)*(-u1)) - 
        ((u2*droite2_point1.x - u1*droite2_point1.y)*(-v1)))/Det
        intersectiony = ((v2*(u2*droite2_point1.x - u1*droite2_point1.y)) - 
        (v2*droite1_point1.x - v1*droite1_point1.y)*(u2))/Det
        Point_dintertection = point(intersectionx, intersectiony)
        return Point_dintertection

def three_points_are_aligned(A, B, C):
    if (abs(((B.y - A.y)*(C.x - B.x) - (C.y - B.y)*(B.x - A.x))) <= 
        sys.float_info.epsilon):
        return True
    else:
        return False
        
def point_contained_in_line(point1, point1_ligne, point2_ligne):
    if (three_points_are_aligned(point1, point1_ligne, point2_ligne) == True 
    and (point1.x <= max(point1_ligne.x, point2_ligne.x) and 
    point1.x >= min(point1_ligne.x, point2_ligne.x)) and
    (point1.y <= max(point1_ligne.y, point2_ligne.y) and 
    point1.y >= min(point1_ligne.y, point2_ligne.y))):
        return True

class triangle:
    def __init__(self, L):
        self.A = point(L[0], L[1])
        self.B = point(L[2], L[3])
        self.C = point(L[4], L[5])
        if (self.A == self.B) and (self.A == self.C):
            print("The three points coincide.")
        if (self.A == self.B) or (self.A == self.C) or (self.B == self.C):
            print("Two points coincide.")
        if three_points_are_aligned(self.A, self.B, self.C) == True:
            print("The points are aligned.")
            
    def translation(self, dx, dy):
        self.A.translation(dx, dy)
        self.B.translation(dx, dy)
        self.C.translation(dx, dy)
    def perimetre(self):
        return (distance(self.A, self.B) + distance(self.B, self.C) +
        distance(self.C, self.A))
        
    def to_string(self):
        return ("TRIANGLE " + self.A.to_string() + " " + self.B.to_string() 
        + " " + self.C.to_string())
    def affiche(self):
        print(self.to_string())

    

    
class polygon:
    def __init__(self, L):
        if len(L) < 5:
            print("Un polygone doit avoir au moins trois sommets.")
        elif len(L)%2 == 1:
            print("Vérifier le nombre de coordonées.")
        else : 
            self.Array_Point=[]
            for i in range(len(L)//2):   
                self.Array_Point.append(point(L[2*i], L[2*i+1]))
                 
    def translation(self, dx, dy):
        for i in range(len(self.Array_Point)):   
            self.Array_Point[i].translation(dx, dy)
    def perimetre(self):
        SUM = 0        
        for i in range(len(self.Array_Point) - 1):   
            SUM += distance(self.Array_Point[i], self.Array_Point[i+1])
        SUM += distance(self.Array_Point[len(self.Array_Point)-1],
                                         self.Array_Point[0])
        return SUM
    def to_string(self):                    
    # Il est plus simple de considérer le triangle comme un polygone.
        if len(self.Array_Point) == 3:
            string = "TRIANGLE "
            for i in range(len(self.Array_Point)):   
                string += self.Array_Point[i].to_string()
            return string
        else:
            string = "POLYGON "
            for i in range(len(self.Array_Point)):   
                string += self.Array_Point[i].to_string()
            return string
    def affiche(self):
        print(self.to_string())
        
    def test_si_point_dans_polygon(self, Point_a_tester):
        Points_dintersection = []
        Point_translate = Point_a_tester.translation2(1,1) 
        # La translation est choisie arbitrairement.
        Test = True
        # On teste si le point appartient à un des cotés du polygone.
        for i in range(len(self.Array_Point)-2):
            if point_contained_in_line(Point_a_tester,
                                    self.Array_Point[i], 
                                    self.Array_Point[i+1]) == True:
                Test = False
        if point_contained_in_line(Point_a_tester, 
                                self.Array_Point[len(self.Array_Point)-1], 
                                self.Array_Point[0]) == True:
            Test = False
            
        if Test == False:
            print("(" + str(Point_a_tester.x) + "," + str(Point_a_tester.y) + 
                    ") is inside the " + self.to_string() )
        # Cas ou le point n'appartient pas aux cotés du polygone.
        else: 
            for i in range(len(self.Array_Point)-2):
                temp = calcul_point_dintersection(Point_a_tester, 
                                                  Point_translate,
                                            self.Array_Point[i], 
                                            self.Array_Point[i+1], i)
                if (isinstance(temp, bool) == False):
                    if (point_contained_in_line(temp,
                                            self.Array_Point[i], 
                                            self.Array_Point[i+1]) and
                                            (temp.y >= Point_a_tester.y and
                                            temp.x >= Point_a_tester.x)):
                        Points_dintersection.append(temp)
            # Dernier point 
            temp = calcul_point_dintersection(Point_a_tester, 
                    Point_translate, self.Array_Point[len(self.Array_Point)-1],
                    self.Array_Point[0], len(self.Array_Point)-1) 
            if (isinstance(temp, bool) == False):
                if (point_contained_in_line(temp, 
                self.Array_Point[len(self.Array_Point)-1], self.Array_Point[0]) 
                and (temp.y >= Point_a_tester.y and 
                temp.x >= Point_a_tester.x)):
                    Points_dintersection.append(temp)
                
            if len(Points_dintersection)%2 == 1:  
                print("(" + str(Point_a_tester.x) + "," + str(Point_a_tester.y)
                + ") is inside the " + self.to_string() )
            else:
                print("(" + str(Point_a_tester.x) + "," + str(Point_a_tester.y)
                + ") is outside the " + self.to_string() )
            
        





"/Users/danconstantini/Documents/IMI/TDLOG/7Oct/test.txt"
# Bien mettre un espace à la fin d'une ligne de numéro.

def lecture_fichier_et_tester_point(chemin):
    fichier = open(chemin, "r")
    liste_de_polygon = []
    liste_de_triangle = []
    liste_de_disque = []
    for line in fichier:      
        if ("POLYGON" in line):
            
            liste_de_coords =  [float(entier) for entier in line.split() 
                                if entier.isdigit()]
            print(liste_de_coords)
            if(len(liste_de_coords) %2 == 1):
                print("Le polygone n'a pas le bon nombre de coordonnées.")
            else:
                liste_de_polygon.append(polygon(liste_de_coords))
                
        if ("DISQUE" in line):
            
            liste_de_coords =  [float(entier) for entier in line.split() 
                                if entier.isdigit()]
            print(liste_de_coords)
            if (len(liste_de_coords) != 3):
                print("Vérifier le nombre de coords pour DISQUE.")
            else:            
                liste_de_disque.append(disque(liste_de_coords[0], 
                                              liste_de_coords[1], 
                                              liste_de_coords[2]))
        if ("TRIANGLE" in line):
            
            liste_de_coords =  [float(entier) for entier in line.split() 
                                if entier.isdigit()]
            print(liste_de_coords)
            if (len(liste_de_coords) != 6):
                print("Vérifier le nombre de coords pour TRIANGLE.")
            else:            
                liste_de_triangle.append(polygon(liste_de_coords)) 
                
        if ("POINT" in line):
            liste_de_coords =  [float(entier) for entier in line.split() 
                                if entier.isdigit()]
            print(liste_de_coords)
            if (len(liste_de_coords) != 2):
                print("Vérifier le nombre de coords pour POINT.")
            else:            
                point_a_tester = point(liste_de_coords[0], liste_de_coords[1])   

    for i in range(len(liste_de_polygon)):
        liste_de_polygon[i].test_si_point_dans_polygon(point_a_tester)
    for i in range(len(liste_de_disque)):
        liste_de_disque[i].test_si_point_dans_disque(point_a_tester)
    for i in range(len(liste_de_triangle)):
        liste_de_triangle[i].test_si_point_dans_polygon(point_a_tester)            
                       
        
# J'ai un problème dans mon code. Lorsque je forme un polygone:
#        pol= polygon([0,0,0,1,1,1,1,0]
# Je teste : pol.test_si_point_dans_polygon(point(0.8,0.5)
# Ce point est dehors mais en testant d'autres points,
# pol.test_si_point_dans_polygon(point(0.5,0.5), le code marche.
# Il semble que ce problème apparait lorsque l'abscisse du point à tester est 
# grand. Cependant, les points sur les côtés sont bien reconnus comme faisant
# parti du polygone.
        
