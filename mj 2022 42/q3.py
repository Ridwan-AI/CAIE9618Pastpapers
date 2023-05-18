class Card:
    # Number Integer
    # Color String
    def __init__(self, num, col):
        self.__Number = num
        self.__Color = col

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Color


# ArrayCard[30] Integer
ArrayCard = [Card("", "") for i in range(30)]
try:
    file = open("./mj 2022 42/CardValues.txt")
    for i in range(30):
        num = int(file.readline())
        col = file.readline()
        NewCard = Card(num, col)
        ArrayCard[i] = NewCard
    file.close()
except IOError:
    print("File not found")

Players = [0 for i in range(5)]

global TakenCards
TakenCards = []


def ChooseCard():
    global TakenCards
    while True:
        PickingCard = int(input("Choose a card: "))

        if PickingCard >= 1 and PickingCard <= 30:
            TakenCheck = False

            for i in range(len(TakenCards)):
                if PickingCard == TakenCards[i]:
                    TakenCheck = True
            if (TakenCheck) == False:
                TakenCards.append(PickingCard)
                break

            else:
                print("Card already taken")
        else:
            print("Number needs to be between 1 and 30")

    return PickingCard - 1


# Player1 [] Card
Player1 = []
for i in range(4):
    NewCardIndex = ChooseCard()
    NewCard = ArrayCard[NewCardIndex]
    Player1.append(NewCard)
for i in range(4):
    print(Player1[i].GetNumber())
    print(Player1[i].GetColour())
