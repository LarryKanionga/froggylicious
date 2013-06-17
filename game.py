# 
# This project tries to solve the problem of the book "learnpythonthehardway"
# in the "Exercise 45: You Make A Game".
# The goal of this exercise is the use of composition and classes 
# in different files using python.
#
# Description of the game:
# This game is about a house with a small lake filled with frogs.
# The user has to manage to calm down the frogs depending on the event 
# at the house.
#
# Created by Diego Loop, diegoloop@icloud.com on 17, June 2013
#

from sys import exit
from random import randint
from situations import *

class Weather(object):
    weather = {
            'january' : 'cold',
            'february' : 'cold',
            'march' : 'cold',
            'april' : 'sunny',
            'may' : 'sunny',
            'june' : 'hot',
            'july' : 'hot',
            'august' : 'hot',
            'september' : 'hot',
            'october' : 'foggy',
            'november' : 'foggy',
            'december' : 'cold'
            }
    temperature = 'cold'
    month = ''

    def __init__(self):
        print "Write the month of the event"
        self.month = raw_input("> ")

    def get_temperature(self):
        self.temperature = self.weather[self.month]
        return self.temperature
    
status = ['happy', 'good looking', 'agressive', 'furious']   

class Frog(object):

    
    activity = ['wanting to mate', 'tanning in the sun', 'singing', 'singing in the rain', 
                'boxing', 'eating fish food', 'taking a bath', 
                'consuming drugs', 'diving', 'learning fish language']

    def agressive_status(self, weather):
        
        if weather == "cold":
            return status[0]

        elif weather == "sunny":
            return status[1]

        elif weather == "foggy":
            return status[2]

        elif weather == "hot":
            return status[3]
        else:
            exit(1)

    def current_activity(self):
        count = len(self.activity) - 1
        return self.activity[randint(0,count)]


class Engine(object):
    
    instructions = """
    What is your invitation for?
    Select one of the crowd by typing the number
    [1] BBQ
    [2] Coffee time
    [3] Birthday Party
    [4] Replanting
    [5] Visit the Russians
    """

    events = [BBQ(), KaffeeKraenzchen(), BirthdayParty(), Replanting(), VisitTheRussians()]
    
    def __init__(self):
        print self.instructions
        self.choice = int(raw_input("> "))

    def choose_event(self):

        while self.choice > len(self.events):
            print "Hey Mr., please select just one of the options"
            self.__init__()

        return self.choice     

    def show_event_weather(self, temperature):
        print "It seems that it will be", temperature, "outside" 
    
    def ask_party_question(self):  
        print "Do you still wanna have this event?"
        print """
        [1] Yes
        [2] No
        """
        answer = int(raw_input("> "))
        if (answer == 1):
            #print "self.choice ", self.choice
            event = self.events[self.choice - 1]
            event.play()
            random_index = randint(0, len(status) - 1)
            if random_index == 0 or random_index == 1:
                print "You made the maniacs %s" % status[random_index], "You win!"
            else:
                print "You made the maniacs %s" % status[random_index], "You lose!"
            exit(1)
            

        else:
            event = Loose()
            event.play()
            

    def show_frogs_humor(self, agressitiblity):
        print "The maniacs will be probably", agressitiblity, self.ask_party_question()
    


engine = Engine()
engine.choose_event()
weather = Weather()
temperature = weather.get_temperature()
engine.show_event_weather(temperature)
frog = Frog()
agressitiblity = frog.agressive_status(temperature)
engine.show_frogs_humor(agressitiblity)
