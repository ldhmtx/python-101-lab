def minmpgverify(): #getting user input for what they want to search
    while True:
        try:
            minmpg = float(input('Enter the minimum mpg ==> '))
            if minmpg < 0: # negative values
                print('Fuel economy given must be greater than zero')
                continue
            elif minmpg > 100: #too high of standards
                print('Fuel economy given must be less than 100')
            else:
                return minmpg
        except ValueError: #specifically catching any non-int values
            print('You must enter a number for the fuel economy')

def fordfil(): #opening whatever file is to be searched
    while True:
        try:
            userfil = input('Enter the name of the input vehicle file ==> ')
            bilfil = open(userfil) #checking if correct
            return bilfil
        except FileNotFoundError: #if it cannot be located
            print('Could not open file {}'.format(userfil))

def outfil(): #creating an output file
    while True:
        try:
            userfil = input('Enter the name of the file to output to ==> ')
            outfil = open(userfil,'w') #creates output file
            return outfil
        except IOError:
            print('There is an IO Error {}'.format(userfil))
            
def write(bilfil,outfil,minmpg): #writing to the output file
    for i in bilfil:
        try:
           fordon = i.split('\t') # seperating out the columns
           filmpg = float(fordon[7])
           if filmpg >= minmpg: #actually searching for the value
               outfil.write('{:<5} {:<20}{:<40}{:>10}\n'.format(fordon[0],fordon[1],fordon[2],fordon[7]))
        except ValueError: #if not formated correctly
            if fordon[7]!= 'combinedmpg':
                print('Could not convert value {} for vehicle {} {} {}'.format(fordon[7],fordon[0],fordon[1],fordon[2]))

#main (runs the functions)

minmpg = minmpgverify()
bilfil = fordfil()
outfil = outfil()
write(bilfil,outfil,minmpg)
bilfil.close()
outfil.close()
