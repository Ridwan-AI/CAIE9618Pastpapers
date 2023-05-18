class Balloon:
    # Health Integer
    # Color String
    # DefenceItem String
    def __init__(self, colour, defenceitem):
        self.__Health = 100
        self.__Colour = colour
        self.__DefenceItem = defenceitem

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, changehealth):
        self.__Health = self.__Health + changehealth

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False


NewDefenceItem = input("Enter defence item name: ")
NewColor = input("Enter color: ")
Balloon1 = Balloon(NewColor, NewDefenceItem)

def Defend(PBalloon):
    OpponentStrength = int(input("Enter opponent strength: "))
    HealthLost = - OpponentStrength
    PBalloon.ChangeHealth(HealthLost)
    print("Defence item was: ", PBalloon.GetDefenceItem())
    if (PBalloon.CheckHealth() == True):
        print("No health remaining")
    else:
        print("Health still remaining")
    return PBalloon

Balloon1 = Defend(Balloon1)