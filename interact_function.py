# Author: Tony Calarese
# Class:  DAT 330-01
# Certification of Authenticity:
# I certify that this is entirely my own work, except where I have given fully documented
# references to the work of others.  I understand the definition and consequences of
# plagiarism and acknowledge that the assessor of this assignment may, for the purpose of
# assessing this assignment reproduce this assignment and provide a copy to another member
# of academic staff and / or communicate a copy of this assignment to a plagiarism checking
# service(which may then retain a copy of this assignment on its database for the purpose
# of future plagiarism checking).

import random
import csv

def interact():
    print("Hello There. " + conjure_phrase())



#Source of Reference: https://stackoverflow.com/questions/24662571/python-import-csv-to-list
def conjure_phrase():
    with open('Phrases.csv', 'r') as f:
        reader = csv.reader(f)
        phrases = list(reader)
    new_list = []
    for j in phrases:
        for i in j:
            new_list.append(i)
    del phrases #Memory Control
    return random.choice(new_list)




#Testing
if __name__== "__main__":
    interact()
