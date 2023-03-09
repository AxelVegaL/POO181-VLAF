import random
import string
lettersmay = string.ascii_letters.upper()
lettersmin = string.ascii_letters.lower()
digits = string.digits
special_chars = string.punctuation

class passwords:
    def __init__(self):
        self.__password = ""
        self.__len = 8

    def juan():
        print('a')

    def createPass(self,leng, mayus, spe):
        self.__len = leng
        if mayus == True and spe == True:
            passPool: lettersmay+lettersmin+digits+special_chars
        elif mayus == True and spe == False:
            passPool: lettersmay+lettersmin
        elif mayus == False and spe == True:
            passPool: lettersmin+digits+special_chars
        else:
            passPool: lettersmin
        self.__password = ''.join(random.choices(passPool,k=self.__len))


    
    #Getters y Setters
    def getLen(self):
        return self.__len
    
    def setLen(self):
        self.__len = lenght