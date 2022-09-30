########################################################################
##
## CS 101 Lab
## Program #
## Name Luke Hill
## Email ldhmtx@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string #importing libraries

def character_value(self): #returning numbers for specific letters
    chkval = ord(self)
    if (chkval >= 48 and chkval<=57):
        return chkval - 48
    
    elif (chkval >= 65 and chkval<=90):
        return chkval - 65

def get_check_digit(self): #function for the verify_check_digit function, checking to see if correct check digit 
    calc = 0
    for index in range(len(self)): #iterating through entire parameter 
        value = character_value(self[index])
        calc = calc +(value * (index + 1))
    return sum % 10
    
def verify_check_digit(cardnum): #all the semantics in card num
    if len(cardnum) != 10: #verify string length
        return False,'The length of the number given must be 10'

    for index in range(5): #checking for letters in the first half
        if cardnum[index] < 'A' or cardnum[index] > 'Z':
            msg = 'The first 5 characters must be A-Z, the invalid character is at ' + str(index) +' is ' + cardnum[index]
            return False, msg

    for index in range(7,10): #verifying through 7-9
        if cardnum[index] < '9' or cardnum[index] > '0':
            warn = 'The last 3 characters must be 0-9, the invalid character is at ' + str(index) +' is ' + cardnum[index]
            return False, warn

    if cardnum[5] != '1' and cardnum[5] != '2' and cardnum[5] != '3': #verifying through 7-9
        return False, 'The sixth character must be 1 2 or 3'

    if cardnum[6] != '1' and cardnum[6] != '2' and cardnum[6] != '3' and cardnum[6] != '4':#verifying through index 6
        return False, 'The seventh character must be 1 2 3 or 4'

    calculated_value = get_check_digit(cardnum)
    given_value = int(cardnum[9]) # iterating through 9th index to verify correct value
    if given_value != calculated_value:
        warn = 'Check Digit ' + str(given_value) + ' does not match calculated value ' + str(calculated_value) + '.'
        return False , warn
    return True , ''

def get_school(self): #retrieving relevant school info
    for index,char in enumerate(self):
        if index == 5:
            if char == '1':
                return 'School of Computing and Engineering SCE'
            elif char == '2':
                return 'School of Law'
            elif char == '3':
                return 'College of Arts and Sciences'
            else:
                return 'Invalid School'
def get_grade(self): #retrieving relevant grade info
    for index,char in enumerate(self):
        if index == 6:
            if char == '1':
                return 'Freshman'
            elif char == '2':
                return 'Sophomore'
            elif char == '3':
                return 'Junior'
            elif char == '4':
                return 'Senior'
            else:
                return 'Invalid Grade'
        else:
            continue

if __name__ == "__main__":
    print('Linda Hall'.center(66,' '))
    print('Library Card Check'.center(66,' '))
    print('='*66) #just the pretty stuff
    while True: #running all the functions
        library_card = input("\nEnter Library Card. Hit Enter to Exit ==> ")
        (check,string) = verify_check_digit(library_card)
        if check == True:
            print(string)
            print("The card belongs to a student in " + get_school(library_card))
            print("The card belongs to a " + get_grade(library_card))
        else:
            print("Library card is invalid.")
            print(string)
        
