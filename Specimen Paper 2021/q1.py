TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(TheData):
    for Count in range(0, len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1

def PrintArray(TheData):
    for Count in range(0, len(TheData)):
        print(TheData[Count])


print("Array before sorting: ")
PrintArray(TheData)

InsertionSort(TheData)
print("Array after sorting: ")
PrintArray(TheData)

def SearchArray(TheData):
    SearchValue = int(input("Enter number to search for: "))
    for Count in range(0, len(TheData)):
        if TheData[Count] == SearchValue:
            print("found")
            return True
    print("not found")
    return False


SearchArray(TheData)
