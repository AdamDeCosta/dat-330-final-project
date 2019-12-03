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

#The prime functionality of Interact is to Interact with the Surroundings around them
import pandas as pd
import numpy as np
import random
import csv

class interaction(Exception):

    """ In order to interact you need to have at least one person
    minimum. If there is no person then this code will return an error on initialization"""
    def __init__(self, people):
        #This function will fail and throw and error if People is not a string
        try:
            if isinstance(people, bool): #single person
                self.type = "single"
                self.amount_of_people = 1
                self.people = "USER" #Setting as generic for the lack of a database
            elif isinstance(people, str): #single person
                self.type = "single"
                self.amount_of_people = 1
            elif isinstance(people, list): #More than one person being addressed
                self.type = "multi"
                self.amount_of_people = len(people)
            else: #The Parameter is out of balance and is not proper
                raise Exception
        except Exception as e:
            print("Invalid amount of people")

        #Setting other variables
        self.people = people

        self.phrases = self.load_phrases()

        #self.phrases = pd.read_csv("Phrases.csv", delimiter=",")


    #Excutes the interaction of the robot
    def interact(self):
        if self.type == "multi":
            self.multi_interaction()
        elif self.type == "single":
            self.single_interaction(self.people)

    def multi_interaction(self):
        print("multi_interaction")
        for person in self.people:
            self.single_interaction(person) #making a single interaction for each of the people


    def single_interaction(self, person):
        print("single_interaction")
        print("Hello " + person + " " + self.conjure_phrase())
        
        #Send Code to the Nueral Network to get text
        #Send to the text to speech

    def speak(self, text):
        pass


    #Making it translate to text to speech
    def load_phrases(self):
        with open('Phrases.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)

        new_list = []
        for j in your_list:
            for i in j:
                new_list.append(i)
        del your_list #Memory Control
        return new_list


    def conjure_phrase(self):
       return random.choice(self.phrases)


#Testing
if __name__== "__main__":
    test_data1 = interaction("Lemon") #should throw single_interaction
    test_data1.interact()

    test_data2 = interaction(["Rose", "Grape"]) #Should throw mulit_interaction
    test_data2.interact()

    test_data3 = interaction(3) #Should throw Error


    print("")

    test_data4 = interaction("Tony")
    test_data4.interact()
    test_data4.conjure_phrase()
