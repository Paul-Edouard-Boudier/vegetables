from tkinter import *
from tkinter import ttk

import functions as f

class GuiVegetables(object):
    def __init__(self, parent, mainframe):
        """
        constructor, set up all the label and dynamic display
        """
        self.root = parent
        self.frame = mainframe
        self.filepath = '/home/pi/Desktop/Associations.ods'
        
        self.vege = f.export.vegetables(self.filepath)
        self.vege_names = sorted(self.vege, key = str.lower)

        self.root.title("Légumes")
        
        self.__createListbox()
        self.__createLabels()
        self.__placeLabels()
        self.good_a = self.bad_a = self.h_shelter = self.h_ground = []
        
        self.__lbox.bind('<<ListboxSelect>>', self.showVegetableInfos)
        
        
    def __createListbox(self):
        """
        Create the listbox that will hold our list of vegetables for our user
        """   
        names = StringVar(value=self.vege_names)
        self.__lbox = Listbox(self.frame, listvariable=names, height=8)
    
    
    def __createLabels(self):
        """
        Create the labels we need for our somewhat dynamic part of the gui
        """
        self.__good_a_label = ttk.Label(self.frame, text="Va bien avec : ")
        self.__bad_a_label = ttk.Label(self.frame, text="Va pas bien avec :")
        
        self.__seed_label = ttk.Label(self.frame, text="Se plante :")
        self.__h_ground_label = ttk.Label(self.frame, text="sous terre en")
        self.__h_shelter_label = ttk.Label(self.frame, text="sous abris en")
        
        self.__list_label = ttk.Label(self.frame, text="légumes")
        
        
    def __placeLabels(self):
        """
        Place our labels how we want it on our somewhat dynamic part of the gui
        """
        self.__good_a_label.grid(column=0, row=2, sticky=W)
        self.__bad_a_label.grid(column=2, row=2, sticky=W)
        
        self.__seed_label.grid(column=0, row=5, sticky=W)
        self.__h_ground_label.grid(column=0, row=6, sticky=W)
        self.__h_shelter_label.grid(column=2, row=6, sticky=W)
        
        self.__list_label.grid(column=0, row=0, sticky=(E,W))
        self.__lbox.grid(column=0, row=1, sticky=W)
        
        
    def showVegetableInfos(self, *args):
        """
        Change the layout of the dynamic gui given what the user selected
        
        ----- PARAMS -----
        lbox :        object
                tkinter listselector
        """
        
        id = self.__lbox.curselection()
        
        if len(id)==1:
            id = int(id[0])
            name = self.vege_names[id]
            infos = self.vege[name]
            self.reset_display()
            self.change_display(infos)
            
    def reset_display(self):
        """
        reset labels of gui because everything is on top of each other it's messy
        """
        
            
    def change_display(self, infos: dict):
        """
        call two functions that will change the  display of the gui
        
        ----- PARAMS -----
        infos :             dict
                holds every informations about the vegetables the user chose
                    ex: 'semis': {'sa': ['Février', 'Mars', 'Avril'], 'pt': []},
                        'good': ['Carotte', 'Haricot', 'Laitue',
                                'Piment', 'Poivron', 'Radis '],
                        'bad': ['P.de terre']}
        """
        #new_row = (lambda x : max(x))([len(infos['good']), len(infos['bad'])])
        #or better yet and without lambda because it is useless here :
        new_row = max([len(infos['good']), len(infos['bad'])])
        
        self.__change_associations(infos['good'], infos['bad'])
        self.__change_harvest(infos['semis'], new_row)
        
    
    def __change_associations(self, good, bad):
        """
        """
        for i in range(len(good)):
            l = ttk.Label(self.frame, text=good[i])
            l.grid(column=1, row=2+i, sticky=W)
        
        for i in range(len(bad)):
            l = ttk.Label(self.frame, text=bad[i])
            l.grid(column=3, row=2+i, sticky=W)
                    
    def __change_harvest(self, harvest, new_row):
        """
        self.__seed_label.grid(column=0, row=5, sticky=W)
        self.__h_ground_label.grid(column=0, row=6, sticky=W)
        self.__h_shelter_label.grid(column=2, row=6, sticky=W)
        """
        self.__seed_label.grid(column=0, row=5+new_row, sticky=W)
        self.__h_ground_label.grid(column=0, row=6+new_row, sticky=W)
        self.__h_shelter_label.grid(column=2, row=6+new_row, sticky=W)
        
        for i in range(len(harvest['pt'])):
            l = ttk.Label(self.frame, text=harvest['pt'][i])
            l.grid(column=1, row=6+new_row+i, sticky=E)
        
        for i in range(len(harvest['sa'])):
            l = ttk.Label(self.frame, text=harvest['sa'][i])
            l.grid(column=3, row=6+new_row+i, sticky=E)