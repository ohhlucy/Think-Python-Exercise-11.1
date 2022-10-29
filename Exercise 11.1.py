import pprint

# write a test file with unique words
names = '''\
Emma
Liam
Oliver
Macy
Sam
Mark
Ron
'''

fname = "names.txt"
with open(fname, 'w') as fout:
    fout.write(names)

name_dict = {}
# read in the names line by line
for line in open(fname):
    word = line.strip()
    #print(word)
    name_dict[word] = len(word)

pprint.pprint(name_dict)
