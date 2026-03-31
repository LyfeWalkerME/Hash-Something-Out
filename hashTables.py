
#hash table size variable(global)
HASH_TABLE_SIZE = 100

#stores the parsed data index[0] is title index[1] is qoute
MOVIE_TITLE_QOUTE = []

#stores the file name
FILE_NAME = "MOCK_DATA.csv"

#hash table
HASH_TABLE = []

#Creates the table for the linked list method fills out the table with lists of None
def create_table_linked_list():
    for i in range(HASH_TABLE_SIZE):
        HASH_TABLE.append([None])

#Cleans words of special characters using .replace
def cleanWord(string):
    string.replace("!","")
    string.replace('"',"")
    string.replace("(","")
    string.replace(")","")
    string.replace("-","")
    string.replace("_","")
    string.replace(",","")
    string.replace("$","")
    string.replace("'","")
    string.replace("é","e")

    return string

#Opens file, breaks it down into lines, breaks it down into individual strings and cleans the word using the cleanWord method, .strip(), and .lower()
with open(FILE_NAME,"r",encoding="utf-8") as file:
    #Splits up the lines within the file and removes the \n charachters at the end
    lines = file.read().splitlines()
    #splits up the lines by (,), appends the title and movie quoute to a temp list and adds that list to the list of movies
    for line in lines:
        lineSplit = line.split(',')
        tempList = []
        cleanWord(lineSplit[0])
        cleanWord(lineSplit[len(lineSplit)-1])
        #index 0 is the first item and 
        # print(type(lineSplit[0]))
        # print(type(lineSplit[len(lineSplit)-1]))
        tempList.append(lineSplit[0].strip().lower())
        tempList.append(lineSplit[len(lineSplit)-1].strip().lower())
        MOVIE_TITLE_QOUTE.append(tempList)
    

#removes first line containing the title and qoute
MOVIE_TITLE_QOUTE.pop(0)


#creates the hash code for string
def hash_function_attempt_1(string):

    #holds the strings value
    value_of_string = 0

    #adds the value of each charachter in string to string value
    for char in string:
        value_of_string+=ord(char)

    #returns the hash code
    return value_of_string%HASH_TABLE_SIZE

#Adds the movies to the table for the linked list method
#Stores the hash code for the movie in the hash_code variable and then checks to see if the there is already a value in the index of the hash_code
#if there isn't it replaces the None with the movie info, if there is already a movie it appends to the list
#keeps track of collisions 
def add_to_table_linked_list(movie):
    collisions = 0
    for movie in MOVIE_TITLE_QOUTE:
        hash_code = hash_function_attempt_1(movie[0])
        if HASH_TABLE[hash_code][0]==None:
            HASH_TABLE[hash_code][0]=movie
        else:
            HASH_TABLE[hash_code].append(movie)
            collisions += 1
    
    return collisions

#Calculates wasted space for table, returns # of unused indexes
def wasted_space():
    unusedIndexes = 0
    for i in range(HASH_TABLE_SIZE-1):
        if HASH_TABLE[i][0]==None:
            unusedIndexes+=1
    
    return unusedIndexes

