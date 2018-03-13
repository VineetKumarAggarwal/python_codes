#Import the libraries we need for the program
import fileinput

#This is the main function, by declaring a main function and then calling it after all the function definitions
def mainFunction():

    #Step 1 - Ask the user to enter their text message
    print("Please enter the message (no punctuation please):")
    txtMessage = input(">") 

    #Step 2 use the split function to get a list that contains all the words in the text message
    messageWords = txtMessage.split()

    #The translationFileName should contain the name of the file that contains the list of Text message abbreviations
    #and their corresponding translations
    translationFileName = "Translations.txt"

    #call the function we created below to make sure our translation file exists
    # If the file is found it will return a 0
    # If the file is not found it will return a 1
    fileFound = fileCheck(translationFileName)

    if fileFound == 0 :

        #Step 3  Call the function we created below to get back two lists, a list of the abbreviations and a list of the translations
        allAbbreviations, allTranslations = dictionaryList(translationFileName) 

        # Call the function we created below to get back a string containing the translated text message
        translatedMessage = compare(messageWords, allAbbreviations, allTranslations) # the final list of words for the message

        #Step 4) Print the translated message to the user
        print(translatedMessage)
    else : 
        print("Could not translate message, file containing translation terms could not be located.")

#This function will check if a specified file exists.
#If the file exists it will not display any error messages
#If the file does not exist it will display an error message and restart the program.
#Accepts one parameter
#   filename the name of the file to check exists
#Returns one value
#   0 indicates the file was succesfully located
#   1 indicates the file could not be located
def fileCheck(fileName):
    try:
        fileObj = open(fileName) #will try to open the file specified
        return 0
    except IOError: #will handle the exception
        print("Could not locate the file " + fileName)
        return 1

#This function accepts the name of a file that contains abbreviations and translations
def dictionaryList(fileName):

    #Declare the lists to be populated and returned
    allAbbreviations = []
    allTranslations = []

    #open the file
    fileObj = open(fileName)

    for line in iter(fileObj): #This for loop will read the file line by line
        #Take each line in the file and split it into a list of words 
        #LOL - Laughing out Loud will return a list containing ["LOL","-","Laughing","Out","Loud"]
        wordsInTheLine = line.split() 

        #The first word in the list is the abbreviation, add that to our list of allAbbreviations
        allAbbreviations.append(wordsInTheLine[0])

        #Now this is the tricky part because we need to take all the remaining words in the list and together they make up our translation
        # e.g. if the line in the file returned ["LOL","-","Laughing","Out","Loud"]

        translation = ""

        #Find out how many words total are in the line read from the file
        totalNumberOfWords = len(wordsInTheLine)

        #Start with the word at position 2 in the list, this allows us to skip the abbreviation and the hyphen 
        for x in range(2,totalNumberOfWords):
            #now take each word starting with the third word (index 2) until the last word and concatentate them together
            #with a space between each word
            translation = translation + wordsInTheLine[x] + " " 
        
        #add the translation to our list of translations    
        allTranslations.append(translation)

    #return the two lists: the list of abbreviations and the list of translations
    return (allAbbreviations, allTranslations)


#this function will go through each word in the message
def compare(messageWords, allAbbreviations, allTranslations):
    
    finalMessage = ""
    
    # Create a loop that will execute once for each word in our list of words in the text message
    for wordPosition in range(0, len(messageWords)):
        #Fetch the next word from our list of words in the text message
        currentWord = messageWords[wordPosition]

        try :
            #search the abbreviation list for the current word
            matchPosition = allAbbreviations.index(currentWord.upper())

            #If you find a match get the translation from the list of definitions
            finalMessage = finalMessage + " " + allTranslations[matchPosition]
        except :
            #If no match is found by the index() search an exception is raised, which means no match was found
            #If no match was found just display the original word in the final message
            finalMessage = finalMessage + " " + currentWord 
            
    return (finalMessage)

mainFunction()
