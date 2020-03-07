import os.path
import re
from tkinter import *


class CfgEdit(object):

    def edit_path(self, mypath, cfg):
        if mypath == '':
            return ''
        if mypath[-1] != '\\':
            mypath += '\\'
        return mypath + cfg + '.cfg'

    def cfg_read(self, path):
        # function turns the cfg into a list of cvars!
        fr = open(path, 'r+')
        text = fr.read()
        fr.close()
        return text

    def split_cfg(self, text):
        list = []
        prev = -1
        for detected, val in enumerate(text):
            if text[detected] == '\n':
                list.append(text[prev+1:detected+1])
                prev = detected
        return list

    def check_list(self, cvar, list):
        for idx, string in enumerate(list):
            text = list[idx]
            sublist = text.split()
            for x, word in enumerate(sublist):
                if sublist[x].lower() == cvar.lower() or sublist[x].lower() == '"' + cvar.lower() + '"':
                    return idx
        return 0

    def readfile(self, path):
        # function turns the cfg into a list of cvars!
        fr = open(path, 'r+')
        text = fr.read()
        return text

    def edit_list_cvar(self, list, idx, Cvar, new_val):

        list[idx] = "seta " + Cvar + ' "' + new_val + '"\n'

        return list


    def rewrite_file(self, cvars_list, valid_path):
        # rewrites the original file
        fw = open(valid_path, 'w')
        fw.write(''.join(cvars_list))
        fw.close()


'''
def change_cvar():
    my_input1 = UserInput()

    editing1 = Manipulate()

    path = my_input1.path_cfg_input()

    valid_path = my_input1.file_valid(path)

    Cvars = editing1.cfg_separate(valid_path)

    cvar_num = 0
    while cvar_num == 0:
        cvar_num = my_input1.cvar_choice_index(Cvars)
        if cvar_num == 0:
            print("Sorry that cvar doesnt exist!")

    user_val = my_input1.ask_for_new_value()

    Cvars = editing1.edit_list(Cvars, cvar_num, user_val)

    editing1.rewrite_file(Cvars, valid_path)
'''
#change_cvar()




def button1():
# Button action (main program start)
    changer = CfgEdit()

    path = entry_path.get()
    print(path)
    Cfg = entry_cfg.get()
    print(Cfg)
    Cvar = entry_cvar.get()
    print(Cvar)
    new_value = entry_new.get()
    print(new_value)
#----------------------------------------------------
    newpath = changer.edit_path(path, Cfg)
    if not os.path.isfile(newpath):
        print('not a path')
        return

#-----------------------------------------------------

    plain = changer.cfg_read(newpath)

#-----------------------------------------------------
    Cvars = changer.split_cfg(plain)
#-----------------------------------------------------
    if Cvar == '':
        print("Blank cvar")
        return
    index = changer.check_list(Cvar, Cvars)
    if index == 0:
        print('not a cvar')
        return
#-----------------------------------------------------

    edited = changer.edit_list_cvar(Cvars, index, Cvar, new_value)
#-----------------------------------------------------
    changer.rewrite_file(edited, newpath)


def listtext():
    obj = CfgEdit()

    path = entry_path.get()
    print(path)
    Cfg = entry_cfg.get()
    print(Cfg)

    newpath = obj.edit_path(path, Cfg)
    if not os.path.isfile(newpath):
        print('not a path')
        return

    string = obj.readfile(newpath)
    viewer.delete('1.0', END)
    viewer.insert('1.0', string)

#-----------------------------------------------------
#                    GUI
#-----------------------------------------------------
pad = 5

root = Tk()
root.wm_title("CFG Editor")
root.minsize(200, 300)

root.geometry('575x400')

top_frame = Frame(root)
left_frame = Frame(root)
textframe = Frame(root)
bottom_frame = Frame(root)


label_path = Label(top_frame, text="Path")
label_cfg = Label(left_frame, text="Cfg")
label_cvar = Label(left_frame, text="Cvar")
label_new = Label(left_frame, text="New value")

entry_path = Entry(top_frame)
entry_cfg = Entry(left_frame)
entry_cvar = Entry(left_frame)
entry_new = Entry(left_frame)

save_button = Button(left_frame, text="Print", command=button1)
list_button = Button(left_frame, text="List", command=listtext)

scroller = Scrollbar(textframe)
scrollerx = Scrollbar(bottom_frame, orient=HORIZONTAL)

viewer = Text(textframe, width=1, height=1, wrap=NONE, padx=5, pady=5, yscrollcommand=scroller.set, xscrollcommand=scrollerx.set)
viewer.config(state=NORMAL)
#------------------------------------------------------
#                   Pack
#------------------------------------------------------
scroller.config(command=viewer.yview)
scrollerx.config(command=viewer.xview)


top_frame.pack(side=TOP, fill=X)
left_frame.pack(side=LEFT, fill=Y)
textframe.pack(side=TOP, expand=TRUE, fill=BOTH)
textframe.pack_propagate(FALSE)
bottom_frame.pack(side=BOTTOM, fill=BOTH)

label_path.pack(side=LEFT, padx=pad, pady=pad)
entry_path.pack(anchor=W, padx=pad, pady=pad, fill=X)

label_cfg.pack(padx=pad, pady=pad)
entry_cfg.pack(padx=pad, pady=pad)

label_cvar.pack(padx=pad, pady=pad)
entry_cvar.pack(padx=pad, pady=pad)

label_new.pack(padx=pad, pady=pad)
entry_new.pack(padx=pad, pady=pad)



save_button.pack(padx=pad, pady=pad)
list_button.pack(padx=pad, pady=pad)

viewer.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=pad, pady=pad)

scrollerx.pack(side=BOTTOM, fill=X)
scroller.pack(side=RIGHT,fill=Y)


root.mainloop()

