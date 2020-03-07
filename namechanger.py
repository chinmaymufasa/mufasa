from tkinter import *


class NameChanger(object):

    name = 'name'

    def __init__(self):
        self.path = 'C:\\Users\\satyam\\Documents\\My Games\\OpenJK\\japlus\\'
        self.cfg_name = 'main.cfg'
        self.text = 'seta name "Padawan"\n'
        self.list = []
        self.prev = -1
        self.detected = 0
        self.idx = 0
        self.element = ''
        self.sublist = []
        self.subtext = ''
        self.newname = 'Padawan'
        self.current_val = ''

        self.open_file()
        # make a list out of the file:
        self.split_cfg()
        # find the name string:
        self.check_list()


        self.root = Tk()
        self.root.geometry('370x70')
        self.root.maxsize(width=370, height=70)
        self.root.minsize(width=370, height=70)
        self.root.wm_title("Name editor")
        self.label_name = Label(self.root, text='Name')
        self.entry_name = Entry(self.root, width=50)
        self.button_rename = Button(self.root, text='Rename!', command=self.rename_action)
        self.button_current = Button(self.root, text='Show Current', command=self.get_current)

        #self.entry_name.delete(0, END)
        #self.entry_name.insert(0, self.current_name)


    def open_file(self):
        fo = open(self.path + self.cfg_name)
        self.text = fo.read()
        fo.close()

    def split_cfg(self):
        for self.detected, val in enumerate(self.text):
            if self.text[self.detected] == '\n':
                self.list.append(self.text[self.prev + 1:self.detected + 1])
                self.prev = self.detected

    def check_list(self):
        for self.idx, val in enumerate(self.list):
            self.element = self.list[self.idx]
            self.sublist = self.element.split()
            for x, word in enumerate(self.sublist):
                if self.sublist[x].lower() == self.name:
                    return

    def rename(self):
        self.list[self.idx] = 'seta name ' + '"' + self.newname + '"\n'

    def write_file(self):
        fo = open(self.path + self.cfg_name, 'w')
        fo.write(''.join(self.list))
        fo.close()

    def rename_action(self):
        self.newname = self.entry_name.get()
        # open!
        print('From: ' + self.list[self.idx])
        # rename!
        self.rename()
        print('To: ' + self.list[self.idx])
        # overwrite!
        self.write_file()

    def get_current(self):
        self.check_list()
        self.current_val = self.sublist[2]
        self.current_val = self.current_val[1:-1]
        self.entry_name.delete(0, END)
        self.entry_name.insert(0, self.current_val)

    def GUI(self):
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name.grid(row=0, column=1,columnspan=3, padx=5, pady=5)
        self.button_rename.grid(row=1, column=1, padx=5, pady=5, sticky=E)
        self.button_current.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        self.root.mainloop()
'''

    def colorize(self):
        self.input = self.entry_name.get()
        self.start = 0
        self.end = 0

        for x, val in enumerate(self.input):
            if self.input[x] == '^' and self.input[x+1] == '1' and self.input[x+2] != '^':
                for y, char in enumerate(self.input[x:], x):
                    if self.input[y] == '^':
                        self.entry_name.tag_add("red", x, y - 1)
                        break




            if self.input[x] == '^' and self.input[x+1] == '2' and self.input[x+2] != '^':
                pass
            if self.input[x] == '^' and self.input[x+1] == '3' and self.input[x+2] != '^':
                pass
            if self.input[x] == '^' and self.input[x+1] == '4' and self.input[x+2] != '^':
                pass
            if self.input[x] == '^' and self.input[x+1] == '5' and self.input[x+2] != '^':
                pass
            if self.input[x] == '^' and self.input[x+1] == '6' and self.input[x+2] != '^':
                pass
            if self.input[x] == '^' and self.input[x+1] == '7' and self.input[x+2] != '^':
                pass
            if self.input[x] == '^' and self.input[x+1] == '0' and self.input[x+2] != '^':
                pass
'''

name = NameChanger()
name.GUI()


#name.get_current()
#print('current: ' + name.current_val + '\n')

#name.newname = 'balls'
#name.rename_action()