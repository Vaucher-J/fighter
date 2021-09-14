#!/usr/bin/python
# -*- coding: utf-8 -*-
from ramdom import randrange

class Fighter: 
    """The base class of a Fighter"""
    
    def __init__(self,name, description):
        self.__name = name #attribut privé
        self.__description = description
        self.agility = randrange(1,9)

    def get_name(self):
        """Return the name of the fighter"""
        return self.__name

    def get_description(self):
        """Return the description of the fighter"""
        return self.__description

    def get_agility(self):
        """Return the agility of the fighter"""
        return self.__agility

    def set_description(self, description):
        """Set the description of the fighter"""
        self.__description = description

    def __repr__(self):
        return self.get_name()
