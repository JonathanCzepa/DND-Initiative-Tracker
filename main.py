from abc import ABC, abstractmethod
import random

"""
help
"""

#Abstract class for NPCs and PCs.
class creature(ABC):

    HP_MIN = 0
    MIN_HP_TEMP = 0

    def __init__(self):

        self.__name = "-"
        self.__AC = 0
        self.__HPmax = 0
        self.__HPcurrent = 0
        self.__HPtemp = 0
        self.__turn = 0
        self.__initMod = 0
        self.__init = 0

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
        self.__init = random.randrange(1,20) + self.__initMod
    
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


    
    def setHPcurrent(self, damage, healing) -> int:    

        if self.__HPtemp > 0:
            damage - self.__HPtemp

            if self.__HPtemp < 0:
                self.__HPtemp = 0
                damage - self.__HPtemp

            else:
                self.__HPtemp =- damage


        #damage_temp =- self.__HPtemp
        #self.__HPtemp =- damage
        
        self.__HPcurrent = self.__HPcurrent - damage + healing

        if self.__HPcurrent > self.__HPmax:
            self.__HPcurrent = self.__HPmax
            
        if self.__HPcurrent < self.HP_MIN:
            self.__HPcurrent = self.HP_MIN

        #check if dead
        if self.__HPtemp < 0: 
            self.__HPtemp = 0

    def getHPcurrent(self):
        return self.__HPcurrent

    def getHPtemp(self) -> int:
        return self.__HPtemp  
    
    def getAC(self) -> int:
        return self.__AC
    
    def getInitMod(self) -> int:
        return self.__initMod
    
    def getHPmax(self) -> int:
        return self.__HPmax
    
    def getTurn(self) -> int:
        return self.__turn
    
    def getInit(self) -> int:
        return self.__init
    
    def getIsDead(self) -> None:
        return self.__dead
    
    def getAlly(self) -> None:
        return self._isAlly

        
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




Katla = playerCharacter()

Katla.setMaxHP(30)
Katla.setHPcurrent(0, 0)
print(f"Katla's HP is: {Katla.getHPcurrent()}")


Katla.setHPTemp(10)
print(f"Katla's THP is: {Katla.getHPtemp()}")

Katla.setHPcurrent(9, 0)

print(f"Katla's THP is: {Katla.getHPtemp()}")
print(f"Katla's HP is: {Katla.getHPcurrent()}")
