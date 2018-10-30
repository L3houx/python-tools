def createListPrimeNumber(lastPrimeNumber):
    return list(range(2,lastPrimeNumber + 1))

def selectPrimeNumber(listPrimerNumber):
    while len(listPrimerNumber) > 0:
        clonedListPrimeNumber = listPrimerNumber
        index = clonedListPrimeNumber[0]
        primeNumberList.append(index)
        print("primeNumberList append: " + str(primeNumberList))
        listPrimerNumber.remove(index)
        print("listPrimerNumber removed: " + str(listPrimerNumber))

        for j in listPrimerNumber:
            print("i: " + str(index) + " -- j: " + str(j))
            if(j % index == 0):
                listPrimerNumber.remove(j)
                print("removed j: " + str(j) + " from listPrimerNumber: " + str(listPrimerNumber))

def calculateSumPrimeNumberList():
    total = 0
    for i in primeNumberList:
        total += i
    return total

text = input("Find all the prime number between 2 and : ")
primeNumberList = []

try:
    lastPrimeNumber = int(text)
    listPrimerNumber = createListPrimeNumber(lastPrimeNumber)
    selectPrimeNumber(listPrimerNumber)
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("This is the list of prime number between 2 and " + str(lastPrimeNumber) + " => " + str(primeNumberList))
    primeNumberTotal = calculateSumPrimeNumberList()
    print("This is the sum of all prime numbers in the list: " + str(primeNumberTotal))

except Exception as e:
    print("An error occured: " + str(e))
