# SPELLING CHECKER QUESTION
from only_words import onlyTheWords
from sys import argv
WORDSS_FILE="..DATA.WORD.txt"

if len(argv)!=2:
    print("one line must be present")
    quit()
try:
    inf=open(argv[i],"r")
except:
    print("failed to open loading..",argv[1])
    quit()

 # for load all the word from dictionary
valid={ }
words_file=open(WORDSS_FILE,"r")
for word in words_file:
    word = word.lower().rstrip()
    valid[word]=0
words_file.close()

# read each lijne from  mispelt
misspelled=[]
for word in words:
    if word.lower() not in valid and word not in misspelled:
        misspelled.append(word)
inf.close()

if len(misspelled)==0:
    print("NO WORS ARE MISPELLED:")
    for word in misspelled:
        print("",word)