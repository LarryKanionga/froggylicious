from sys import exit
from random import randint

class Situations(object):
    """Base class of events"""

    calm_down_options = ["burn the lake",
                         "drop a big wood into the lake",
                         "start singing",
                         "invite some frog-girls to join the lake",
                         "bring a shark to the lake",
                         "shoot them"
                         ]

    def enter(self):
        print "Implemented in subclass"
        exit(1)


class BBQ(object):
    """Child of Situations, BBQ event"""
    bbq_options = ["\nThe frogs are hungry smelling your tasty steaks, they are starting eating your fishes",
                   "\nThe frogs are furious hearing you singing and eating hot dogs",
                   "\nThe coal is starting to get louder, so the frogs can't speak to each other so they are making the fishes singing to get louder"]

    def __init__(self):
        self.situations = Situations()    

    def play(self):
        
        print self.bbq_options[randint(0, len(self.bbq_options) - 1)]
        print "\t How do you want to calm them down?"
        i = 0
        for option in self.situations.calm_down_options:
            print """\t[%d] %s""" % (i, option)
            i += 1
        
        return int(raw_input("> "))
         

class KaffeeKraenzchen(object):
    """Child of Situations, coffee time event"""

    options = ["\nYour coffee maker is too loud, the frogs are jealous and started to sing with your karaoke machine",
               "\nThe frogs don't like to hear your gossip so they started to jump until they get your cake"]

    def __init__(self):
        self.situations = Situations()    

    def play(self):
        
        print self.options[randint(0, len(self.options) - 1)]
        print "\t How do you want to calm them down?"
        i = 0
        for option in self.situations.calm_down_options:
            print """\t[%d] %s""" % (i, option)
            i += 1
        
        return int(raw_input("> "))

class BirthdayParty(object):
    """Child of Situations, birthday event"""

    options = ["\n The frogs don't like your wannabe friends so they are having an orgy to distract your friends",
               "\n The frogs are furious because nobody of your girlfriends are wearing mini-skirts, so they started to eat your plants"]

    def __init__(self):
        self.situations = Situations()    

    def play(self):
        
        print self.options[randint(0, len(self.options) - 1)]
        print "\t How do you want to calm them down?"
        i = 0
        for option in self.situations.calm_down_options:
            print """\t[%d] %s""" % (i, option)
            i += 1
        
        return int(raw_input("> "))


class Replanting(object):
    """Child of Situations, removing plants event"""

    options = ["\n The frogs are eating your fish as a protest of your bad choice of new plants",
               "\n The frogs are leaving the mosquitoes alive knowing that the time you spent at home will be unsupportable"]

    def __init__(self):
        self.situations = Situations()    

    def play(self):
        
        print self.options[randint(0, len(self.options) - 1)]
        print "\t How do you want to calm them down?"
        i = 0
        for option in self.situations.calm_down_options:
            print """\t[%d] %s""" % (i, option)
            i += 1
        
        return int(raw_input("> "))


class VisitTheRussians(object):
    """Child of Situations, visit the Russians neighbor event"""
    
    options = ["\n It was hard to learn German and just because you go with the Russians the frogs are jealous and want to scream as loud as they can",
               "\n The frogs are not communists anymore, so they decided to eat your fish and your plants as salad"]

    def __init__(self):
        self.situations = Situations()    

    def play(self):
        
        print self.options[randint(0, len(self.options) - 1)]
        print "\t How do you want to calm them down?"
        i = 0
        for option in self.situations.calm_down_options:
            print """\t[%d] %s""" % (i, option)
            i += 1
        
        return int(raw_input("> "))


class Loose(object):
    """For exit and loose situation"""
    the_form_you_died = ["This event is actually canceled, whatever! You don't have access to the house anymore, the government took your house away from you.",
                         "The frogs mutated themselves with fish, rats and Russians and they are living in your house, so you lose.",
                         "You forgot to close the door so the frogs found your marihuana plant and reported it to the Russians."]

    def __init__(self):
        self.situations = Situations()
    
    def play(self):
        print self.the_form_you_died[randint(0,len(self.the_form_you_died) - 1)]
        exit(1)
