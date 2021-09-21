#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randrange, uniform



class Fighter: 
    """The base class of a Fighter"""
    
    def __init__(self,name, description):
        self.__name = name #attribut privé
        self.__description = description
        self.__agility = randrange(1,9)
        self.__healthPoints = 100 # Lors de la création d'une instance, les points de vie valent 100.
        self.__weapon = None

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

    def punch(self, afighter):
        """
        punch Fighter
        return the  health points of Fighter
        """
        points=int(uniform(0.7,1.0)*10*self.get_strenght()/afighter.get_agility())
        afighter.__healthPoints = afighter.get_healthPoints()-points
        return afighter.get_healthPoints()

    def summary(self):
        """Return the summary of a fighter"""
        name = 'name : ' + self.get_name()
        description = 'description : ' + self.get_description()
        agility = 'agility : ' + str(self.get_agility())
        strength = 'strength : ' + str(self.get_strength())
        health_points = 'health_points : ' + str(self.get_health_points())
        summary = '\n'.join([name, description, agility, strength, health_points])
        if self.take_weapon():
            summary += self.take_weapon().summary()
        return summary

    def shoot(self, a_fighter):
        """Shoot a fighter and return the fighter health points"""
        if self.get_ammos()>0:
            lostPoints = int(self.get_damage() / a_fighter.get_agility())
            lostPoints = int(lostPoints * uniform(0.5,1)) # some random added
            a_fighter.__health_points = a_fighter.get_health_points() - lostPoints
            self.__ammos -= 1 # remove one ammo
        return a_fighter.get_health_points()

    def take_weaopn(self, a_weapon):
        if self.__weapon == None:
            self.__weapon == a_weapon
        return self.__weapon




class Weapon:
    """The base class of a Weapon"""

    def __init__(self, name, description):
        self.__name = name # attribut privée
        self.__damage = damage
        self.__ammos = ammos

    def __repr__(self):
        return self.get_name()

    def get_name(self):
        """ return the name of the fighter"""
        return self.__name

    def get_damage(self):
        """ return the name of the fighter"""
        return self.__damage

    def get_ammos(self):
        """ return the name of the fighter"""
        return self.__ammos

    def get_owner(self):
        """Returns the owner of the weapon"""
        return self.__owner

    def set_owner(self, owner):
        """Returns the owner of the weapon"""
        self.__owner = owner

    def summary(self):
        """Return the summary of a weapon"""

        name='name:%s'%self.getName()
        damage='dégat:%s'%self.getDamage()
        ammos='munitions:%s'%self.getAmmos()
        return '\n'.join([name, damage, ammos])

    def shoot(self, a_fighter):
        """Shoot a fighter and return the fighter health points"""
        if self.get_ammos()>0:
            lostPoints = int(self.get_damage() / a_fighter.get_agility())
            lostPoints = int(lostPoints * uniform(0.5,1)) # some random added
            a_fighter.__health_points = a_fighter.get_health_points() - lostPoints
            self.__ammos -= 1 # remove one ammo
        return a_fighter.get_health_points()

