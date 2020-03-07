


def sublist_analyze(list):
    newlist = []
    for idx, string in enumerate(list):
        text = list[idx]
        prev = 0
        for detected, val in enumerate(text):
            if text[detected] == ' ':
                newlist.append(text[prev:detected])
                prev = detected
    return newlist

def check_list(cvar, list):
    for idx, string in enumerate(list):
        text = list[idx]
        sublist = text.split()
        for x, word in enumerate(sublist):
            if sublist[x].lower() == cvar.lower() or sublist[x].lower() == '"' + cvar.lower() + '"':
                return idx
    return 0



fo = open(r'C:\Users\satyam\Documents\My Games\OpenJK\japlus\testconfig.cfg', 'r')

text = fo.read()

fo.close()

var = "ctrl"
mycfglist = split_cfg(text)


print(mycfglist)

print('\n\n')

print(check_list(var, mycfglist))
