import random

#Add word up
def addWordUp(grid, word, dimension):
  row=random.randint(0,dimension)
  column=random.randint(0,dimension)
  canAddWord = False

  while(canAddWord == False):

    canAddWord = True
    for i in range(0, len(word)):
      if(grid[row - i][column] != "-"):
        canAddWord = False

    if(not canAddWord):
        row=random.randint(0,dimension)
        column=random.randint(0,dimension)

  if(canAddWord):
    for i in range(0, len(word)):
      grid[row - i][column] = word[i]

#Add word up-left
def addWordUpLeft(grid, word, dimension):
  row=random.randint(0,dimension)
  column=random.randint(0,dimension)
  canAddWord = False

  while(canAddWord == False):

    canAddWord = True
    for i in range(0, len(word)):
      if(grid[row - i][column - i] != "-"):
        canAddWord = False

    if(not canAddWord):
        row=random.randint(0,dimension)
        column=random.randint(0,dimension)

  if(canAddWord):
    for i in range(0, len(word)):
      grid[row - i][column - i] = word[i]

#Add word up-right
def addWordUpRight(grid, word, dimension):
  row=random.randint(0,dimension)
  column=random.randint(0,dimension)
  canAddWord = False

  while(canAddWord == False):

    canAddWord = True
    for i in range(0, len(word)):
      if(grid[row - i][column + i] != "-"):
        canAddWord = False

    if(not canAddWord):
        row=random.randint(0,dimension)
        column=random.randint(0,dimension)

  if(canAddWord):
    for i in range(0, len(word)):
      grid[row - i][column + i] = word[i]

#Add word down
def addWordDown(grid, word, dimension):
  row=random.randint(0,dimension)
  column=random.randint(0,dimension)
  canAddWord = False

  while(canAddWord == False):

    canAddWord = True
    for i in range(0, len(word)):
      if(grid[row + i][column] != "-"):
        canAddWord = False

    if(not canAddWord):
        row=random.randint(0,dimension)
        column=random.randint(0,dimension)

  if(canAddWord):
    for i in range(0, len(word)):
      grid[row + i][column] = word[i]

#Add word down-left
def addWordDownLeft(grid, word, dimension):
  row=random.randint(0,dimension)
  column=random.randint(0,dimension)
  canAddWord = False

  while(canAddWord == False):

    canAddWord = True
    for i in range(0, len(word)):
      if(grid[row + i][column - i] != "-"):
        canAddWord = False

    if(not canAddWord):
        row=random.randint(0,dimension)
        column=random.randint(0,dimension)

  if(canAddWord):
    for i in range(0, len(word)):
      grid[row + i][column - i] = word[i]

#Add word down-right
def addWordDownRight(grid, word, dimension):
  row=random.randint(0,dimension)
  column=random.randint(0,dimension)
  canAddWord = False

  while(canAddWord == False):

    canAddWord = True
    for i in range(0, len(word)):
      if(grid[row + i][column + i] != "-"):
        canAddWord = False

    if(not canAddWord):
        row=random.randint(0,dimension)
        column=random.randint(0,dimension)

  if(canAddWord):
    for i in range(0, len(word)):
      grid[row + i][column + i] = word[i]

#Add word left
def addWordLeft(grid, word, dimension):
  row=random.randint(0,dimension)
  column=random.randint(0,dimension)
  canAddWord = False

  while(canAddWord == False):

    canAddWord = True
    for i in range(0, len(word)):
      if(grid[row][column - i] != "-"):
        canAddWord = False

    if(not canAddWord):
        row=random.randint(0,dimension)
        column=random.randint(0,dimension)

  if(canAddWord):
    for i in range(0, len(word)):
      grid[row][column - i] = word[i]

#Add word right
def addWordRight(grid, word, dimension):
  row=random.randint(0,dimension)
  column=random.randint(0,dimension)
  canAddWord = False

  while(canAddWord == False):

    canAddWord = True
    for i in range(0, len(word)):
      if(grid[row][column + i] != "-"):
        canAddWord = False

    if(not canAddWord):
        row=random.randint(0,dimension)
        column=random.randint(0,dimension)

  if(canAddWord):
    for i in range(0, len(word)):
      grid[row][column + i] = word[i]


#Replace all "-" (empty characters) with random letters
def fillEmptyFieldInGrid(grid):
  LETTERS="abcdefghijklmnopqrstuvwxyz"
  for row in range(0, len(grid)):
    for col in range(0, len(grid)):
      if grid[row][col]=="-":
        randomLetter = random.choice(LETTERS)
        grid[row][col]=randomLetter


def addWordWithRightOrientation(grid, word, orientation, dimension):
  print(str(orientation))
  if(orientation == 0): #Up
    addWordUp(grid, word, dimension)
  elif(orientation == 1): #Up-Left
    addWordUpLeft(grid, word, dimension)
  elif(orientation == 2): #Up-Right
    addWordUpRight(grid, word, dimension)
  elif(orientation == 3): #Down
    addWordDown(grid, word, dimension)
  elif(orientation == 4): #Down-Left
    addWordDownLeft(grid, word, dimension)
  elif(orientation == 5): #Down-Right
    addWordDownRight(grid, word, dimension)
  elif(orientation == 6): #Leftnew
    addWordLeft(grid, word, dimension)
  elif(orientation == 7): #Right
    addWordRight(grid, word, dimension)

  return True

#Adding words to the grid
def addWordsToTheGrid(grid, dict):
  nbrOfWord = random.randint(200,499)

  wordAdded = []
  for indexOfWordToAdd in range(0, nbrOfWord):
    indexOfWordInDict = random.randint(0,499)
    wordToAdd = dict[indexOfWordInDict]
    orientation = random.randint(0,8)
    if(wordToAdd not in wordAdded):
      wordAdded.append(wordToAdd)
      isAddedSuccessfully = False
      while(isAddedSuccessfully == False):
        try:
          isAddedSuccessfully = addWordWithRightOrientation(grid, wordToAdd, orientation, len(grid))
        except:
          print "Error occured"
          isAddedSuccessfully = False
      print("Word added")
  return wordAdded

#Read dictionnary that contains possible words that we want to have in the grid
def readDict():
  #	print("Enter the name of the dict: ")
  #	filename = raw_input()
	filename = "longwords3.txt"
	return [line.rstrip('\n') for line in open(filename)]

#Print the dictionary
def printDict(dict):
	for i in range(0,len(dict)):
		print(dict[i])

#Create an empty grid N by N (list of lists)
def generateGrid(dimension, dict):
  grid = []
  for row in range(0,dimension):
    grid.append([])
    for col in range(0,dimension):
      grid[row].append("-")
  return grid

#Print the grid
def printGrid(grid):
  print(" " + "_" * (dimension * 2 + 1) + "\n" + "|" + " " * (dimension * 2 + 1) + "|")

  for row in range(0, dimension):
    line = "| "
    for column in range(0, dimension):
            line += str(grid[row][column]) + " "
    line += "|"
    print line
  print("|" + "_" * (dimension * 2 + 1) + "|")

#Write the grid to file to be able to use it in with another program.
def writeGridIntoFile(grid, dimension):
  filename = "grid_" + str(dimension) + ".txt"
  with open (filename, "w+") as f:
    f.write(str(dimension) + "\n")
    for row in range(0, dimension):
      for column in range(0, dimension):
        f.write(grid[row][column])
      f.write("\n")
  print "done writting file"

#Write words of dict to file
def writeDictIntoFile(wordsAdded, dimension):
  filename = "grid_" + str(dimension) + "_wordsContained.txt"
  with open (filename, "w+") as f:
    for wordAdded in wordsAdded:
      f.write(wordAdded + "\n")


print("Dimension of the grid: ")
dimension = int(raw_input())
print("Dimension is " + str(dimension) + " by " + str(dimension))

dict = readDict()

grid = generateGrid(dimension, dict)
wordsAdded = addWordsToTheGrid(grid, dict)
fillEmptyFieldInGrid(grid)
printGrid(grid)

writeGridIntoFile(grid, dimension)
writeDictIntoFile(wordsAdded, dimension)
