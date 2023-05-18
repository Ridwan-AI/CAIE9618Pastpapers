# QueueArray [10] string
QueueArray = ["" for i in range(10)]
# HeadPointer integer
# TailPointer integer
# NumberOfItems integer
HeadPointer = 0
TailPointer = 0
NumberOfItems = 0


"""
FUNCTION Enqueue(BYREF QueueArray[] : STRING, BYREF HeadPointer : INTEGER, BYREF TailPointer : INTEGER, NumberItems : INTEGER, DataToAdd : STRING) RETURNS BOOLEAN
    IF NumberItems = 10 
        THEN
            RETURN FALSE
    ENDIF
    QueueArray[TailPointer] ← DataToAdd
    IF TailPointer >= 9 
        THEN
            TailPointer ← 0
        ELSE
            TailPointer ← TailPointer + 1
    ENDIF
    NumberItems ← NumberItems + 1
    RETURN TRUE
ENDFUNCTION
"""


def Enqueue(DataToAdd, HeadPointer, TailPointer, NumberItems, QueueArray):
    if NumberItems == 10:
        return (False, HeadPointer, TailPointer, NumberItems, QueueArray)
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
    NumberItems = NumberItems + 1
    return (True, HeadPointer, TailPointer, NumberItems, QueueArray)


def Dequeue(HeadPointer, TailPointer, NumberItems, QueueArray):
    if NumberItems == 0:
        return (False, HeadPointer, TailPointer, NumberItems, QueueArray)

    DataToReturn = QueueArray[HeadPointer]
    HeadPointer = HeadPointer + 1
    if (HeadPointer >= 9):
        HeadPointer = 0
    NumberItems = NumberItems - 1
    return (DataToReturn, HeadPointer, TailPointer, NumberItems, QueueArray)


# Enqueue(DataToAdd, HeadPointer, TailPointer, NumberOfItems, QueueArray)
for i in range (11):
    DataToAdd = input("Enqueue: ")
    (Status, HeadPointer, TailPointer, NumberOfItems, QueueArray) = Enqueue(DataToAdd, HeadPointer, TailPointer, NumberOfItems, QueueArray)
    if (Status == True):
        print ("Successfully enqueued")
    else:
        print ("Failed to enqueue")
    
(DataReturned, HeadPointer, TailPointer, NumberOfItems, QueueArray) = Dequeue(HeadPointer, TailPointer, NumberOfItems, QueueArray)
print ("First value" , DataReturned)
(DataReturned, HeadPointer, TailPointer, NumberOfItems, QueueArray) = Dequeue(HeadPointer, TailPointer, NumberOfItems, QueueArray)
print ("Second value" , DataReturned)