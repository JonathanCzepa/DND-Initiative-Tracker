from abc import ABC, abstractmethod
import random


#Abstract class for NPCs and PCs.
class creature(ABC):

    HP_MIN = 0
    MIN_HP_TEMP = 0

    def __init__(self, Name, AC, HP, initMod):

        self.__name = Name
        self.__AC = AC
        self.__HPmax = HP
        self.__HPcurrent = HP
        self.__HPtemp = 0
        self.__turn = 0
        self.__initMod = initMod
        self.init = 0

        self.__dead = False
        self.__hasSaves = False
        self.__manual = False
        self._isAlly = False
        

    @abstractmethod
    def deathSaves(self):
        pass

    def rollX(die):
        result = random.randrange(1,die)
        return random.randrange(1,die)
    
    def setDead(self):
        self.__dead = not self.__dead

    def setAlly(self):
        self.__isAlly = not self.__isAlly

    def rollInit(self):
        self.init = random.randrange(1,20) + self.__initMod
    
    def isManual(self):
        self.__manual = not self.__manual
    
    """
    if using radio buttons we can change this to:
    def isManual(x) -> none
    self.__manual = x
    
    """

    def setInitMod(self, x) -> None:
        self.__initMod = x
    
    def setAC(self, x) -> None:
        self.__AC = x

    def setTurn(self, x) -> None:
        self.__turn = x

    def setHPTemp(self, x) -> None:
        self.__HPtemp = x
    
    def setMaxHP(self, x) -> None:
        self.__HPmax = x
        self.__HPcurrent = x

    def setHeal(self, x) -> None:
        self.setDamage(-x)
    
    def setTempHP(self, x) -> None:
        self.__HPtemp = x


    """ Setter to deal with damage and healer scenarios  """   
    def setHPcurrent(self, damage) -> int:    

        #Check if wanting to deal damage
        if (damage > 0):
            #Check if TempHP is existent
            if (self.__HPtemp > 0):
            
                #Deal damage to tempHP
                self.__HPtemp -= damage
                #Check if tempHP is less than 0
                if (self.__HPtemp < 0):
                    self.__HPtemp = 0
                    #Set follow through damage
                    throughDamage = damage - self.__HPtemp
                    #Deal follow through damage
                    self.__HPcurrent -= throughDamage
        
            #Deal damage with no temp HP
            if (self.__HPtemp == 0):
                self.__HPcurrent -= damage
      
        #Healing == -damage
        if (damage < 0):
            self.__HPcurrent -= damage

            if (self.__HPcurrent > self.__HPmax):
                self.__HPcurrent = self.__HPmax


    def getHPcurrent(self):
        return self.__HPcurrent

    def getHPtemp(self) -> int:
        return self.__HPtemp  
    
    def getAC(self) -> int:
        return self.__AC
    
    def getInit(self) -> int:
        return (self.__initMod + self.init) 
    
    def getHPmax(self) -> int:
        return self.__HPmax
    
    def getTurn(self) -> int:
        return self.__turn
    
    def getIsDead(self) -> None:
        return self.__dead
    
    def getAlly(self) -> None:
        return self._isAlly
    
    def getName(self) -> str:
        return self.__name
        
    
    def __str__(self):
        return f'{self.__name}'
        
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

def sortInit(creatures, init, reverse=False):
    return sorted(creatures, key=lambda x: getattr(x, init), reverse=reverse)




