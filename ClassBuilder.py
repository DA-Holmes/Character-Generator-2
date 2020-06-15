'''
Used to create class list, class description list, and to retrieve the relevant data from the chosen class
*class will be chosen in mainfile because the user will need to interact with the gui
'''
import random
import os
direct = os.getcwd()

class ClassBuilder:
    
    def __init__(self):
        file1 = open(direct + "\\Program Tools\\Program Data\\Class_Descriptions.txt", 'r')
        file2 = open(direct + "\\Program Tools\\Program Data\\Class_Data.txt", 'r')

        self.class_list = []
        self.desc_list = []
        for line in file1:
            self.desc_list.append(line.strip())
            classes = line.split('|')[0].replace(' ','')
            self.class_list.append(classes)

        self.info_list = []
        for line in file2:
            self.info_list.append(line.strip().split(';'))
    
    def auto_choose(self):
        self.ch_class = random.choice(self.class_list)
        self.set_data(self.ch_class)
#         return self.ch_class
    
    # retrieving and assigning data
    def set_data(self, ch_class):
        self.ch_class = ch_class
        for entry in self.info_list:
            if ch_class == entry[0]:
                my_info = entry

        self.prim_stat      = my_info[1]
        self.sec_stat       = my_info[2]
        self.rec_background = my_info[3]
        self.hit_die        = my_info[4]
        self.armor          = my_info[5]
        self.weapons        = my_info[6]
        self.tools          = my_info[7].split(',')
        self.save1          = my_info[8]
        self.save2          = my_info[9]
        self.num_skills     = my_info[11]
        self.skill_list     = my_info[10].split(',')
        
        self.skills_str = ''
        if self.skill_list[0] != 'Any':
            for i in range(len(self.skill_list)-1):
                self.skills_str += self.skill_list[i] + ', '
            self.skills_str += "and " + self.skill_list[len(self.skill_list)-1]
        else:
            self.skills_str = 'any'
        
        equip_raw = my_info[12].split('&')
        self.equip = []
        for item in equip_raw:
            self.equip.append(item.split('/'))
    
    # this is mostly just to make sure it's working
    def display(self):
        print("Class attributes for ", self.ch_class, ":", sep='')
        print()
        print("Primary Stat:", self.prim_stat)
        print("Secondary Stat:", self.sec_stat)
        print("Recommended Background:", self.rec_background)
        print("Hit Die:", self.hit_die)
        print()
        print("Proficiencies:")
        print("Armor:", self.armor)
        print("Weapons:", self.weapon)
        print("Tools:", self.tool)
        print()
        print("Saving Throws: ", self.save1, ", ", self.save2, sep='')
        
        if 'Any' in self.skill_list:
            print("Skills: Choose any", self.num_skills)
        else:
            print("Skills: Choose", self.num_skills, "from ", end='')
            count = len(self.skill_list) - 1
            for i in range(count-1):
                print(self.skill_list[i], ', ', sep='', end='')
            print('and ', self.skill_list[count],sep='')
                
        print()
        print("Starting Equipment:")
        for line in self.equip:
            if len(line) == 3:
                print('-(a)', line[0], ' OR (b)', line[1], ' OR (c)', line[2], sep='')
            elif len(line) == 2:
                print('-(a)', line[0], ' OR (b)', line[1], sep='')
            elif len(line) == 1:
                print('-', line[0], sep='')
