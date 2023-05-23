class Character:
    # Private Name string
    # Private XCoordinate integer
    # Private YCoordinate integer
    def __init__(self, pName, pXCoordinate, pYCoordinate):
        self.__Name = pName
        self.__XCoordinate = int(pXCoordinate)
        self.__YCoordinate = int(pYCoordinate)

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange


# CharacterArray Character[10]
CharacterArray = [Character("", 0, 0) for i in range(10)]

try:
    file = open("./on 2022 42/Characters.txt", "r")
    for i in range(10):
        name = file.readline().strip("\n")
        xcoordinate = int(file.readline().strip("\n"))
        ycoordinate = int(file.readline().strip("\n"))
        newCharacter = Character(name, xcoordinate, ycoordinate)
        CharacterArray[i] = newCharacter
    file.close()
except IOError:
    print("File not found")

Found = False
Index = 0
while Found == False:
    SearchName = input("Enter character name: ")
    for i in range(10):
        if (CharacterArray[i].GetName()).lower() == (SearchName).lower():
            Index = i
            Found = True
            break

letter = ""
while letter != "A" and letter != "W" and letter != "S" and letter != "D":
    letter = input("Enter a letter: ")

XChange = 0
YChange = 0

if letter == "A":
    XChange -= 1
if letter == "W":
    YChange += 1
if letter == "S":
    YChange -= 1
if letter == "D":
    XChange += 1

CharacterArray[Index].ChangePosition(XChange, YChange)
print (CharacterArray[Index].GetName()," has changed coordinates to X = ", CharacterArray[Index].GetX(), " and Y = ", CharacterArray[Index].GetY())