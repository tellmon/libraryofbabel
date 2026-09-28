import random
import time

allCharictors = {1:' ', 2:'.', 3:',', 4:'a', 5:'b', 6:'c', 7:'d', 8:'e', 9:'f', 10:'g', 11:'h', 12:'i', 13:'j', 14:'k', 15:'l', 16:'m', 17:'n', 18:'o', 19:'p', 20:'q', 21:'r', 22:'s', 23:'t', 24:'u', 25:'v', 26:'w', 27:'x', 28:'y', 29:'z'}

savedVolumes = []

def genletter():
    randnum = random.randint(1, 29)

    return allCharictors[randnum]

def bookTitle():
    title = ""
    for i in range(0, 26):
        title += genletter()
        
    return title

def genLine():
    line = ""
    for i in range(0, 80):
        line += genletter()
    
    return line

def genPage():
    page = ""
    
    for i in range(0, 40):
        page += genLine()
        page += "\n"
        
    return page

def genBook():
    book = ""
    
    for i in range(0, 410):
        book += genPage()
        
    return book

def searchForWords():

    sentanceToFind = input("what to find> ")
    print("it may take a long time")

    found = False
    attempt = 0
    start_time = time.time()

    while(not found):
        book = genBook()
        attempt += 1
        if (sentanceToFind in book):
            found = True
        
    print(book)
    print("found on attempt " + str(attempt) + ", it took the following seconds")
    print("--- %s seconds ---" % (time.time() - start_time))
    input("\n\n\nPress enter to go back")
    menu()

def shelf():
    shelfDic = {}
    bookTitleList = []
    
    for i in range(0, 35):
        title = bookTitle()
        book = genBook()
        shelfDic[title] = book
        bookTitleList.append(title)
    
    searchShelf(shelfDic, bookTitleList)
    
def searchShelf(shelfDic, bookList):
    count = 1
    for i in bookList:
        print(str(count) +": "+ i)
        count += 1
        
    titleToSelect = input("what book do you want to open > ")
    titleToSelect = int(titleToSelect)
    titleToSelect -= 1
    
    print(shelfDic[bookList[titleToSelect]])
    
    takeBook = input("\n\n\nTake this book (Yes/No)> ")
    if("Yes" in takeBook):
        savedVolumes.append([bookList[titleToSelect], shelfDic[bookList[titleToSelect]]])
        print(savedVolumes)
        print("\nSaved")
        
    input("\n\n\nPress enter to go back")
    generateRoom()

def generateBookCase():
    
    listOfBooks = ""
    
    for i in range(1, 6):
        listOfBooks += str(i) + ": |||||| \n"
    
    print(listOfBooks)
    
    getShelf = input("what shelf to use > ")
    shelf()
    
def generateRoom():
    print("""
    __
1  /  \\  2
  /    \\
 |      |
 |      |
  \\    /
3  \\__/  4

""")
    
    getShelf = input("""
what do you want to do:
1. Book shelf 1
2. Book Shelf 2
3. Book Shelf 3
4. Book shelf 4
5. go left
6. go right
7. go up a floor 
8. go down a floor
9. Bed and Bathroom
""")
    
    getShelf = int(getShelf)
    
    if(getShelf < 5):
        generateBookCase()
        
    elif(getShelf > 4 and getShelf < 9):
        generateRoom()
        
    else:
        bedAndBath()
    
def bedAndBath():
    print("""
___________
| |x|x|x| |
|         |
|        /
|##      \\
|       ##|
|##       |
|_______##|
""")
    
    ans = input("Do you wnat to save all books picked up (Yes/No) >")
    
    if ("Yes" in ans):
        save()
        
    else:
        menu()

def save():
    for i in range (len(savedVolumes)):
        title = savedVolumes[i][0]
        book = savedVolumes[i][1]
        
        file = open(title+".txt", "w")
        file.write(book)
        file.close()
        
    savedVolumes.clear()
    menu()

def menu():
    option = input("""
what do you want to do:
1. Search
2. Find random book case
3. exit
> """)
    
    if(option == "1"):
        searchForWords()
    
    elif(option == "2"):
        generateRoom()
    
    else:
        exit()
        
menu()