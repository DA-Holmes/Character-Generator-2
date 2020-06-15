# from tkinter import *
# from re import search
# import random
import os
direct = os.getcwd()

class MiscBuilder:
    def __init__(self):
        file1 = open(direct + "\\Subprograms\\Program Data\\Misc_Data.txt", 'r')

        all_data = []
        for line in file1:
            stripped = line.strip()
            data = stripped.split(':')
            all_data.append(data)

        self.standard_languages = all_data[0][1].split(',')
        self.exotic_languages   = all_data[1][1].split(',')
        self.all_skills         = all_data[2][1].split(',')
        self.simple_weapons     = all_data[3][1].split(',')
        self.artisan_tools      = all_data[4][1].split(',')
        self.instruments        = all_data[5][1].split(',')
        self.gaming_sets        = all_data[6][1].split(',')
#         print(self.lang_standard)
#         print(self.lang_exotic)





#     def set_tools(self, r_tools, sr_tools, c_tools, bg_tools):
#         self.tools = []
#         self.tool_options = []
#         for tool in r_tools:
#             if tool != 'NA':
#                 self.tools.append(tool)
#         for tool in sr_tools:
#             if tool != 'NA':# and tool not in self.tools:
#                 self.tools.append(tool)
#         for tool in c_tools:
#             if tool != 'NA':# and tool not in self.tools:
#                 self.tools.append(tool)
#         for tool in bg_tools:
#             if tool != 'NA':# and tool not in self.tools:
#                 self.tools.append(tool)
#
#
#         for tool in self.tools:
#             if tool.find("/"):
#                 self.tools.remove(tool)
#                 self.tool_options.append(tool)
# #         for tool in self.tools:
# #             if tool == "One Type of Gaming Set":
# #                 self.tools.remove(tool)
# #                 self.tool_options.append(tool)
