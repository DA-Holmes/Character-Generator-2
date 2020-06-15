'''
just don't choose half-elf yet...
'''

import sys
sys.path.insert(0, 'Subprograms/')

# import python tools
from tkinter import *
from functools import partial
import random


# import my modules
from RaceBuilder import *
from ClassBuilder import *
from BackgroundBuilder import *
from StatBuilder import *
from MiscBuilder import *
rb = RaceBuilder()
cb = ClassBuilder()
bb = BackgroundBuilder()
sb = StatBuilder()
mb = MiscBuilder()


class Main(Frame):

    # initialize the window
    def __init__(self, master):
        Frame.__init__(self, master)
        master.title("D&D Character Generator")
        self.master = master

        self.menu()

    # clears the whole window
    def clear(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def temp_ch_set(self):
        if self.ch_set == False:
#             rb.auto_choose()
#             cb.auto_choose()
#             bb.auto_choose()
            rb.set_data('Dwarf')
            rb.set_sub_data('Hill')
            cb.set_data('Monk')
            bb.set_data('Entertainer')
            self.ch_set = True
        print("Race:", rb.race_str)
        print("Class:", cb.ch_class)
        print("BG:", bb.bg)

    # presents the menu page that allows access to other pages
    def menu(self):
        self.clear()

        self.ch_set = False

        #can probably simplify to just one 'empty' variable
        self.r_cont_empty = True
        self.c_cont_empty = True
        self.b_cont_empty = True
        self.sr_info_empty = True
        self.r_btn_empty = True
        self.OPTIONS = [1,2,3,4,5,6]

        self.master.geometry("560x340")
#         self.master.resizable(0,0)

        # using frames to better manipulate the visualization
        title_frame = Frame(self.master)
        btn_frame = Frame(self.master)

        self.menu_title = Label(title_frame, text="The D&D Character Generator", font=("Times New Roman", 25))
        self.menu_title.pack(padx=10)
        Button(btn_frame, text="Manual Generator", width=20, command = self.race_page).pack(pady=5)
        Button(btn_frame, text="Automatic Generator", width=20, command = self.auto_page).pack(pady=5)
        Button(btn_frame, text="Dice Roller", width=20, command = self.roll_page).pack(pady=5)
        Button(btn_frame, text="Instructions", width=20, command = self.inst_page).pack(pady=5)
        Button(btn_frame, text="Other Choices Shortcut", width=20, command = self.additional_choices).pack(pady=5)
#         Button(btn_frame, text="THIS PAGE", width=20, command = self.stat_init).pack(pady=5)


        title_frame.pack(fill=BOTH)
        btn_frame.pack(fill=BOTH)

    # an instrucional page on how to use the program (currently just a placeholder)
    def inst_page(self):
        self.clear()

        Button(self.master, text="Back to Menu", command=self.menu).pack(anchor='w', padx=5, pady=15)

        frm1 = Frame(self.master)
        frm2 = Frame(self.master)

        Label(frm1, text="The world of D&D").pack(anchor='w', padx=5, pady=5)
        inst_a = Text(frm1, width=25)
        inst_a.pack(padx=5,pady=5)
        inst_a.insert('1.0',
"""Brief description of D&D.
This is how it works.""")

        inst_a.config(state=DISABLED)

        Label(frm2, text="How to use this program").pack(anchor='w', padx=5, pady=5) #might want to just create a seperate page for this, and let the user switch back and forth
        inst_b = Text(frm2, width=25)
        inst_b.pack(padx=5,pady=5)
        inst_b.insert('1.0',
"""This is how the PROGRAM works.
Easy step by step.""")

        inst_b.config(state=DISABLED)

        frm1.pack(side=LEFT, anchor='nw')
        frm2.pack(anchor='nw')



    # a dice-rolling page
    def roll_page(self):
        self.clear()
#         self.master.geometry("275x300")
        self.master.geometry("410x290")

        rl_frm1 = Frame(self.master)#, bg='red')
        rl_frm2 = Frame(self.master)#, bg='blue')
        rl_frm3 = Frame(self.master)#, bg='yellow')
        rl_frm4 = Frame(self.master)#, bg='green')

        Button(rl_frm1, text="Back to Menu", command=self.menu).grid(row=0, column=0, padx=5, pady=15)
        Label(rl_frm3, text="Start Rolling!").grid(row=0, column=0, padx=5, pady=5)
        Button(rl_frm1, text="Reset", command=self.roll_page).grid(row=0, column=1, padx=5, pady=15)

        # making the buttons
        self.dice_list = [4,6,8,10,12,20,100,1000]
        self.button_ids = []
        for i in range(8):
            if i < 4:
                button = Button(rl_frm2, text="d" + str(self.dice_list[i]), height=1, width=5, command=partial(self.roll, i))
                button.grid(row=i, column=0, sticky='w', padx=15, pady=5)
                self.button_ids.append(button)
            else:
                button = Button(rl_frm2, text="d" + str(self.dice_list[i]), height=1, width=5, command=partial(self.roll, i))
                button.grid(row=i-4, column=2, sticky='w', padx=15, pady=5)
                self.button_ids.append(button)

        # placing labels for the output
        self.label_ids = []
        for i in range(8):
            if i < 4:
                label = Label(rl_frm2, text='', width=5, bg='white', relief=RIDGE)
                label.grid(row=i, column=1)
                self.label_ids.append(label)
            else:
                label = Label(rl_frm2, text='', width=5, bg='white', relief=RIDGE)
                label.grid(row=i-4, column=3)
                self.label_ids.append(label)

        # trying to make an option to roll (x) number of (y)-sided dice
#         die_label
#         die_entry
#         num_label
#         num_entry

        #put adjustable die roller right above the log
        Label(rl_frm4, text="Roll Log").pack(anchor='w')
        self.roll_log = Text(rl_frm4, width=12, height=5)
        self.roll_log.pack()
        self.roll_log.config(state=DISABLED)


        #create log to track rolls! (maybe "forget" rather than "destroy"?)

        rl_frm1.grid(row=0, column=0, sticky='w')
        rl_frm3.grid(row=1, column=0, sticky='w')
        rl_frm2.grid(row=2, column=0, sticky='nw')
        rl_frm4.grid(row=2, column=1, sticky='nw', padx=20)



    # the rolling functionality
    def roll(self, n):
        lbl_name = self.label_ids[n]
        for k in range(len(self.dice_list)):
            if k == n:
                die = self.dice_list[k]
                roll_outcome = random.randint(1,die)
                lbl_name.configure(text = roll_outcome)
        self.roll_log.config(state='normal')
        self.roll_log.insert(END, 'd' + str(die) + ': ' + str(roll_outcome) + '\n')
        self.roll_log.config(state=DISABLED)


    # a page that automatically generates a character
    def auto_page(self):
        self.clear()
        self.master.geometry("500x500")

        # automatically choose all the information
        rb.auto_choose()
        cb.auto_choose()
        bb.auto_choose()

        self.ch_set = True


        # presenting the chosen character information
        info_frm = Frame(self.master)
        btn_frm = Frame(self.master)

        info = Text(info_frm, width=30, height=10)
        info.pack(anchor='w')
        info.insert('1.0',
                    "Character Bio:" +
                    "\n\nRace: " + rb.race_str +
                    "\nClass: " + cb.ch_class +
                    "\nBackground: " + bb.bg)
        info.config(state=DISABLED, font=('Times New Roman', 10))

        # allows to create a new character, and eventually write the bio into a text file
        Button(btn_frm, text="Back to Menu", command=self.menu).grid(row=0, column=0, padx=5, pady=15)
        Button(btn_frm, text="Create New", command=self.auto_page).grid(row=0, column=1, padx=5, pady=15)
        Button(btn_frm, text="Make bio (not yet, needs auto-stats)").grid(row=0, column=2, padx=5, pady=15)
        # write to file button

        btn_frm.pack(fill=BOTH)
        info_frm.pack(fill=BOTH)






















    def race_page(self):
        self.clear()
#         self.master.geometry("1150x545")
        self.master.geometry("800x600")
        if self.r_cont_empty == False:
            self.r_frm4.destroy()
            self.r_frm5.destroy()

        self.r_frm1 = Frame(self.master)#, bg='red')
        self.r_frm2 = Frame(self.master)#, bg='orange')
        self.r_frm3 = Frame(self.master)#, bg='yellow')



        Label(self.r_frm2, text="Races:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        v = IntVar()
        val = 0
        brow = 1
        race_radio_ids = []
        for i in range(len(rb.race_list)):
            button = Radiobutton(self.r_frm2,
                                 text=rb.race_list[i], width=10, variable=v, value=val+i, indicatoron=0,
                                 command=partial(self.race_info, i))
            button.grid(row=brow, column=0, sticky='w', padx=5, pady=3)
            race_radio_ids.append(button)
            brow += 1

        Button(self.r_frm1, text="Back to Menu", command=self.menu).grid(row=0, column=0, padx=5, pady=15)

        self.r_txt = Text(self.r_frm3, height=10, width=50)
        self.r_txt.pack(anchor='w', padx=5, pady=5)


        self.r_frm1.pack(anchor='w')
        self.r_frm2.pack(side=LEFT, anchor='nw')
#         self.r_frm3.pack(fill=BOTH, anchor='w')




    def race_info(self, k):
        if self.r_cont_empty == False:
            self.r_frm4.destroy()
            self.r_cont_empty = True
        if self.sr_info_empty == False:
            self.sr_frm1.destroy()
            self.sr_frm2.destroy()
            self.sr_info_empty = True
        if self.r_btn_empty == False:
            self.r_btn.destroy()
            self.r_btn_empty = True

        self.r_btn = Button(self.r_frm1, text="Choose a Race!", relief=SUNKEN)
        rb.set_data(rb.race_list[k])

        self.r_txt.config(state='normal')
        self.r_txt.delete('1.0', END)
        self.r_txt.insert('1.0', rb.race + " Features:") # all the class info will go in here
        self.r_txt.config(state=DISABLED)

        self.r_frm3.pack(anchor='w')

        if rb.subrace == 'NA':
            self.r_btn.config(text="Choose " + rb.race, command=self.race_confirm, relief=RAISED)
            self.r_btn.grid(row=0, column=1, padx=5, pady=15)
            self.r_btn_empty = False

        else:
            self.sr_frm1 = Frame(self.master)#, bg='green')
            self.sr_frm2 = Frame(self.master)#, bg='blue')

            self.sr_txt = Text(self.sr_frm2, height=10, width=50)
            self.sr_txt.pack(anchor='w', padx=5, pady=5)
#             self.sr_txt.insert('1.0', "Select a subrace!")
#             self.sr_txt.config(state=DISABLED)

            Label(self.sr_frm1, text="Subraces:").grid(row=0, column=0)
            v = IntVar()
            val = 0
            bcol = 0
            race_radio_ids = []
            for i in range(len(rb.sub_list)):
                button = Radiobutton(self.sr_frm1,
                                     text=rb.sub_list[i], width=10, variable=v, value=val+i, indicatoron=0,
                                     command=partial(self.subrace_info, i))
                button.grid(row=1, column=bcol+i, sticky='w', padx=5, pady=3)
                race_radio_ids.append(button)



            self.sr_frm1.pack(anchor='w')
            self.sr_info_empty = False
        self.r_btn_empty = False



    def subrace_info(self, k):
        if self.r_btn_empty == False:
            self.r_btn.destroy()
            self.r_btn_empty = True

        rb.set_sub_data(rb.sub_list[k])

        self.r_btn = Button(self.r_frm1, text="Choose " + rb.subrace + ' ' + rb.race, relief=RAISED, command=self.race_confirm)


#         self.r_btn.config(text="Choose " + rb.subrace + ' ' + rb.race, relief=RAISED, command=self.race_confirm)
        self.r_btn.grid(row=0, column=1, padx=5, pady=15, sticky='w')

        self.sr_txt.delete('1.0', END)
        self.sr_txt.insert('1.0', "Subrace: " + rb.subrace)


        self.sr_frm2.pack(anchor='w')

        self.r_btn_empty = False












    def race_confirm(self):
        self.r_frm2.destroy()
        self.r_btn.destroy()
        if rb.subrace != 'NA':
            self.sr_frm1.destroy()

        self.r_frm4 = Frame(self.master)#, bg='grey')
        self.r_frm5 = Frame(self.master)#, bg='white')

        if rb.subrace == 'NA':
            self.r_choice = Label(self.r_frm4, text="You've chosen " + rb.race + "! Continue to Class?")
        else:
            self.r_choice = Label(self.r_frm4, text="You've chosen " + rb.subrace + ' ' + rb.race + "! Continue to Class?")
        self.r_choice.pack(anchor='w')
        self.r_cont = Button(self.r_frm5, text="Continue", command=self.class_page)
        self.r_cont.grid(row=0, column=1, padx=5 ,pady=5)
        self.r_reset = Button(self.r_frm5, text="Choose Different Race", command=self.race_page)
        self.r_reset.grid(row=0, column=0, padx=5 ,pady=5)

        self.r_frm4.pack(anchor='w')
        self.r_frm5.pack(anchor='w')
        self.r_cont_empty = False






    # manually choosing a class; this page allows the user to see all the information about each class
    # before allowing them to choose one (it technically 'chooses' any class that they click on and
    # resets their choice if they click on another)
    def class_page(self):
        self.clear()
        self.master.geometry("1150x548")
        if self.c_cont_empty == False:
            self.c_frm4.destroy()
            self.c_frm5.destroy()

        self.c_frm1 = Frame(self.master)
        self.c_frm2 = Frame(self.master)
        self.c_frm3 = Frame(self.master)

        Label(self.c_frm2, text="Classes:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        v = IntVar()
        val = 0
        brow = 1
        class_radio_ids = []
        for i in range(len(cb.class_list)):
            button = Radiobutton(self.c_frm2,
                                 text=cb.class_list[i], width=10, variable=v, value=val+i, indicatoron=0,
                                 command=partial(self.class_info, i))
            button.grid(row=brow, column=0, sticky='w', padx=5, pady=3)
            class_radio_ids.append(button)
            brow += 1

        Button(self.c_frm1, text="Back to Menu", command=self.menu).grid(row=0, column=0, padx=5, pady=15)
        self.c_btn = Button(self.c_frm1, text="Choose Class", relief=SUNKEN)
        self.c_btn.grid(row=0, column=1, padx=5, pady=15)

        self.c_txt = Text(self.c_frm3, height=10, width=50)
        self.c_txt.pack(anchor='w', padx=5, pady=5)
        self.c_txt.insert('1.0', "Select a class to get started!")
        self.c_txt.config(state=DISABLED)

        self.c_frm1.pack(anchor='w')
        self.c_frm2.pack(side=LEFT, anchor='nw')
        self.c_frm3.pack(fill=BOTH, anchor='w')


    # using this to try and see what the issue is with calling the class_info function

    def class_info(self, k):
        if self.c_cont_empty == False:
            self.c_frm4.destroy()
            self.c_cont_empty = True

        cb.set_data(cb.class_list[k])

        self.c_txt.config(state='normal')
        self.c_txt.delete('1.0', END)
        self.c_txt.insert('1.0', "You selected: " + cb.ch_class) # all the class info will go in here
        self.c_txt.config(state=DISABLED)

        self.c_btn.config(text="Choose " + cb.ch_class, command=self.class_confirm, relief=RAISED)

    def class_confirm(self):

        if self.c_cont_empty == True:
            self.c_frm2.destroy()
            self.c_btn.destroy()

            self.c_frm4 = Frame(self.master)
            self.c_frm5 = Frame(self.master)

            self.c_choice = Label(self.c_frm4, text="You've chosen " + cb.ch_class + "! Continue to Background?")
            self.c_choice.pack(anchor='w')
            self.c_cont = Button(self.c_frm5, text="Continue", command=self.background_page)
            self.c_cont.grid(row=0, column=1, padx=5 ,pady=5)
            self.c_reset = Button(self.c_frm5, text="Choose Different Class", command=self.class_page)
            self.c_reset.grid(row=0, column=0, padx=5 ,pady=5)

            self.c_frm4.pack(anchor='w', fill=BOTH)
            self.c_frm5.pack(fill=BOTH)

            self.c_cont_empty = False

        elif self.c_cont_empty == False:
            self.c_choice.config(text="You've chosen " + cb.ch_class + "! Continue to Background?")







    # Backgrounds  VVVVV
    def background_page(self):
        self.clear()
        self.master.geometry("1150x585")
        if self.b_cont_empty == False:
            self.b_frm4.destroy()
            self.b_frm5.destroy()

        self.b_frm1 = Frame(self.master)
        self.b_frm2 = Frame(self.master)
        self.b_frm3 = Frame(self.master)

        Label(self.b_frm2, text="Backgrounds:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        v = IntVar()
        val = 0
        brow = 1
        bg_radio_ids = []
        for i in range(len(bb.bg_list)):
            button = Radiobutton(self.b_frm2,
                                 text=bb.bg_list[i], width=10, variable=v, value=val+i, indicatoron=0,
                                 command=partial(self.background_info, i))
            button.grid(row=brow, column=0, sticky='w', padx=5, pady=3)
            bg_radio_ids.append(button)
            brow += 1

        Button(self.b_frm1, text="Back to Menu", command=self.menu).grid(row=0, column=0, padx=5, pady=15)
        self.b_btn = Button(self.b_frm1, text="Choose Background", relief=FLAT)
        self.b_btn.grid(row=0, column=1, padx=5, pady=15)

        self.b_txt = Text(self.b_frm3, height=10, width=50)
        self.b_txt.pack(anchor='w', padx=5, pady=5)
        self.b_txt.insert('1.0', "Select a background to get started!")
        self.b_txt.config(state=DISABLED)

        self.b_frm1.pack(anchor='w')
        self.b_frm2.pack(side=LEFT, anchor='nw')
        self.b_frm3.pack(fill=BOTH, anchor='w')


    # using this to try and see what the issue is with calling the class_info function
    def background_info(self, k):
        if self.b_cont_empty == False:
            self.b_frm4.destroy()
            self.b_cont_empty = True

        bb.set_data(bb.bg_list[k])

        self.b_txt.config(state='normal')
        self.b_txt.delete('1.0', END)
        self.b_txt.insert('1.0', "You selected: " + bb.bg) # all the class info will go in here
        self.b_txt.config(state=DISABLED)

        self.b_btn.config(text="Choose " + bb.bg, command=self.background_confirm, relief=RAISED)

    def background_confirm(self):

        if self.b_cont_empty == True:
            self.b_frm2.destroy()
            self.b_btn.destroy()

            self.b_frm4 = Frame(self.master)
            self.b_frm5 = Frame(self.master)

            self.b_choice = Label(self.b_frm4, text="You've chosen " + bb.bg + "! Continue to stats?")
            self.b_choice.pack(anchor='w')
            self.b_cont = Button(self.b_frm5, text="Continue", command=self.stat_page)
            self.b_cont.grid(row=0, column=1, padx=5 ,pady=5)
            self.b_reset = Button(self.b_frm5, text="Choose Different Background", command=self.background_page)
            self.b_reset.grid(row=0, column=0, padx=5 ,pady=5)

            self.b_frm4.pack(anchor='w', fill=BOTH)
            self.b_frm5.pack(fill=BOTH)

            self.ch_set = True

            self.b_cont_empty = False



    def stat_page(self):

        # assigning automatically so i can work on this page without going through all the previous pages

        if self.ch_set == False:
            rb.auto_choose()
            cb.auto_choose()
            bb.auto_choose()
#             print("Auto-chosen race:", rb.race)
#         else:
#             print("Manually-chosen race:", rb.race)


        if rb.race == 'Half-Elf':
#             print("Got Half-Elf. Not ready yet, so re-doing auto selection.")
            self.stat_page()
            self.ch_set = False

        sb.set_data(cb.ch_class, rb.race, rb.subrace)

        self.clear()
        self.master.geometry("400x300")

        s_frm1 = Frame(self.master)
        Button(s_frm1, text="Back to Menu", command=self.menu).pack(anchor='w', padx=5, pady=15)
        Label(s_frm1, text="Ability Score Stats:").pack()
        s_frm1.pack(fill=BOTH)

        s_frm2 = Frame(self.master)
        Button(s_frm2, text="Roll for your Stats", height=3, width=15, borderwidth=5, command=lambda: self.set_stats('roll')).grid(row=0, column=0, padx=15, pady=10)
        Button(s_frm2, text="Use Default Stats", height=3, width=15, borderwidth=5, command=lambda: self.set_stats('default')).grid(row=0, column=1, padx=15, pady=10)
        s_frm2.pack()

        s_frm3 = Frame(self.master)
        Label(s_frm3, text="You can use the default ability score values (8,10,12,13,14,15) or you can roll for your own! Choose Wisely :)", wraplength=300).pack()
        s_frm3.pack()

    def set_stats(self, method):
        sb.values = sb.default_values
        if method == 'roll':
            sb.roll_stats()
        sb.values.sort()
        self.used_stats = []
        self.OPTIONS = sb.values

        self.stat_allocation()


    def stat_allocation(self):
        self.clear()
        self.master.geometry("500x560")

        while len(self.used_stats) > 0:
            for number in self.used_stats:
                self.OPTIONS.append(number)
                self.used_stats.remove(number)
        self.OPTIONS.sort()

        sa_frm1 = Frame(self.master)
        Button(sa_frm1, text="Back to Menu", command=self.menu).grid(row=0, column=0, padx=5, pady=15)
        Button(sa_frm1, text="Reallocate Stats", command=self.stat_allocation).grid(row=0, column=1, padx=5, pady=15)
        sa_frm1.pack(fill=BOTH, anchor='w')

        val_str = ''
        for i in range(5):
            val_str += str(sb.values[i]) + ', '
        val_str += str(sb.values[5])
#         print(val_str)
        Label(self.master, text="Ability Score Values: " + val_str).pack(anchor='w', padx=5)

        self.allocation_frame = Frame(self.master)
        Label(self.allocation_frame, text="Stat:").grid(row=0, column=0, padx=5)
        Label(self.allocation_frame, text="Assign Value:").grid(row=0, column=1, padx=5)
        Label(self.allocation_frame, text="Stat Bonus:").grid(row=0, column=2, padx=5)
        Label(self.allocation_frame, text="Final Score:").grid(row=0, column=3, padx=5)

#         asn_txt_ids = []
        for i in range(6):
            Label(self.allocation_frame, text=sb.abrevs_list[i], relief=GROOVE, height=2, width=5).grid(row=i+1, column=0, padx=10, pady=10)
            Label(self.allocation_frame, text=sb.boosts[i], relief=RIDGE, height=2, width=5, bg='white').grid(row=i+1, column=2, padx=10, pady=10)

        self.final_a = Label(self.allocation_frame, text="---", relief=GROOVE, height=2, width=5)
        self.final_a.grid(row=1, column=3, padx=10, pady=10)
        self.final_b = Label(self.allocation_frame, text="---", relief=GROOVE, height=2, width=5)
        self.final_b.grid(row=2, column=3, padx=10, pady=10)
        self.final_c = Label(self.allocation_frame, text="---", relief=GROOVE, height=2, width=5)
        self.final_c.grid(row=3, column=3, padx=10, pady=10)
        self.final_d = Label(self.allocation_frame, text="---", relief=GROOVE, height=2, width=5)
        self.final_d.grid(row=4, column=3, padx=10, pady=10)
        self.final_e = Label(self.allocation_frame, text="---", relief=GROOVE, height=2, width=5)
        self.final_e.grid(row=5, column=3, padx=10, pady=10)
        self.final_f = Label(self.allocation_frame, text="---", relief=GROOVE, height=2, width=5)
        self.final_f.grid(row=6, column=3, padx=10, pady=10)

        self.allocation_frame.pack(anchor='w')

        self.stat_init()


    def stat_init(self):
        self.a_set = False
        self.b_set = False
        self.c_set = False
        self.d_set = False
        self.e_set = False
        self.f_set = False

        self.var = StringVar()
        self.var.set("-select-")
        self.a = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 1))
        self.a.grid(row=1, column=1)
        self.b = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 2))
        self.b.grid(row=2, column=1)
        self.c = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 3))
        self.c.grid(row=3, column=1)
        self.d = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 4))
        self.d.grid(row=4, column=1)
        self.e = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 5))
        self.e.grid(row=5, column=1)
        self.f = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 6))
        self.f.grid(row=6, column=1)



    def this_func(self, but_num, value):
        self.OPTIONS.remove(value)
        self.used_stats.append(value)
        self.var.set("-select-")

        if len(self.used_stats) == 6:
            self.a_frame_confirm = Frame(self.master)
            Button(self.a_frame_confirm, text="Confirm Stat Allocation", command=self.additional_choices).pack(padx=5, pady=5)
            self.a_frame_confirm.pack(anchor='w')

        # setting label for the chosen button

        if but_num == 1 and self.a_set == False:
            self.a.destroy()
            Label(self.allocation_frame, text=value).grid(row=1, column=1)
            self.strength_final = text=int(value) + int(sb.boosts[0])
            self.final_a.config(text=self.strength_final)
            self.a_set = True
        elif but_num == 2 and self.b_set == False:
            self.b.destroy()
            Label(self.allocation_frame, text=value).grid(row=2, column=1)
            self.dexterity_final = text=int(value) + int(sb.boosts[1])
            self.final_b.config(text=self.dexterity_final)
            self.b_set = True
        elif but_num == 3 and self.c_set == False:
            self.c.destroy()
            Label(self.allocation_frame, text=value).grid(row=3, column=1)
            self.constitution_final = text=int(value) + int(sb.boosts[2])
            self.final_c.config(text=self.constitution_final)
            self.c_set = True
        elif but_num == 4 and self.d_set == False:
            self.d.destroy()
            Label(self.allocation_frame, text=value).grid(row=4, column=1)
            self.intelligence_final = text=int(value) + int(sb.boosts[3])
            self.final_d.config(text=self.intelligence_final)
            self.d_set = True
        elif but_num == 5 and self.e_set == False:
            self.e.destroy()
            Label(self.allocation_frame, text=value).grid(row=5, column=1)
            self.wisdom_final = text=int(value) + int(sb.boosts[4])
            self.final_e.config(text=self.wisdom_final)
            self.e_set = True
        elif but_num == 6 and self.f_set == False:
            self.f.destroy()
            Label(self.allocation_frame, text=value).grid(row=6, column=1)
            self.charisma_final = text=int(value) + int(sb.boosts[5])
            self.final_f.config(text=self.charisma_final)
            self.f_set = True

        # resetting option for unchosen option menus

        if but_num != 1 and self.a_set == False:
            self.a.destroy()
            self.a = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 1))
            self.a.grid(row=1, column=1)
        if but_num != 2 and self.b_set == False:
            self.b.destroy()
            self.b = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 2))
            self.b.grid(row=2, column=1)
        if but_num != 3 and self.c_set == False:
            self.c.destroy()
            self.c = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 3))
            self.c.grid(row=3, column=1)
        if but_num != 4 and self.d_set == False:
            self.d.destroy()
            self.d = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 4))
            self.d.grid(row=4, column=1)
        if but_num != 5 and self.e_set == False:
            self.e.destroy()
            self.e = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 5))
            self.e.grid(row=5, column=1)
        if but_num != 6 and self.f_set == False:
            self.f.destroy()
            self.f = OptionMenu(self.allocation_frame, self.var, *self.OPTIONS, command=partial(self.this_func, 6))
            self.f.grid(row=6, column=1)






















    def additional_choices(self):
        self.clear()
        self.master.geometry("800x500")
#         print("HERE")

        self.temp_ch_set()

        top_frm = Frame(self.master)
        Button(top_frm, text="Back to Menu", command=self.menu).grid(row=0, column=0, sticky='nw', padx=5, pady=15)
        Button(top_frm, text="Reset Choices", command=self.additional_choices).grid(row=0, column=1, sticky='nw', padx=5, pady=15)
        top_frm.pack(anchor='nw')
        self.skill_profs = []
#         self.RACE_SKILL_OPTIONS = []
#         self.RACE_SKILL_OPTIONS = mb.all_skills
#         print("INITIATION OF - skill_profs:        ", self.skill_profs)
#         print("INITIATION OF - RACE_SKILL_OPTIONS: ", self.RACE_SKILL_OPTIONS)
#         print()


#         self.lang_choices()
#         self.skill_choices()
        self.tool_choices()
#         self.equip_choices()















    def skill_choices(self):
#         self.skl_confirm_empty = True
#         self.skill_profs = []
#         self.RACE_SKILL_OPTIONS = mb.all_skills
#         print("Starting skill_profs:        ", self.skill_profs)
#         print("Starting RACE_SKILL_OPTIONS: ", self.RACE_SKILL_OPTIONS)
#         print()


        skill_title_frm      = Frame(self.master)
        self.race_skl_frm    = Frame(self.master)
        bg_skl_frm           = Frame(self.master)
#         class_lbl_frm        = Frame(self.master)
#         skills_frm1          = Frame(self.master)
#         skills_frm2          = Frame(self.master)
#         skills_frm3          = Frame(self.master)
#         self.skl_confirm_frm = Frame(self.master)


        Label(skill_title_frm, text="Choose Your Skill Proficiencies:").pack(padx=5, pady=5)
        skill_title_frm.pack(anchor='w')


        # BACKGROUND SKILLS

        Label(bg_skl_frm, text="From your " + bb.bg + " background, you gain proficiency in the ").grid(row=0, column=0)
        Button(bg_skl_frm, text=bb.skills[0], relief=SUNKEN).grid(row=0, column=1)
        Label(bg_skl_frm, text=" and ").grid(row=0, column=2)
        Button(bg_skl_frm, text=bb.skills[1], relief=SUNKEN).grid(row=0, column=3)
        Label(bg_skl_frm, text=" skills.").grid(row=0, column=4)

        bg_skl_frm.pack(anchor='w', padx=5)
#         print(bb.skills)
        for i in range(len(bb.skills)):
#             if skill not in self.skill_profs:
            self.skill_profs.append(bb.skills[i])
#             self.RACE_SKILL_OPTIONS.remove(bb.skills[i])
#             print("bb skill_profs:        ", self.skill_profs)
#             print("bb RACE_SKILL_OPTIONS: ", self.RACE_SKILL_OPTIONS)
#             print()







        # RACE SKILLS


#         Label(skill_title_frm, text="Choose Your Skills:").pack(padx=5, pady=5)
#         skill_title_frm.pack(anchor='w')

        if rb.skill != 'NA':
            Label(self.race_skl_frm, text="As a " + rb.race_str + ", you gain proficiency in the ").grid(row=0, column=0)
#             if rb.skills != 'Half-Elf':
            if rb.skill != 'Any2':
                Button(self.race_skl_frm, text=rb.skill, relief=SUNKEN).grid(row=0, column=1)
                Label(self.race_skl_frm, text=" skill.").grid(row=0, column=2)
#                 self.race_skl_frm.pack(anchor='w', padx=5)
                if rb.skill not in self.skill_profs:
                    self.skill_profs.append(rb.skill)
                self.class_skl_init()

            else:
                self.race_skill_choices()
#                 if self.r_skl1_set == True and self.r_skl2_set == True:
#                     self.class_skl_init()

            self.race_skl_frm.pack(anchor='w', padx=5)
        else:
            self.class_skl_init()
#         self.class_skl_init()







#         # BACKGROUND SKILLS
#
#         Label(bg_skl_frm, text="From your " + bb.bg + " background, you gain proficiency in the ").grid(row=0, column=0)
#         Button(bg_skl_frm, text=bb.skills[0], relief=SUNKEN).grid(row=0, column=1)
#         Label(bg_skl_frm, text=" and ").grid(row=0, column=2)
#         Button(bg_skl_frm, text=bb.skills[1], relief=SUNKEN).grid(row=0, column=3)
#         Label(bg_skl_frm, text=" skills.").grid(row=0, column=4)
#         bg_skl_frm.pack(anchor='w', padx=5)
#
#         for skill in bb.skills:
#             if skill not in self.skill_profs:
#                 self.skill_profs.append(skill)
# # # # #         print(self.skill_profs)




    def class_skl_init(self):
#         print("Starting class skills")
        class_lbl_frm        = Frame(self.master)
        skills_frm1          = Frame(self.master)
        skills_frm2          = Frame(self.master)
        skills_frm3          = Frame(self.master)

        # CLASS SKILLS

        Label(class_lbl_frm, text="Because you are a " + cb.ch_class + ", you may choose " + cb.num_skills + " skills from:").pack()
        class_lbl_frm.pack(anchor='w', padx=5)

        self.skl_choices_rem = int(cb.num_skills)

        self.skl_btn_ids = []
#         if cb.skill_list[0] != 'Any':
#             print("Not any skills")
        for i in range(len(cb.skill_list)):
            if i < 8:
                skl_btn = Button(skills_frm1, text=cb.skill_list[i], relief=SUNKEN, state=DISABLED)
                skl_btn.grid(row=0, column=i, padx=5, pady=5)
                self.skl_btn_ids.append(skl_btn)
                skills_frm1.pack(anchor='w', padx=5)
            elif i < 16:
                skl_btn = Button(skills_frm2, text=cb.skill_list[i], relief=SUNKEN, state=DISABLED)
                skl_btn.grid(row=0, column=i-8, padx=5, pady=5)
                self.skl_btn_ids.append(skl_btn)
                skills_frm2.pack(anchor='w', padx=5)
            else:
                skl_btn = Button(skills_frm3, text=cb.skill_list[i], relief=SUNKEN, state=DISABLED)
                skl_btn.grid(row=0, column=i-16, padx=5, pady=5)
                self.skl_btn_ids.append(skl_btn)
                skills_frm3.pack(anchor='w', padx=5)

        for j in range(len(self.skl_btn_ids)):
            skill = self.skl_btn_ids[j]['text']
            if skill not in self.skill_profs:
#                 print(skill)
                self.skl_btn_ids[j].config(relief=RAISED, state='normal', command=partial(self.choose_skill, j))











    def race_skill_choices(self):
#         self.RACE_SKILL_OPTIONS = mb.all_skills

        self.RACE_SKILL_OPTIONS = []
        for skill in mb.all_skills:
            self.RACE_SKILL_OPTIONS.append(skill)



        for skill in self.skill_profs:
#             print("Removing:", skill)
#             print("From:", self.RACE_SKILL_OPTIONS)
            self.RACE_SKILL_OPTIONS.remove(skill)

#         print("setting buttons skill_profs:        ", self.skill_profs)
#         print("setting buttons RACE_SKILL_OPTIONS: ", self.RACE_SKILL_OPTIONS)
#         for skill in self.skill_profs:
#             self.RACE_SKILL_OPTIONS.remove(skill)

        self.r_skl_var = StringVar()
        self.r_skl_var.set('pick')

        self.r_skl_opt1 = OptionMenu(self.race_skl_frm, self.r_skl_var, *self.RACE_SKILL_OPTIONS, command=partial(self.choose_r_skl, 1))
        self.r_skl_opt1.grid(row=0, column=1)
        self.r_skl1_set = False

        Label(self.race_skl_frm, text=" and ").grid(row=0, column=2)

        self.r_skl_opt2 = OptionMenu(self.race_skl_frm, self.r_skl_var, *self.RACE_SKILL_OPTIONS, command=partial(self.choose_r_skl, 2))
        self.r_skl_opt2.grid(row=0, column=3)
        self.r_skl2_set = False

        Label(self.race_skl_frm, text=" skills.").grid(row=0, column=4)



    def choose_r_skl(self, btn, skill):
        self.RACE_SKILL_OPTIONS.remove(skill)
        self.skill_profs.append(skill)
        print(skill)
#         print("chose skill skill_profs:        ", self.skill_profs)
#         print("chose skill RACE_SKILL_OPTIONS: ", self.RACE_SKILL_OPTIONS)


        self.r_skl_var.set('next race skill')
#         self.r_skl_opt1.destroy()
#         self.r_skl_opt2.destroy()
#         self.r_skl_opt1.destroy()

        print(btn)
        print(skill)

        if btn == 1:
            self.r_skl_opt1.destroy()
            self.r_skl_lbl1 = Label(self.race_skl_frm, text=skill)
            self.r_skl_lbl1.grid(row=0, column=1)
            self.r_skl1_set = True

            if self.r_skl2_set == False:
                self.r_skl_opt2.destroy()
                self.r_skl_opt2 = OptionMenu(self.race_skl_frm, self.r_skl_var, *self.RACE_SKILL_OPTIONS, command=partial(self.choose_r_skl, 2))
                self.r_skl_opt2.grid(row=0, column=3)
            else:
                self.class_skl_init()


        elif btn == 2:
            self.r_skl_opt2.destroy()
            self.r_skl_lbl2 = Label(self.race_skl_frm, text=skill)
            self.r_skl_lbl2.grid(row=0, column=3)
            self.r_skl2_set = True

            if self.r_skl1_set == False:
                self.r_skl_opt1.destroy()
                self.r_skl_opt1 = OptionMenu(self.race_skl_frm, self.r_skl_var, *self.RACE_SKILL_OPTIONS, command=partial(self.choose_r_skl, 1))
                self.r_skl_opt1.grid(row=0, column=1)
            else:
                self.class_skl_init()



#         if btn != 1 and self.r_skl1_set == False:
#             self.r_skl_opt1.destroy()
#             self.r_skl_opt1 = OptionMenu(self.race_skl_frm, self.r_skl_var, *self.RACE_SKILL_OPTIONS, command=partial(self.choose_r_skl, 1))
#             self.r_skl_opt1.grid(row=0, column=1)
#         if btn != 2 and self.r_skl2_set == False:
#             self.r_skl_opt2.destroy()
#             self.r_skl_opt2 = OptionMenu(self.race_skl_frm, self.r_skl_var, *self.RACE_SKILL_OPTIONS, command=partial(self.choose_r_skl, 2))
#             self.r_skl_opt2.grid(row=0, column=3)













    def choose_skill(self, n):
        self.skl_choices_rem -= 1
        self.skill_profs.append(self.skl_btn_ids[n]['text'])
#         print("Skill added:", self.skl_btn_ids[n]['text'])
#         print(self.skill_profs)
#         print("Can choose", self.skl_choices_rem, "more")

        self.skl_btn_ids[n].config(relief=SUNKEN, command=partial(self.unchoose_skill, n))

        if self.skl_choices_rem == 0:
            self.confirm_skills_prompt()

    def unchoose_skill(self, m):
        self.skl_choices_rem += 1
        self.skill_profs.remove(self.skl_btn_ids[m]['text'])
#         print("Skill removed:", self.skl_btn_ids[m]['text'])
#         print(self.skill_profs)
#         print("Can choose", self.skl_choices_rem, "more")

        self.skl_btn_ids[m].config(relief=RAISED, command=partial(self.choose_skill, m))

        if self.skl_confirm_empty == False:
#             self.skl_confirm_frm.destroy()

            for k in range(len(self.skl_btn_ids)):
                if self.skl_btn_ids[k]['text'] not in self.skill_profs:
#                     print(self.skl_btn_ids[k]['text'])
                    self.skl_btn_ids[k].config(state='normal')

    def confirm_skills_prompt(self):
        self.skl_confirm_empty = False

        for k in range(len(self.skl_btn_ids)):
            if self.skl_btn_ids[k]['text'] not in self.skill_profs:
                self.skl_btn_ids[k].config(state=DISABLED)




























    def tool_choices(self):
        tool_title_frm = Frame(self.master)
        Label(tool_title_frm, text="Choose Your Tool Proficiencies:").pack()
        tool_title_frm.pack(anchor='w', padx=5)

        self.tool_frm1 = Frame(self.master)
#         self.tool_frm1.pack(anchor='w')
        self.tool_frm2 = Frame(self.master)
        self.tool_frm2.pack(anchor='w')

#         Label(self.tool_frm1, text="Tool Time with Tim Taylor").pack(padx=5)

        self.tool_row_num = 0
        instrument_options = mb.instruments
        artisan_options = mb.artisan_tools

        self.tools = []
        self.tool_either_or = []
        for tool in rb.tools:
            if tool != 'NA':
                self.tools.append(tool)
        if rb.subrace != 'NA':
            for tool in rb.s_tools:
                if tool != 'NA':# and tool not in self.tools:
                    self.tools.append(tool)
        for tool in cb.tools:
            if tool != 'NA':# and tool not in self.tools:
                self.tools.append(tool)
        for tool in bb.tools:
            if tool != 'NA':# and tool not in self.tools:
                self.tools.append(tool)


        print("Tools:", self.tools)
        print()

        self.tools_either_or = []
        for tool in self.tools:
            if '/' in tool:
                self.tools_either_or.append(tool)
        for tool in self.tools_either_or:
            if tool in self.tools:
                self.tools.remove(tool)

        print("Either Or:", self.tools_either_or)
        print("Remaining Tools:", self.tools)
        print()

        self.tools_choose_type = []
        for tool in self.tools:
            if 'Type' in tool:
                self.tools_choose_type.append(tool)
                self.tools.remove(tool)
        for tool in self.tools_either_or:
            if tool in self.tools:
                self.tools.remove(tool)

        print("Choose Type:", self.tools_choose_type)
        print("Remaining Tools:", self.tools)
        print()








        # tools for either or

        self.either_or_finished = False

        while self.either_or_finished == False:
            if len(self.tools_either_or) != 0:
                for i in range(len(self.tools_either_or)):
                    self.this_one_done = False
                    self.either_func(i)

#             self.this_either_set = False
# #             while self.this_either_set == False:
#             temp_frm = Frame(self.master)
#             temp_frm.pack(anchor='w')
#             self.either_or_choices = tool.split('/')
#             for i in range(len(self.either_or_choices)):
#                 if i != len(self.either_or_choices) - 1:
#                     Button(temp_frm, text=self.either_or_choices[i], command=lambda: partial(self.tool_either_choice, i)).grid(row=self.tool_row_num, column=(i), sticky='w')
# #                     Label(temp_frm, text="OR")
#                 else:
#                     Button(temp_frm, text=self.either_or_choices[i], command=lambda: partial(self.tool_either_choice, i)).grid(row=self.tool_row_num, column=i, sticky='w')
#             self.tool_row_num += 1










        # tools with list options (make a callable function so i don't have to rewrite for above)

#         for tool in self.tools_choose_type:
#             if "Instrument" in tool:
# #                 choices = mb.instruments
#                 if "One" in tool:
#                     Label(self.tool_frm1, text=tool).grid(row=self.tool_row_num, column=0, sticky='w')
#
#                     var = StringVar()
#                     var.set("seeelect")
#                     OptionMenu(self.tool_frm1, var, *instrument_options).grid(row=self.tool_row_num, column=1)
#                     self.tool_row_num += 1
#                 elif "Three" in tool:
#                     print("three instr")
#             elif "Artisan's Tools" in tool:
#                 print("one artisan's")


        # place remaining tools

#         for tool in self.tools:
#             Label(self.tool_frm1, text=tool).grid(row=self.tool_row_num, column=0, sticky='w')
#             self.tool_row_num += 1



#         self.tool_frm1.pack(anchor='w')









    def either_func(self, k):
        self.k_complete = False
        # while self.k_complete == False:

        print(k)
        options = self.tools_either_or[k].split('/')

        #check if it's the "choose type" kind; if so, allow to choose from the dropdown, but after that, block the other option
        temp_frm = Frame(self.master)
        temp_frm.pack(anchor='w')
        for j in range(len(options)):
            print(options[j])
            btn = Button(temp_frm, text=options[j], command=lambda: partial(self.choose_either, j))
            btn.grid(row=0, column=j, padx=5, pady=5)


#         k_complete = True
        ### set this after they choose

        if k == len(self.tools_either_or)-1:
            self.either_or_finished = True
            print("done")




    def choose_either(self, n):
        print(n)
#         self.k_complete = True

    def tool_either_choice(self, n):
#         print("Choose:", value)
        print("Button:", n)
        print("Tool:", self.either_or_choices[n])
#         self.this_either_set = True




















    def lang_choices(self):

        self.lang_raw = []

        lang_lbl_frm = Frame(self.master)
        self.lang_frm = Frame(self.master)

        for entry in rb.languages:
            self.lang_raw.append(entry)
        if rb.subrace != 'NA':
            for entry in rb.s_languages:
                if entry != 'NA':
                    self.lang_raw.append(entry)
        for entry in bb.languages:
            if entry != 'NA':
                self.lang_raw.append(entry)

        self.num_lang_choices = self.lang_raw.count("Any1")

        self.languages = []
        for lang in self.lang_raw:
            if lang != 'Any1':
                self.languages.append(lang)
        self.num_lang = len(self.languages)

        if self.num_lang_choices > 0:

#         print("init  : ", self.lang_raw)
#         print("fin   : ", self.languages)
#         print("CHOOSE: ", self.num_lang_choices)
#         print()



            Label(lang_lbl_frm, text="Choose Your Language Proficiencies:").pack()
            lang_lbl_frm.pack(anchor='w')

            Label(self.lang_frm, text="You know how to speak, read, and write :").grid(row=0, column=0)

    #         self.num_lang = len(self.languages)
            for i in range(self.num_lang-1):
                Label(self.lang_frm, text=self.languages[i] + ", ").grid(row=0, column=i+1)
            Label(self.lang_frm, text=self.languages[self.num_lang-1]).grid(row=0, column=self.num_lang)

            self.lang_frm.pack(anchor='w')

#         if self.num_lang_choices > 0:
            self.more_languages()



    def more_languages(self):
        langs_chosen = False
        self.LANG_OPTIONS = []

        for lang in mb.standard_languages:
            if lang not in self.languages:
                self.LANG_OPTIONS.append(lang)
        for lang in mb.exotic_languages:
            if lang not in self.languages:
                self.LANG_OPTIONS.append(lang)

#         print(self.LANG_OPTIONS)

        self.l_var = StringVar()
        self.l_var.set("select")

        self.lang_opt1 = OptionMenu(self.lang_frm, self.l_var, *self.LANG_OPTIONS, command=partial(self.choose_lang, 1))
        self.lang_opt1.grid(row=0, column=self.num_lang+1)
        self.lang1_set = False

        if self.num_lang_choices > 1:
            self.lang_opt2 = OptionMenu(self.lang_frm, self.l_var, *self.LANG_OPTIONS, command=partial(self.choose_lang, 2))
            self.lang_opt2.grid(row=0, column=self.num_lang+2)
            self.lang2_set = False
        if self.num_lang_choices > 2:
            self.lang_opt3 = OptionMenu(self.lang_frm, self.l_var, *self.LANG_OPTIONS, command=partial(self.choose_lang, 3))
            self.lang_opt3.grid(row=0, column=self.num_lang+3)
            self.lang3_set = False

    def choose_lang(self, btn, lang):
#         print(btn)
#         print(lang)
#         print()

        self.LANG_OPTIONS.remove(lang)
        self.languages.append(lang)
#         print(self.languages)
        self.l_var.set("next")

        if btn == 1 and self.lang1_set == False:
            self.lang_opt1.destroy()
            self.lang_lbl1 = Label(self.lang_frm, text=lang)
            self.lang_lbl1.grid(row=0, column=self.num_lang+1)
            self.lang1_set = True
        elif btn == 2 and self.lang2_set == False:
            self.lang_opt2.destroy()
            self.lang_lbl2 = Label(self.lang_frm, text=lang)
            self.lang_lbl2.grid(row=0, column=self.num_lang+2)
            self.lang2_set = True
        elif btn == 3 and self.lang3_set == False:
            self.lang_opt3.destroy()
            self.lang_lbl3 = Label(self.lang_frm, text=lang)
            self.lang_lbl3.grid(row=0, column=self.num_lang+3)
            self.lang3_set = True


        if btn != 1 and self.lang1_set == False:
            self.lang_opt1.destroy()
            self.lang_opt1 = OptionMenu(self.lang_frm, self.l_var, *self.LANG_OPTIONS, command=partial(self.choose_lang, 1))
            self.lang_opt1.grid(row=0, column=self.num_lang+1)
        if btn != 2 and self.lang2_set == False:
            self.lang_opt2.destroy()
            self.lang_opt2 = OptionMenu(self.lang_frm, self.l_var, *self.LANG_OPTIONS, command=partial(self.choose_lang, 2))
            self.lang_opt2.grid(row=0, column=self.num_lang+2)
        if btn != 3 and self.lang3_set == False:
            self.lang_opt3.destroy()
            self.lang_opt3 = OptionMenu(self.lang_frm, self.l_var, *self.LANG_OPTIONS, command=partial(self.choose_lang, 3))
            self.lang_opt3.grid(row=0, column=self.num_lang+3)


    def equip_choices(self):
        self.equip_frm1 = Frame(self.master)
        self.equip_frm2 = Frame(self.master)
        self.equip_frm1.pack(anchor='w')
        self.equip_frm2.pack()

        Label(self.equip_frm1, text="Choose Your Equipment:").pack()



















#         choices = Text(self.master, width=300, height=5)
#         choices.pack()
#         choices.insert('1.0', "This is where you'll make choices about skill, equipment, languages, and tools")
#         Button(self.master, text="Flavor Choices", command=self.flavor_choices).pack()

#         skill_frame.pack(anchor='w')










    def flavor_choices(self):
        self.clear()

        Button(self.master, text="Back to Menu", command=self.menu).pack()
        f_choices = Text(self.master, width=300, height=5)
        f_choices.pack()
        f_choices.insert('1.0', "This is where you'll choose your name, age, size, alignment")
        Button(self.master, text="Make Bio", command=self.bio_placeholder).pack()

    def bio_placeholder(self):
        self.clear()

        Button(self.master, text="Back to Menu", command=self.menu).pack()
        Button(self.master, text="Write to File (not yet)").pack()
        bio_place_txt = Text(self.master)
        bio_place_txt.pack()
        bio_place_txt.insert('1.0',
                             "Race: " + rb.race_str +
                             "\nClass: " + cb.ch_class +
                             "\nBackground: " + bb.bg +
                             "\n\nSTR: " + str(self.strength_final) +
                             "\nDEX: " + str(self.dexterity_final) +
                             "\nCON: " + str(self.constitution_final) +
                             "\nINT: " + str(self.intelligence_final) +
                             "\nWIS: " + str(self.wisdom_final) +
                             "\nCHA: " + str(self.charisma_final))




#     def final_choices(self):
#         self.clear()
#         # character name[entry], age[entry], height[entry], weight[entry], class[set], background[set], race/subrace[set], alignment[allow choice from list]
#         # ability scores/modifiers[set except for mods], saving throws[set], skills[choices], prof bonus=2[set]
#         # AC[calculate], init bonus[DEX mod], hit dice[set], max hp[calculate], speed[set]
#         # Proficiencies: languages[choices], tools[choices], armor[organize], weapons[organize]
#         # Equipment[choices & organize]
#         # Traits[sort of set]
#
#
#         if rb.subrace != 'NA':
#             race = rb.subrace + ' ' + rb.race
#         else:
#             race = rb.race
#         ch_class = cb.ch_class
#         bg = bb.bg
#
#
#
#         save1 = cb.save1
#         save2 = cb.save2



root = Tk()
test_run = Main(root)
root.mainloop()
