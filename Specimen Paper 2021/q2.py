class HiddenBox:
    # __BoxName String
    # __Creator String
    # __DateHidden String
    # __GameLocation String
    # __LastFinds [10][2] String
    # __Active Boolean !Not sure what this str/bool
    def __init__(self,BoxName,Creator,DateHidden,GameLocation):
        __BoxName = BoxName
        __Creator = Creator
        __DateHidden = DateHidden
        __GameLocation = GameLocation
        __LastFinds = [["" for i in range (2)] for j in range (10)]
        __Active = False
    
    def GetBoxName(self):
        return (self.__BoxName)
    def GetGameLocation(self):
        return (self.__GameLocation)


TheBoxes = [HiddenBox("","","","") for i in range(10000)]

def NewBox():
    BoxName = input ("Enter Box Name: ")
    Creator = input ("Enter Creator: ")
    DateHidden = input ("Enter Date Hidden: ")
    GameLocation = input ("Enter Game Location: ")
    NewInstance = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
    TheBoxes.append(NewInstance)

# NewBox()

print (len(TheBoxes))
