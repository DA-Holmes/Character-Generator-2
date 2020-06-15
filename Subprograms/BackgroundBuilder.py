import random
import os
direct = os.getcwd()

class BackgroundBuilder:
    
    def __init__(self):
        file = open(direct + "\\Program Tools\\Program Data\\Background_Data.txt", 'r')
        
        self.all_info = []
        for line in file:
            self.all_info.append(line.strip().split(';'))
        self.all_info.remove(self.all_info[0])
        
        self.bg_list = []
        for entry in self.all_info:
            self.bg_list.append(entry[0])
     
    def auto_choose(self):
        self.bg = random.choice(self.bg_list)
        self.set_data(self.bg)
        
    def set_data(self, bg):
        self.bg = bg
        for entry in self.all_info:
            if entry[0] == bg:
                my_info = entry
        
        self.skills    = my_info[1].split(',')
        self.tools     = my_info[2].split(',')
        self.languages = my_info[3].split(',')
        self.equip     = my_info[4].split('&')
        
        
    def display(self):
        print("Background features for ", self.background, ':', sep='')
        print()
        print("Skill Proficiencies: ", self.skills[0], ',', self.skills[1], sep='')
        if self.tools != 'NA':
            print("Tool Proficiencies:", end='')
            if len(self.tools) == 1:
                print(self.tools[0])
            elif len(self.tools) == 2:
                print(self.tools[0], ", ", self.tools[1], sep='')
        if self.languages == 'Any1':
            print("Languages: One of your choice")
        elif self.languages == 'Any2':
            print("Languages: Two of your choice")
        print("Equipment:")
        for item in self.equipment:
            print('-', item, sep ='')
            
               
        