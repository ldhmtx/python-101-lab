########################################################################
##
## CS 101 Lab
## Program #4
## Name - Luke Hill
## Email
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

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        player = input('Do you want to play again? ==>') #check if wants to play again
        player=player.lower() #lowercase all input to check
        if player == 'y' or player=='yes':
            return True
        elif player == 'n' or player == 'no':
            return False
        else: #invalid input
            print('You must enter Y/YES/N/NO to continue. Please try again')
            continue
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True: 
        wager = int(input('How many chips would you like to wager?'))
        if wager>bank: #if wager is greater than available amount
            print('The wager amount cannot be greater than the amount you have.')
            continue
        elif wager<0: #if wager is invalid input
            print('The wager amount must be greater than 0')
            continue
        else: #all ready to bet
            break
    return wager           

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1,10)
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)
    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reelb == reelc: #if all 3 match
        return 3
    elif reela == reelb or reelb == reelc or reela == reelc: #if only two match
        return 2
    return 0 #nothing matches

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        banke=int(input('How many chips do you want to start with? ==>'))
        if banke<0: #if user input was negative
            print('Too low a value, you can only choose 1-100 chips')
            continue
        elif banke>100: #if user input was over 100
            print('Too high a value, you can only choose 1-100 chips')
            continue
        else: #valid input
            break
    return banke

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches==3: #calculating payout for all matches
        wager=(wager*10)-wager
    elif matches==2: #if only two match
        wager=(wager*3)-wager
    else: #all 3 numbers are different
        wager=-wager 
    return wager     


if __name__ == "__main__":

    playing = True
    while playing:
        #set default values every time game restarts
        bank = get_bank()
        spins = 0
        origbanke=bank
        topscore=0

        while bank != 0:  #so long as bank is in the green
            spins=spins+1
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()
            
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            #relaying results
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            #setting the highest value the player achieved
            if bank>topscore:
                topscore=bank
        #once game is over, final results relay
        print("You lost all", origbanke, "in", spins, "spins")
        print("The most chips you had was", topscore)
        #check if player wants to play again
        playing = play_again()
