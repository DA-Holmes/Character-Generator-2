'''
This class is designed to create and assign character statistics.
'''

import random
import os
direct = os.getcwd()
# from RaceBuilder_New import *
# from ClassBuilder import *
# rb = RaceBuilder()
# cb = ClassBuilder()

class StatBuilder:
    
    #Default stats, stat names, and stat bonuses
    def __init__(self):
        self.default_values = [8,10,12,13,14,15]
        self.values = self.default_values
        self.abrevs_list = ['STR','DEX','CON','INT','WIS','CHA']
        self.full_list = ['Strength','Dexterity','Constitution','Intelligence','Wisdom','Charisma']
        self.boost_list = [0,0,0,0,0,0]
        self.assigned_list = []
        
        file1 = open(direct + "\\Program Tools\\Program Data\\Class_Stat_Priorities.txt", 'r')
        file2 = open(direct + "\\Program Tools\\Program Data\\Race_Main_Boosts.txt", 'r')
        file3 = open(direct + "\\Program Tools\\Program Data\\Race_Subs_Boosts.txt", 'r')
        
        self.all_pri = []
        for line in file1:
            self.all_pri.append(line.strip().split(';'))
        self.all_pri.remove(self.all_pri[0])
        
        self.main_boosts = []
        for line in file2:
            self.main_boosts.append(line.strip().split(';'))
        
        self.sub_boosts = []
        for line in file3:
            self.sub_boosts.append(line.strip().split(';'))
        
        
        
    def set_data(self, ch_class, race, subrace='NA'):
#         self.ch_class = ch_class
#         self.race = race
#         self.subrace = subrace
        
        for entry in self.all_pri:
            if entry[0] == ch_class:
                self.priorities = entry
                
                self.prims = self.priorities[1].split(',')
                self.secs = self.priorities[2].split(',')                
        
        for entry in self.main_boosts:
            if entry[0] == race:
                self.boosts = entry[1].split(',')
        
        if subrace != 'NA':
            for entry in self.sub_boosts:
                if entry[0] == subrace:
                    self.subs = entry[1].split(',')
            
            for i in range(6):
                self.boosts[i] = int(self.boosts[i]) + int(self.subs[i])
            
                
    
    

        
    
    #For each stat, roll 4 six-sided dice and subtract the smallest from the sum 
    def roll_stats(self):
        
        stats_rolled = []
        for i in range(6):            
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            die3 = random.randint(1,6)
            die4 = random.randint(1,6)
            lowest = min(die1, die2, die3, die4)
            total = die1 + die2 + die3 + die4 - lowest
            stats_rolled.append(total)
        
        #Make a list of the rolled stats
        self.values = stats_rolled


    
    
    def auto_assign(self):
        print("full auto, baby")
        
    
    
    
    
    #Automate assignment for randomization
    def assign_stats_auto(self, main):
        self.assigned_list = [0,0,0,0,0,0]
        remaining = 6
        
        #Set main stat as highest
        for stat in self.ordered_list:
            if stat == main:
                main_index = self.ordered_list.index(stat)
                highest = max(self.stat_values)
                self.assigned_list[main_index] = highest
                self.stat_values.remove(highest)
                remaining -= 1
        
        #CON is always good
        if main != 'CON':
            highest = max(self.stat_values)
            self.assigned_list[2] = highest
            self.stat_values.remove(highest)
            remaining -= 1

        #Others
        #get indeces of unassigned stats
        remaining_indeces_list = []
        for i in range(6):
            if self.assigned_list[i] == 0:
                remaining_indeces_list.append(i)
                
        #Assign at random based on indeces
        while remaining > 0:
            highest = max(self.stat_values)
            index = random.choice(remaining_indeces_list)
            self.assigned_list[index] = highest
            self.stat_values.remove(highest)
            remaining_indeces_list.remove(index)
            remaining -= 1
    