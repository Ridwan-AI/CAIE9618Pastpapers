global PlayerNames
global PlayerScores

PlayerNames = ["" for i in range(11)]  # String
PlayerScores = [0 for i in range(11)]  # Integer


def ReadHighScores():
    global PlayerNames
    global PlayerScores
    try:
        file = open("./mj 2022 41/HighScore.txt", "r")
        for i in range(10):
            NewName = (file.readline()).strip("\n")
            NewScore = int((file.readline()).strip("\n"))
            PlayerNames[i] = NewName
            PlayerScores[i] = NewScore
        file.close()
    except IOError:
        print("File not found")


def OutputHighScores():
    global PlayerNames
    global PlayerScores
    for i in range(11):
        print(PlayerNames[i], PlayerScores[i])

def CreateNewTopTenList(NewPlayerName, NewPlayerScore):
    global PlayerNames
    global PlayerScores
    NewPlayerPosition = 10
    PlayerNames[NewPlayerPosition] = NewPlayerName
    PlayerScores[NewPlayerPosition] = NewPlayerScore

    while PlayerScores[NewPlayerPosition] > PlayerScores[NewPlayerPosition - 1]:
        TempName = PlayerNames[NewPlayerPosition - 1]
        TempScore = PlayerScores[NewPlayerPosition - 1]

        PlayerNames[NewPlayerPosition - 1] = PlayerNames[NewPlayerPosition]
        PlayerScores[NewPlayerPosition - 1] = PlayerScores[NewPlayerPosition]

        PlayerNames[NewPlayerPosition] = TempName
        PlayerScores[NewPlayerPosition] = TempScore
        NewPlayerPosition = NewPlayerPosition - 1
        if NewPlayerPosition == 0:
            break

ReadHighScores()
OutputHighScores()

NewPlayerName = ""
NewPlayerScore = 0
while len(NewPlayerName) != 3:
    NewPlayerName = input("Enter name of new player: ")
while NewPlayerScore < 1 or NewPlayerScore > 100000:
    NewPlayerScore = int(input("Enter score of new player: "))

CreateNewTopTenList(NewPlayerName, NewPlayerScore)
OutputHighScores()

def WriteTopTen():
    file = open('./mj 2022 41/NewHighScore.txt', 'w')
    for i in range (10):
        file.write(PlayerNames[i] + "\n")
        file.write(str(PlayerScores[i]) + "\n")
    file.close()
WriteTopTen()