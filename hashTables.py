
import time


#hash table size variable(global)
HASH_TABLE_SIZE = 15000

#stores the parsed data index[0] is title index[1] is qoute
MOVIE_INFO = []

#stores the file name
FILE_NAME = "MOCK_DATA.csv"

#hash tableS
HASH_TABLE_MOVIE_TITLE = []
HASH_TABLE_MOVIE_QOUTE = []

#Creates the table for the linked list method fills out the table with lists of None
def create_table_linked_list():
    for i in range(HASH_TABLE_SIZE):
        HASH_TABLE_MOVIE_TITLE.append([None])
        HASH_TABLE_MOVIE_QOUTE.append([None])

#Cleans words of special characters using .replace
def cleanWord(string):
    string.replace("!"," ")
    string.replace('"'," ")
    string.replace("("," ")
    string.replace(")"," ")
    string.replace("-"," ")
    string.replace("_"," ")
    string.replace(","," ")
    string.replace("$"," ")
    string.replace("'"," ")
    string.replace("é","e")

    return string

#creates the hash code for string(attempt 1)
#Calculates the total value of the string of the key, modulos it by the size of the hash table and returns the code
def hash_function_attempt_1(string):

    #holds the strings value
    value_of_string = 0

    #adds the value of each charachter in string to string value
    for char in string:
        value_of_string+=ord(char)

    #returns the hash code
    return value_of_string%HASH_TABLE_SIZE


#creates the hash code for string(attempt 2)
def hash_function_attempt_2(string):

    #holds the strings value
    value_of_string = 0

    #Stores the value of index of the char in the list 
    index = 0
    #adds the value of each charachter in string to string value
    for char in string:
        if index<2:
            value_of_string+=ord(char)*19
        elif index<3:
            value_of_string+=ord(char)*23
        elif index<7:
            value_of_string+=ord(char)*29
        elif index<11:
            value_of_string+=ord(char)*31
        elif index<13:
            value_of_string+=ord(char)*37
        elif index<17:
            value_of_string+=ord(char)*41
        else:
            value_of_string+=ord(char)*43

    #multiplies by len of string to create even greater difference
    value_of_string = (value_of_string*len(string))


    #returns the hash code
    return value_of_string%HASH_TABLE_SIZE

#Adds the movies to the table for the linked list method
#Stores the hash code for the movie in the hash_code variable and then checks to see if the there is already a value in the index of the hash_code
#if there isn't it replaces the None with the movie info, if there is already a movie it appends to the list
#keeps track of collisions 

def add_to_table_linked_list():
    collisions_title = 0
    collisions_qoute = 0
    # index = 1
    for movie in MOVIE_INFO:
        #adds movie based on title
        hash_code_title = hash_function_attempt_1(cleanWord(movie[0]))
        hash_code_qoute = hash_function_attempt_1(cleanWord(movie[len(movie)-1]))
        # if index<100:
        #     print(f"{index}:{hash_code_title}")
        #Adds the movie to the hash table based on title as key
        if HASH_TABLE_MOVIE_TITLE[hash_code_title][0]==None:
            HASH_TABLE_MOVIE_TITLE[hash_code_title][0]=movie
        else:
            HASH_TABLE_MOVIE_TITLE[hash_code_title].append(movie)
            collisions_title += 1

        #Adds movie to to the hash table based on qoute
        if HASH_TABLE_MOVIE_QOUTE[hash_code_qoute][0]==None:
            HASH_TABLE_MOVIE_QOUTE[hash_code_qoute][0]=movie
        else:
            HASH_TABLE_MOVIE_QOUTE[hash_code_qoute].append(movie)
            collisions_qoute += 1
        # index+=1
    
    return collisions_title, collisions_qoute


#Calculates wasted space for table, returns # of unused indexes
def wasted_space(hashTable):
    unusedIndexes = 0
    for i in range(HASH_TABLE_SIZE-1):
        if hashTable[i][0]==None:
            unusedIndexes+=1
    
    return unusedIndexes

#finds an item in the the hash table
def findItem(movie):
    #found item
    movieInfo = HASH_TABLE_MOVIE_TITLE[hash_function_attempt_2(movie)]

    print(movieInfo)

    return
def main():
    #Opens file, breaks it down into lines, breaks it down into individual strings and cleans the word using the cleanWord method, .strip(), and .lower()
    with open(FILE_NAME,"r",encoding="utf-8") as file:
        #Splits up the lines within the file and removes the \n charachters at the end
        lines = file.read().splitlines()
        #splits up the lines by (,), appends the title and movie quoute to a temp list and adds that list to the list of movies
        for line in lines:
            lineSplit = line.split(',')
            tempList = []
            for word in lineSplit:
                #adds word to tempList to keep movie info together 
                # print(type(lineSplit[0]))
                # print(type(lineSplit[len(lineSplit)-1]))
                tempList.append(word)
            #adds movie to MOVIE_INFO once cleaned
            MOVIE_INFO.append(tempList)
    
    #removes first line containing the title and qoute
    MOVIE_INFO.pop(0)
    
    create_table_linked_list()

    #Start timer
    start = time.time()

    #adds the movies to the hash table and returns the amount of collisions
    collisions_title,collisions_qoute = add_to_table_linked_list()

    #ends timer
    end=time.time()
    
    #found movie checks
    # findItem(MOVIE_INFO[1000][0])
    # findItem(MOVIE_INFO[4000][0])
    # findItem(MOVIE_INFO[7000][0])
    # findItem(MOVIE_INFO[10000][0])

    #Unused space/wasted space
    unused_space_title = wasted_space(HASH_TABLE_MOVIE_TITLE)
    qoute = wasted_space(HASH_TABLE_MOVIE_QOUTE)

    #prints time it took to complete operations
    print(f"Time to complete: {end-start}")

    #prints wasted space
    print(f"Unused space in title table: {unused_space_title}")
    print(f"Unused space in qoute table: {unused_space_title}")

    print(f"Collisions_title: {collisions_title}")
    print(f"Collisions_qoute: {collisions_qoute}")

    # print(HASH_TABLE_MOVIE_TITLE[10:20])

main()