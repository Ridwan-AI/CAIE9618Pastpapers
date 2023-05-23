# Queue[100] integer
Queue = [-1 for i in range(100)]
# HeadPointer integer
HeadPointer = -1
# TailPointer integer
TailPointer = 0


def Enqueue(NewData):
    global Queue
    global HeadPointer
    global TailPointer
    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = NewData
        TailPointer = TailPointer + 1
        return True
    else:
        return False


allsuccess = True
for i in range(1, 21):
    Success = Enqueue(i)
    if Success == False:
        allsuccess = False
if allsuccess == False:
    print("Unsuccessful")
else:
    print("Successful")
# print(Queue)


def RecursiveOutput(Start):
    # Base Case
    if Start == 0:
        return Queue[Start]
    # General Case
    else:
        return (RecursiveOutput(Start-1)) + Queue[Start]


print(RecursiveOutput(TailPointer - 1))
