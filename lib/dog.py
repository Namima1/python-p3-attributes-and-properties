#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Default String", breed="Beagle"):
        # if (type(name) is str) and (1 <= len(name) <= 25):
        self.name = name
        self.breed = breed
        # else: 
        #     print("Name must be string between 1 and 25 characters.")
        
    def get_name(self):
        return self._name 
        
    def set_name(self, name):
        if (type(name) is str) and (1 <= len(name) <= 25):
            self._name = name
        else: 
            print("Name must be string between 1 and 25 characters.")
    name = property(fset=set_name, fget=get_name) 
    
    def get_breed(self):
        return self._breed 
        
    def set_breed(self, breed):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
        if (breed in approved_breeds):
            self._breed = breed
        else: 
            print("Breed must be in list of approved breeds.")
    breed = property(fset=set_breed, fget=get_breed) 
    
    
    
#name is property
#_name is correspondent attribute
#use properties to protect attribute 
