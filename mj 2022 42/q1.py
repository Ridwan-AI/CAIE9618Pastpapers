# StackData Integer
# StackPointer Integer

global StackData
global StackPointer

StackData = [0 for i in range(10)]
StackPointer = 0

def PrintAll():
    global StackPointer
    global StackData
    print ("StackPointer is ", StackPointer)
    print ("StackData is: ")
    for i in range(10):
        print(StackData[i])


def Push(NewInteger):
    global StackPointer
    global StackData
    print(StackPointer)
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = NewInteger
        StackPointer = StackPointer + 1
        return True
def Pop():
    global StackPointer
    global StackData
    if StackPointer == 0:
        return -1
    else:
        PopValue = StackData[StackPointer - 1]
        StackPointer = StackPointer - 1


for i in range(11):
    NewInteger = input("Enter a new integer: ")
    if Push(NewInteger) == True:
        print("Successfully added to the stack")
    else:
        print("Failed to add to the stack")

PrintAll()
Pop()
Pop()
PrintAll()
