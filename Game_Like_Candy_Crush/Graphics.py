# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:24:35 2015

@author: danconstantini
"""
import sys
from PyQt4 import QtGui, QtCore

import TP3_CONSTANTINI_DAN as m

class Display_Grid(QtGui.QWidget):
    
    def __init__(self):
        self.G = m.Grid()
        super(Display_Grid, self).__init__()
        self.grid_Button = [[QtGui.QPushButton(str(self.G.Game_Grid[i][j]))
                             for i in range(m.N)] for j in range(m.N)]
        self.liste = []
        self.G.print()
        self.initUI()

    
    def refresh(self):
        self.G.print()
        for i in range(m.N):
            for j in range(m.N):
                self.grid_Button[i][j].setText(str(self.G.Game_Grid[i][j]))
        
    def initUI(self):
        
        grid_layout = QtGui.QGridLayout()
        self.setLayout(grid_layout) 
        
        for i in range(m.N):
            for j in range(m.N):
                grid_layout.addWidget(self.grid_Button[i][j], i, j)
                self.grid_Button[i][j].value = (i,j)
                self.grid_Button[i][j].clicked.connect(self.get_coord)
            
        # Score
        score = QtGui.QLabel('<b>' + 'Score' + '</b>', self)
        self.scoreLabel = QtGui.QLabel(str(self.G.Score),self)
        grid_layout.addWidget(score)
        grid_layout.addWidget(self.scoreLabel)


        # Moves
        Moves = QtGui.QLabel('<b>' + 'Moves' + '</b>', self)
        self.movesLabel = QtGui.QLabel(str(self.G.Moves),self)
        grid_layout.addWidget(Moves)
        grid_layout.addWidget(self.movesLabel)
        
        # Quit button
        self.btn_reset = QtGui.QPushButton('Exit', self)
        self.btn_reset.move(280, 250)
        self.btn_reset.setFixedSize(50, 30)
        self.btn_reset.clicked.connect(self.close) 
        
        
        self.move(900, 600)
        self.setWindowTitle('Merge3')
        self.show()
        
    def Exchange(self):
        self.G.Exchange(self.liste[0], self.liste[1])
        self.refresh()
        
    def get_coord(self):
        sender = self.sender()
        temp = sender.value
        if len(self.liste) == 0:
            self.liste.append(temp)
        elif len(self.liste) == 1:
            self.liste.append(temp)
            print(self.liste)
            self.Exchange()
            self.liste = []
  



        
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Display_Grid()
    sys.exit(app.exec_())
    
    
main()
    