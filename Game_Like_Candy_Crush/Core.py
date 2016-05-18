# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:24:35 2015

@author: danconstantini
"""


import sys, random, math, string


# Number of lines in the grid.
N = 7

class Printable:
    def print(self):
        print(self)


class Grid(Printable):
    def __init__(self):
        self.Game_Grid = [[random.randint(0,N-1) for x in range(N)] for x in range(N)]
        self.Initialize_Grid()
        self.Current_Case = [0,0]
        self.visited = [[0 for x in range(N)] for x in range(N)]
        self.count = 0
        self.temp_u_case = [0,0] # upper case of the whole selected block.
        self.temp_l_case = [0,0] # lefter case of the whole selected block.
        self.Score = 0
        self.Moves = 0
        
    def __str__(self):
        string = ""
        for i in range(N):
            string = string + "\n" + str(self.Game_Grid[i])
        return string
    
    def __repr__(self):
        print(self.__str__())
    
    def set_case(self, number, coord):
        self.Game_Grid[coord[0]][coord[1]] = number
            

    def Exchange(self, coord1, coord2):
        if (abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]) == 1):
            temp = self.Game_Grid[coord1[0]][coord1[1]]
            self.Game_Grid[coord1[0]][coord1[1]] = self.Game_Grid[coord2[0]][coord2[1]]
            self.Game_Grid[coord2[0]][coord2[1]] = temp
            # We test the grid for possible alignments.
            flag = False
            while not flag:
                flag = True
                for i in range(N):
                    for j in range(N):
                        self.Current_Case = [i,j]
                        self.Play_V([i,j], flag)
                        self.Play_H([i,j], flag)
                        

    # Reset the visited array.
    def set_visited(self):
        self.visited = [[0 for x in range(N)] for x in range(N)]
        
    def set_Current_Case(self, i, j):
        self.Current_Case = [i,j]
    
    # Perform a flood algorithm. It finds all the blocks with the same number.
    def Flood_Horizontally(self, coord):
        if ((coord[0] < 0 or coord[0] > (N-1) or coord[1] < 0 or coord[1] > (N-1))
        or (self.visited[coord[0]][coord[1]] == 1) or not 
            (self.Game_Grid[self.Current_Case[0]][self.Current_Case[1]] 
             == self.Game_Grid[coord[0]][coord[1]])) :
            return
        else: 
            self.visited[coord[0]][coord[1]] = 1
            self.count += 1 
            self.Flood_Horizontally([coord[0], coord[1]-1])
            self.Flood_Horizontally([coord[0], coord[1]+1])
            
    def Flood_Vertically(self, coord):
        if ((coord[0] < 0 or coord[0] > (N-1) or coord[1] < 0 or coord[1] > (N-1))
        or (self.visited[coord[0]][coord[1]] == 1) or not 
            (self.Game_Grid[self.Current_Case[0]][self.Current_Case[1]] 
             == self.Game_Grid[coord[0]][coord[1]])) :
            return
        else: 
            self.visited[coord[0]][coord[1]] = 1
            self.count += 1 
            self.Flood_Vertically([coord[0]-1, coord[1]])
            self.Flood_Vertically([coord[0]+1, coord[1]])
    
    def Find_Upper_Case(self):
        k = 0
        self.temp_u_case[1] = self.Current_Case[1]
        self.temp_u_case[0] = self.Current_Case[0]
        while (k >= 0 and k < N and 
               self.visited[self.Current_Case[0]-(k+1)][self.Current_Case[1]] == 1):
            self.temp_u_case[0] -= 1
            k += 1
            
    def Fall_Vertically(self):
        if not (self.temp_u_case[0] == 0):
            for k in range(self.temp_u_case[0]):
                self.set_case(self.Game_Grid[k][self.temp_u_case[1]],
                              [self.count + k, self.Current_Case[1]])
        for k in range(self.count):
            self.set_case(random.randint(0,N-1), [k, self.temp_u_case[1]])
            
    # Tries for vertical alignments.
    def Play_V(self, coord, flag):
        self.count = 0
        self.temp_u_case = [0,0]
        self.set_visited()
        self.Flood_Vertically(coord)
        if self.count >= 3:
            self.Score += 10
            self.Find_Upper_Case()
            self.Fall_Vertically()
            flag = False
            
    
    def Find_Lefter_Case(self):
        k = 0
        self.temp_l_case[1] = self.Current_Case[1]
        self.temp_l_case[0] = self.Current_Case[0]
        while (k >= 0 and k < N and 
               self.visited[self.Current_Case[0]][self.Current_Case[1]-(k+1)] == 1):
            self.temp_l_case[1] -= 1
            k += 1
       
    def Fall_Horizontally(self):
        if not (self.temp_l_case[0] == 0):
            for k in range(self.temp_l_case[0]):
                temp1 = (self.Game_Grid[self.temp_l_case[0]-(k+1)]
                         [self.temp_l_case[1]:(self.temp_l_case[1] + self.count)])
                (self.Game_Grid[self.temp_l_case[0]-k]
                 [self.temp_l_case[1]:(self.temp_l_case[1] + self.count)]) = temp1
        for k in range(self.count):
            self.set_case(random.randint(0,N-1), [0, self.temp_l_case[1] + k])
            
    # Tries for horizontal alignments.
    def Play_H(self, coord, flag):
        self.count = 0
        self.temp_l_case = [0,0]
        self.set_visited()
        self.Flood_Horizontally(coord)
        if self.count >= 3:
            self.Score += 10
            self.Find_Lefter_Case()
            self.Fall_Horizontally()
            flag = False
    
    # We initialize a grid that does not contain 3 elements in the same line.
    def Initialize_Grid(self):
        flag = False
        while not flag:
            flag = True
            for i in range(N):
                for j in range(N):
                    self.Current_Case = [i, j]
                    self.count = 0
                    self.temp_l_case = [0,0]
                    self.set_visited()
                    self.Flood_Horizontally(self.Current_Case)
                    if self.count >= 3:
                        self.Game_Grid = [[random.randint(0,N-1) for x in range(N)]
                                          for x in range(N)]
                        flag = False
                    self.count = 0
                    self.temp_u_case = [0,0]
                    self.set_visited()
                    self.Flood_Vertically(self.Current_Case)
                    if self.count >= 3:
                        self.Game_Grid = [[random.randint(0,N-1) for x in range(N)]
                                          for x in range(N)]
                        flag = False
                    
                    



