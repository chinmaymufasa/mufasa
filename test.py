import os.path
import re


def path_input():
    #asks user for the directory
    print('Enter the path to your directory')
    mypath = input('> ')
    if mypath[-1] != '\\':
        mypath = mypath + '\\'                     #makes sure that the last character is a '\'
    print('Enter the name of your cfg (no extension)')
    cfg_name = input('> ') + '.cfg'
    return mypath + cfg_name


def file_valid(filepath):
    exists = os.path.isfile(filepath)
    while exists is False:
        print("Sorry! That cfg doesn't exist!")
        filepath = path_input()
        exists = os.path.isfile(filepath)
    return filepath


def cfg_separate(path):
    #function turns the cfg into a list of cvars!
    fr = open(path, 'r+')
    text = fr.read()
    textlist = re.split(r'(\s+)',text)
    #print(text)
    print(textlist)
    fr.close()
    return textlist

def cvar_choice_index(cvars):
    #asks the cvar to edit and returns its index
    print("Enter the cvar you would like to modify")
    input_cvar = input('> ')
    for index, val in enumerate(cvars):
        #print(i)
        if val.lower() == input_cvar.lower():
            return index
    return 0

'''
def sum_list(list):
    sum = ''
    for i, val in list:
        sum = sum + val
    return sum

'''


def edit_list(list, idx, new_val):
    #edits the chosen cvar value given its index, and new val,also must pass in the list
    list[idx + 2] = ('"' + new_val + '"')
    return list

def ask_for_new_value():
    #asks user for new val and returns it
    print("Enter the new value")
    new_value = input('> ')
    return new_value

def rewrite_file(cvars_list):
    #rewrites the original file
    fw = open(filepath, 'w')
    fw.write(''.join(cvars_list))
    fw.close()




def edit_config():
    while True:

        cvar_index_number = 0

        while cvar_index_number == 0:
            cvar_index_number = cvar_choice_index(cvars)
            if cvar_index_number == 0:
                print("sorry that cvar does not exist!")

        #print(cvar_index_number)

        user_val = ask_for_new_value()

        edit_list(cvars, cvar_index_number, user_val)

        #print(cvars)

        #print(''.join(cvars))

        rewrite_file(cvars)

        print("File overwritten!")

        response = input("Would you like to change another? y/n \n>")

        if response == 'Y' or response == 'y':
            continue
        else:
            break


def add_to_config(list):
    #adds cvar to config by appending it to list
    print("Enter the CVAR or you would like to add to your config\nNote: this will add what ever you type.")
    print("To avoid error a new cfg will be made.")
    var = input('> ')
    print("Enter the value")
    val = '"' + str(input('> ')) + '"'
    list.extend(['\n', "seta ", var, " ", val])

    fcreate = open(mypath + '\\' + 'newfile' + str(randint(1,1000)), 'w')

    fcreate.write(''.join(list))






print('Hello! Welcome to the magic cfg changer!')

filepath = path_input() #sets file to variable

filepath = file_valid(filepath) #checks to see if the file is a valid one, if not then it loops till it is; then sets the correct file to variable

#print(filepath)

cvars = cfg_separate(filepath)

#print(cvars[108])



