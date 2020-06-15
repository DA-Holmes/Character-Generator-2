'''
Used to create race list, race description list, and to retrieve the relevant data from the chosen race/subrace

'''
import random
import os
direct = os.getcwd()

class RaceBuilder:

    def __init__(self):
        file1 = open(direct + "\\Subprograms\\Program Data\\Race_Descriptions.txt", 'r')
        file2 = open(direct + "\\Subprograms\\Program Data\\Race_Main_Data.txt", 'r')
        file3 = open(direct + "\\Subprograms\\Program Data\\Race_Subs_Data.txt", 'r')

        self.race_list = []
        self.desc_list = []
        for line in file1:
            self.desc_list.append(line.strip())
            races = line.split('[')[0].replace(' ','')
            self.race_list.append(races)


        self.main_data = []
        for line in file2:
            self.main_data.append(line.strip().split(';'))
        self.main_data.remove(self.main_data[0])

        self.sub_data = []
        for line in file3:
            self.sub_data.append(line.strip().split(';'))
        self.sub_data.remove(self.sub_data[0])


    def auto_choose(self):
        self.race = random.choice(self.race_list)
        self.set_data(self.race)
#         self.race_str = self.race

        self.get_sub_list(self.race)
        if self.subrace != 'NA':
            self.subrace = random.choice(self.sub_list)
            self.set_sub_data(self.subrace)
#             self.race_str = self.subrace + ' ' + self.race
#             print(self.subrace + ' ' + self.race)
#         else:
#             print(self.race)




    def get_sub_list(self, race):
        for i in range(len(self.main_data)):
            if race == self.main_data[i][0]:
                if self.main_data[i][1] == 'Yes':
                    self.subrace = 'TBD'

                    self.sub_list = []
                    for entry in self.sub_data:
                        name_split = entry[0].split(',')
                        if name_split[0] == race:
                            self.sub_list.append(name_split[1])
                else:
                    self.subrace = 'NA'



    # don't have subrace data yet
    def set_data(self, race):
        self.race = race
        self.race_str = self.race
        self.get_sub_list(race)
        for entry in self.main_data:
            if race == entry[0]:
                main_info = entry

        self.boosts    = main_info[2].split(',')
        age            = main_info[3].split(',')
        self.age_min   = age[0]
        self.age_max   = age[1]
        self.rec_align = main_info[4]
        rec_size       = main_info[5].split(',')
        height         = rec_size[0].split('/')
        self.ht_min    = height[0]
        self.ht_max    = height[1]
        self.weight    = rec_size[1]
        self.size      = rec_size[2]
        self.speed     = main_info[6]
        self.skill     = main_info[7]
        self.tools     = main_info[8].split(',')
        self.languages = main_info[9].split(',')
        self.armor     = main_info[10].split(',')
        self.weapons   = main_info[11].split(',')
        self.traits    = main_info[12].split('&')


    def set_sub_data(self, subrace):
        self.subrace = subrace
        self.race_str = self.subrace + ' ' + self.race
        for entry in self.sub_data:
            sub = entry[0].split(',')
            if subrace == sub[1]:
                sub_info = entry

        self.s_boosts    = sub_info[1]
        self.s_speed     = sub_info[2]
        self.s_tools     = sub_info[3].split(',')
        self.s_languages = sub_info[4].split(',')
        self.s_armor     = sub_info[5].split(',')
        self.s_weapons   = sub_info[6].split(',')
        self.s_traits    = sub_info[7].split('&')

    # for use in the shell
    def check_main_info(self):
        print("Race: ", self.race)
        print()
        print("ASI: ", end='')
        print(self.boosts)
        print("Age: " + self.age_min + " to " + self.age_max)
        print("Alignment: " + self.rec_align)
        print("Size")
        print("Height: " + self.ht_min + " to " + self.ht_max)
        print("Weight: " + self.weight)
        print("Size Class: " + self.size)
        print("Speed: " + self.speed)
        print("Skills: " + self.skills)
        print("Tools: " + self.tools)
        print("Languages: ", end='')
        print(self.languages)
        print("Armor: ", end='')
        print(self.armor)
        print("Weapons: ", end='')
        print(self.weapons)
        print("Traits: ", end='')
        print(self.traits)

    def check_sub_info(self):
        if self.subrace != 'NA':
            print("Subrace: " + self.subrace)
            print("Sub ASI: ", end='')
            print(self.s_boosts)
            print("Sub Speed: " + self.s_speed)
            print("Sub Tools: " + self.s_tools)
            print("Sub Languages: ", end='')
            print(self.s_languages)
            print("Sub Weapons: ", end='')
            print(self.s_weapons)
            print("Sub Traits: ", end='')
            print(self.s_traits)
