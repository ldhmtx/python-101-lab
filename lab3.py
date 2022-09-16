keep_playing = 'y'

while keep_playing == 'y': #loop if player wants to continue
    print('Welcome to the Flarsheim Guesser!')

    print('Please think of a number between and including 1 and 100.')
    while True:
        rem1 = int(input('What is the remainder when your number is divided by 3 ?'))#first remainder value
        if rem1 < 0: #check if less than zero, invalid input
            print('The value entered must be 0 or greater')
            continue
        elif rem1 > 2:#check if 3 or greater also invalid
            print('The value entered must be less than 3')
            continue
        else: #input is valid
            break #move on to next remainder
    rem2 = int(input('What is the remainder when your number is divided by 5 ?'))
    rem3 = int(input('What is the remainder when your number is divided by 7 ?'))
    while True: #finding the number
        for i in range(1,100):
            guess1 = i % 3 #for each i, finding the remainder
            guess2 = i % 5
            guess3 = i % 7
            if guess1 == rem1 and guess2 == rem2 and guess3 == rem3: #if all the reaminders match to the originals
                print('Your number was',i)
                print('How amazing was that?')
                break #game is completed
            else:
                continue #i wasn't the player chosen value
        break
    while True: #check if player wants to continue
        keep_playing = input('Do you want to play again? Y to continue, N to quit ==>')
        if keep_playing == 'n':
            break
        elif keep_playing == 'y':
            break
        else: #if player enters invalid input, ask again(more aggressively)
            continue
