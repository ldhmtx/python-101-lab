import math

def menu():
    x = '1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit\n'
    print(x)
def addtest(): #user adding test
    while True:
        try:
            tempscore = float(input('Enter the new test score 0-100 ==> '))
            if tempscore < 0: # if negative value
                return addtest()
            else:
                prov.append(tempscore)
                break
        except ValueError: #invalid input
            print('Invalid input, please try again.')
            return addtest()
def addassign(): # user adding an assignment
    while True:
        try:
            tempscore = float(input('Enter the new assignment score 0-100 ==> '))
            if tempscore < 0: # if negative value
                print('Score cannot be less than zero.')
                return addassign()
            else:
                assign.append(tempscore)
                break
        except ValueError: #invalid input
            print('Invalid input, please try again.')
            return addassign()
def removetest(): # user removing a test
    while True:
        try:
            temprem = float(input('Enter the test to remove 0-100 ==> '))
            if temprem in prov: #iff found
                prov.remove(temprem)
                break
            else:
                print('Could not find that score to remove')
                return removetest()
        except ValueError: #invalid input
            print('Invalid input, please try again.')
            return removetest()
def removeassign(): # user removing an assignment
    while True:
        try:
            temprem = float(input('Enter the assignment to remove 0-100 ==> '))
            if temprem in assign: #iff found
                assign.remove(tempscore)
                break
            else:
                print('Could not find that score to remove')
                return removeassign()
        except ValueError: #invalid input
            print('Invalid input, please try again.')
            return removeassign()
def clear(thelist): #clears whatever passed to it
    thelist.clear()
def display(p,a):
    print('{:<15}{:^10}{:^10}{:^10}{:^10}{:^5}'.format('Type','#','min','max','avg','std'))
    print('='*60)
    print('{:<15}{:^10}{:^10}{:^10}{:^10}{:^5}'.format('Tests',len(p),minimum(p),maximum(p),medel(p),std(p)))
    print('{:<15}{:^10}{:^10}{:^10}{:^10}{:^5}'.format('Programs',len(a),minimum(a),maximum(a),medel(a),std(a)))
    
def minimum(x): #find min value
    try:
        return float(min(x))
    except:
        return 'n/a'
def maximum(x): # find max value
    try:
        return float(max(x))
    except:
        return 'n/a'
def medel(x): # finding the average value
    try:
        avg = sum(x)/len(x)
        return '{:.2f}'.format(avg)
    except:
        return 'n/a'
def std(x): #standard deviation
    try:
        summ = 0
        stdavg = sum(x)/len(x)
        for vard in x:
            temp = (vard - stdavg) ** 2
            summ += temp
        final = math.sqrt(summ)
        return '{:.2f}'.format(final)
    except:
        return 'n/a'
    
def weight(x,y): #find total weighted value
    if medel(x) == 'n/a': #if no values for tests
        mp = 0
    else:
        mp = medel(x)
    if medel(y) == 'n/a': #if no values for assignments
        ma = 0
    else:
        ma = medel(y)
    weightprov = float(mp) *0.6
    weightassign = float(ma) *0.4
    finalpoang = weightprov + weightassign #adding together
    print('The weighted score is {:.2f}'.format(finalpoang))

prov = [] #list for tests
assign = [] #list for assignments

funga = True
while funga: #while user wants to use
    menu()
    valg = input('==> ')
    if valg == '1':
        addtest()
    elif valg == '2':
        removetest()
    elif valg == '3':
        clear(prov)
    elif valg == '4':
        addassign()
    elif valg == '5':
        removeassign()
    elif valg == '6':
        clear(assign)
    elif valg == 'D' or valg == 'd':
        display(prov,assign)
        weight(prov,assign)
    elif valg == 'Q' or valg == 'q':
        funga = False #ending the loop
    else:
        print('Invalid input, please try again.') #input validation
