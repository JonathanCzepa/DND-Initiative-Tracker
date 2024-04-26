from abc import ABC, abstractmethod


#Abstract class for NPCs and PCs.
class creature(ABC):

    HP_MIN = 0
    MIN_DAMAGE_TAKEN = 0
    MIN_DAMAGE_HEALED = 0

    def __init__(self):

        self.__name = "Enter Name"
        self.__AC = 0
        self.__HPmax = 0
        self.__HPcurrent = 0
        self.__turn = 0
        self.__initMod = 0
        self.__damageHealed = creature.MIN_DAMAGE_HEALED
        self.__damageTaken = creature.MIN_DAMAGE_TAKEN
        self.__hasSaves = False

    @abstractmethod
    def deathSaves(self):
        pass

class playerCharacter(creature):

    """
    Method that ensures players always have death saves. Always call by default
    """
    def deathSaves(self):
        self.__hasSaves = True
    #Will most likely change how death saves are handled. 
    #However, there needs to be at least one abstract method so this is it for now.

class NPC(creature):
    
    """
    Method that allows the user to choose whether a NPC has death saves
    """
    def deathSaves(self):
        self.__hasSaves = not self.__hasSaves



