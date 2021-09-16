#!/usr/bin/python
# -*- coding: utf-8 -*-
from ramdom import randrange, uniform

class Fighter: 
    """The base class of a Fighter"""
    
    def __init__(self,name, description):
        self.__name = name #attribut privé
        self.__description = description
        self.__agility = randrange(1,9)
        self.__healthPoints = 100 # Lors de la création d'une instance, les points de vie valent 100.

    def get_name(self):
        """Return the name of the fighter"""
        return self.__name

    def get_description(self):
        """Return the description of the fighter"""
        return self.__description

    def get_agility(self):
        """Return the agility of the fighter"""
        return self.__agility

    def get_strenght(self):
        """Return the strenght of the fighter"""
        return 10 - self.get_agility()

    def get_healthPoints(self):
        """Return the healthPoints of the fighter"""
        return self.__healthPoints

    def set_description(self, description):
        """Set the description of the fighter"""
        self.__description = description

    def __repr__(self):
        return self.get_name()

    def punch(self, Fighter):
        """
        punch Fighter
        return the  health points of Fighter
        """
        points=int(uniform(0.7,1.0)*10*self_strenght()/Fighter.get_agility())
        Fighter.__healthpoints = Fighter.get_healthpoints()-points
        return Fighter.get_healthpoints()

class Weapon:
    """The base class of a Weapon"""

    def
