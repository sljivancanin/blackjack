"""This is a Blackjack game. The program will ask the
user how much money they have and prompt them to bet some.
Then the program will deal the user a hand and play it out.
At the end of each hand the program will ask the user if they
wish to continue playing.

Made by: Mihailo Cvetkovic August 30, 2018.
"""
#This game is played so the dealer hits until 17, dealer also hits on soft 17

'''WHAT TO DO NEXT:
        
        -fix the dealer's hand when he pulls more than 4 cards.
'''



from time import sleep
from random import choice

card_values = {'A':[1,11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J': 10, 'Q':10, 'K':10}
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
number_of_decks = 6
shoe = cards * 4 * number_of_decks 
minimum_bet = 5


def cash_in():
    
    bank = int(input("There is a $%d minimum bet per hand. How much money would you like in chips?: " %minimum_bet))
    while type(bank) != type(5) or bank < 5:
        if type(bank) != type(5):
            bank = int(input("I didn't quite get that. How much money would you like in chips?: "))
        elif bank < minimum_bet:
            bank = int(input("That's less than the minimum betting amount. The minimum bet is $%d. How much money would you like in chips?" % minimum_bet))

        sleep(1)
        print("Here are your chips.")

    return bank


def place_bet(money_in_bank):
    
    sleep(.5)
    bet = int(input("How much would you like to bet?: "))
    
    while bet < minimum_bet or bet > money_in_bank:
        if bet > money_in_bank:
            print("You don't have enough money to make that bet. Make a new bet.")
            bet = int(input("How much would you like to bet?: "))
        else:
            print("That is less than the minimum betting amount. You must bet at least $%d." %minimum_bet) 
            bet = int(input("How much would you like to bet?: "))
    
    return bet


   
def deal_hands():

    player_hand = []
    dealer_hand = []
        
    x = choice(shoe)
    shoe.remove(x)
    player_hand.append(x)
    
    x = choice(shoe)
    shoe.remove(x)
    dealer_hand.append(x)
    
    x = choice(shoe)
    shoe.remove(x)
    player_hand.append(x)

    sleep(1)
    print("Your hand is: (" + str(player_hand[0]) + ',' + str(player_hand[1]) + ').')
    sleep(.5)
    print("The dealer is showing a " + str(dealer_hand[0]))
    return (player_hand, dealer_hand)

def play_turn(money_in_bank, bet):

    hands = deal_hands()
    phand = hands[0]
    dhand = hands[1]
    
    

    if 'A' not in phand:      
        psum = card_values[phand[0]] + card_values[phand[1]]
    elif 'A' in phand and phand[0] == phand[1]:
        psum = [2, 12]
    else:
        non_ace_ind = (phand.index('A') + 1) % 2
        psum = [card_values[phand[non_ace_ind]] + 1, card_values[phand[non_ace_ind]] + 11]

    if 'A' not in dhand:
        dsum = card_values[dhand[0]]
    else:
        dsum = [1, 11]

    #if dealt a pair, offer a split
    if card_values[phand[0]] == card_values[phand[1]]:
        if phand[0] == 'A':
            print("You have double aces, 2 or 12. I suggest you split them.")
            action = input("Choose what wou would like to do. ('hit', 'stay', 'double down', 'split'): ")
        else:
            print("You have %d." %psum)
            action = input("Choose what wou would like to do. ('hit', 'stay', 'double down', 'split'): ")

        while psum != "BJ" and action not in ["hit", "stay", "double down", "split"]:
            action = input("Choose what wou would like to do. ('hit', 'stay', 'double down', 'split'): ")

    #if dealt a nonpair, don't offer a split
    else:
        if 'A' in phand:
            if card_values[phand[0]] == 10 or card_values[phand[1]] == 10:
                sleep(.7)
                print("Blackjack!")
                psum = "BJ"
            else:
                sleep(.7)
                print("You have %d or %d" %(psum[0],psum[1]))
                sleep(.7)
                action = input("Choose what wou would like to do. ('hit', 'stay', 'double down'): ")
        else:
            sleep(.7)
            print("You have %d" %psum)
            sleep(.7)
            action = input("Choose what you would like to do. ('hit, 'stay', 'double down'): ")

        while psum != "BJ" and action not in ["hit", "stay", "double down"]:
            sleep(.7)
            if action == "split":
                action = input("You cannot split your cards, they have different values. Choose what you would like to do. ('hit', 'stay', 'double down'): ")
            else:
                action = input("Choose what wou would like to do. ('hit', 'stay', 'double down'): ")


    while psum != "BJ" and action != "stay":


        if action == "hit":
            split = False
            y = choice(shoe)
            shoe.remove(y)
            phand.append(y)
            sleep(1)
            print(y)
                                #taking care of all the possible cases with ACES
            #dealt a non-ace hand and hit with non-ace card
            if type(psum) == type(50) == type(card_values[y]):
                psum += card_values[y]
                if psum > 21:
                    sleep(.7)
                    print("You have %d" %psum)
                    break
                elif psum == 21:
                    sleep(.7)
                    print("21!")
                    break
                else:
                    sleep(.7)
                    print("You have %d" %psum)
                    sleep(.7)
                    action = input("Choose what wou would like to do. ('hit', 'stay'): ")
                    while action != "hit" and action != "stay":
                        if action == "split":
                            action = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                        elif action == "double down":
                            action = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                        else:
                            action = input("Choose what wou would like to do. ('hit', 'stay'): ")

            #dealt with an ace hand and hit with a non-ace card
            elif type(psum) == type([2, 3, 4, 5]) and type(card_values[y]) == type(50):
                psum = [x+card_values[y] for x in psum]
                if psum[0] < 21 and psum[1] < 21:
                    sleep(.7)
                    print("You have %d or %d" % (psum[0], psum[1]))
                    sleep(.7)
                    action = input("Choose what wou would like to do. ('hit', 'stay'): ")
                    while action != "hit" and action != "stay":
                        if action == "split":
                            action = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                        elif action == "double down":
                            action = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                        else:
                            action = input("Choose what wou would like to do. ('hit', 'stay'): ")
                elif psum[0] == 21 or psum[1] == 21:
                    sleep(.7)
                    print("21!")
                    break
                elif psum[0] > 21 and psum[1] > 21:
                    psum = min(psum)
                    sleep(.7)
                    print("You have %d" %psum)
                    break
                else:
                    sleep(.7)
                    print("You have %d" %min(psum))
                    sleep(.7)
                    action = input("Choose what wou would like to do. ('hit', 'stay'): ")
                    while action != "hit" and action != "stay":
                        if action == "split":
                            action = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                        elif action == "double down":
                            action = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                        else:
                            action = input("Choose what wou would like to do. ('hit', 'stay'): ")

            #deal with a non-ace hand and hit with an ace
            elif type(psum) == type(50) and type(card_values[y]) == type([1, 2, 3]):
                psum = [a+psum for a in card_values[y]]
                if psum[0] < 21 and psum[1] < 21:
                    sleep(.7)
                    print("You have %d or %d" % (psum[0], psum[1]))
                    sleep(.7)
                    action = input("Choose what wou would like to do. ('hit', 'stay'): ")
                    while action != "hit" and action != "stay":
                        if action == "split":
                              action = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                        elif action == "double down":
                            action = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                        else:
                            action = input("Choose what wou would like to do. ('hit', 'stay'): ")
                elif psum[0] == 21 or psum[1] == 21:
                    sleep(.7)
                    print("21!")
                    break
                elif psum[0] > 21 and psum[1] > 21:
                    psum = min(psum)
                    sleep(.7)
                    print("You have %d" %psum)
                    break
                else:
                    sleep(.7)
                    print("You have %d" %min(psum))
                    sleep(.7)
                    action = input("Choose what wou would like to do. ('hit', 'stay'): ")
                    while action != "hit" and action != "stay":
                        if action == "split":
                            action = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                        elif action == "double down":
                            action = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                        else:
                            action = input("Choose what wou would like to do. ('hit', 'stay'): ")

            #deal a hand with an ace and hit with a hand with an ace
            elif type(psum) == type([1, 2, 3, 4]) == type(card_values[y]):
                psum = [a+b for a in psum for b in card_values[y]]
                if psum[0] == 21 or psum[1] == 21 or psum[2] == 21 or psum[3] == 21:
                    sleep(.7)
                    print("21!")
                    break
                else:
                    new_psum = [a for a in psum if a<21]
                    if newpsum == []:
                        psum = min(psum)
                        sleep(.7)
                        print("You have %d" %psum)
                        break
                    else:
                        sleep(.7)
                        print("You have: " + str(new_psum))
                        sleep(.7)
                        action = input("Choose what wou would like to do. ('hit', 'stay'): ")
                        while action != "hit" and action != "stay":
                            if action == "split":
                                action = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                            elif action == "double down":
                                action = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                            else:
                                action = input("Choose what wou would like to do. ('hit', 'stay'): ")
                                           


        #SPLITS
                        
  #      elif action == "split" and (card_values[phand[0]] != card_values[phand[1]] or len(phand) > 2):
   #         split = False
    #        action = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay', 'double down')")


        elif card_values[phand[0]] == card_values[phand[1]] and action == "split":
            split = True
            phand = (phand[0], phand[1])

            phand1 = [phand[0]]
            psum1 = card_values[phand[0]]
            phand2 = [phand[1]]
            psum2 = card_values[phand[1]]
            if type(psum1) == type([1, 2, 3]):
                print("1st hand: %d, or %d" %(psum1[0], psum1[1]))
            else:
                print("1st hand: %d" %psum1)
            sub_action_1 = input("Choose what you would like to do for your 1st hand. ('hit', 'stay'): ")

            #!st split hand
            while sub_action_1 != 'stay':
                if sub_action_1 == "hit":
                    y = choice(shoe)
                    shoe.remove(y)
                    phand1.append(y)
                    sleep(1)
                    print(y)
                                        #taking care of all the possible cases with ACES
                    #dealt a non-ace hand and hit with non-ace card
                    if type(psum1) == type(50) == type(card_values[y]):
                        psum1 += card_values[y]
                        if psum1 > 21:
                            sleep(.7)
                            print("You have %d" %psum1)
                            break
                        elif psum1 == 21:
                            sleep(.7)
                            print("21!")
                            break
                        else:
                            sleep(.7)
                            print("You have %d" %psum1)
                            sleep(.7)
                            sub_action_1 = input("Choose what wou would like to do. ('hit', 'stay'): ")
                            while sub_action_1 != "hit" and action != "stay":
                                if sub_action_1 == "split":
                                    sub_action_1 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_1 == "double down":
                                    sub_action_1 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_1 = input("Choose what wou would like to do. ('hit', 'stay'): ")

                    #dealt with an ace hand and hit with a non-ace card
                    elif type(psum1) == type([2, 3, 4, 5]) and type(card_values[y]) == type(50):
                        psum1 = [x+card_values[y] for x in psum1]
                        if psum1[0] < 21 and psum1[1] < 21:
                            sleep(.7)
                            print("You have %d or %d" % (psum1[0], psum1[1]))
                            sleep(.7)
                            sub_action_1 = input("Choose what wou would like to do for the first hand.. ('hit', 'stay'): ")
                            while sub_action_1 != "hit" and action != "stay":
                                if sub_action_1 == "split":
                                    sub_action_1 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_1 == "double down":
                                    sub_action_1 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_1 = input("Choose what wou would like to do. ('hit', 'stay'): ")
                        elif psum1[0] == 21 or psum1[1] == 21:
                            sleep(.7)
                            print("21!")
                            break
                        elif psum1[0] > 21 and psum1[1] > 21:
                            psum1 = min(psum1)
                            sleep(.7)
                            print("You have %d" %psum1)
                            break
                        else:
                            sleep(.7)
                            print("You have %d" %min(psum1))
                            sleep(.7)
                            sub_action_1 = input("Choose what wou would like to do for your 1st hand. ('hit', 'stay'): ")
                            while sub_action_1 != "hit" and action != "stay":
                                if sub_action_1 == "split":
                                    sub_action_1 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_1 == "double down":
                                    sub_action_1 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_1 = input("Choose what wou would like to do. ('hit', 'stay'): ")

                    #deal with a non-ace hand and hit with an ace
                    elif type(psum1) == type(50) and type(card_values[y]) == type([1, 2, 3]):
                        psum1 = [a+psum1 for a in card_values[y]]
                        if psum1[0] < 21 and psum1[1] < 21:
                            sleep(.7)
                            print("You have %d or %d" % (psum1[0], psum1[1]))
                            sleep(.7)
                            sub_action_1 = input("Choose what wou would like to do for your first hand. ('hit', 'stay'): ")
                            while sub_action_1 != "hit" and action != "stay":
                                if sub_action_1 == "split":
                                    sub_action_1 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_1 == "double down":
                                    sub_action_1 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_1 = input("Choose what wou would like to do. ('hit', 'stay'): ")
                        elif psum1[0] == 21 or psum1[1] == 21:
                            sleep(.7)
                            print("21!")
                            break
                        elif psum1[0] > 21 and psum1[1] > 21:
                            psum1 = min(psum1)
                            sleep(.7)
                            print("You have %d" %psum1)
                            break
                        else:
                            sleep(.7)
                            print("You have %d" %min(psum1))
                            sleep(.7)
                            sub_action_1 = input("Choose what wou would like to do for your first hand. ('hit', 'stay'): ")
                            while sub_action_1 != "hit" and action != "stay":
                                if sub_action_1 == "split":
                                    sub_action_1 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_1 == "double down":
                                    sub_action_1 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_1 = input("Choose what wou would like to do. ('hit', 'stay'): ")

                    #deal a hand with an ace and hit with a hand with an ace
                    elif type(psum1) == type([1, 2, 3, 4]) == type(card_values[y]):
                        psum1 = [a+b for a in psum1 for b in card_values[y]]
                        if psum1[0] == 21 or psum1[1] == 21 or psum1[2] == 21 or psum1[3] == 21:
                            sleep(.7)
                            print("21!")
                            break
                        else:
                            new_psum1 = [a for a in psum1 if a<21]
                            if newpsum1 == []:
                                psum1 = min(psum1)
                                sleep(.7)
                                print("You have %d" %psum1)
                                break
                            else:
                                sleep(.7)
                                print("You have: " + str(new_psum1))
                                sleep(.7)
                                sub_action_1 = input("Choose what wou would like to do for your first hand. ('hit', 'stay'): ")
                                while sub_action_1 != "hit" and action != "stay":
                                    if sub_action_1 == "split":
                                        sub_action_1 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                    elif sub_action_1 == "double down":
                                        sub_action_1 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                    else:
                                        sub_action_1 = input("Choose what wou would like to do. ('hit', 'stay'): ")

                if psum1 == 21 and len(phand1) == 2:
                    print("Blackjack!")
                    psum = "BJ"

            #2nd split hand
            while sub_action_2 != 'stay':
                sleep(.7)
                if type(psum1) == type([1, 2, 3]):
                    print("2nd hand: %d, or %d" %(psum2[0], psum2[1]))
                else:
                    print("2nd hand: %d" %psum2)
                if sub_action_2 == "hit":
                    w = choice(shoe)
                    shoe.remove(w)
                    phand2.append(w)
                    sleep(1)
                    print(w)
                                        #taking care of all the possible cases with ACES
                    #dealt a non-ace hand and hit with non-ace card
                    if type(psum2) == type(50) == type(card_values[w]):
                        psum2 += card_values[w]
                        if psum2 > 21:
                            sleep(.7)
                            print("You have %d" %psum2)
                            break
                        elif psum2 == 21:
                            sleep(.7)
                            print("21!")
                            break
                        else:
                            sleep(.7)
                            print("You have %d" %psum2)
                            sleep(.7)
                            sub_action_2 = input("Choose what wou would like to do for your 2nd hand. ('hit', 'stay'): ")
                            while sub_action_2 != "hit" and action != "stay":
                                if sub_action_2 == "split":
                                    sub_action_2 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_2 == "double down":
                                    sub_action_2 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_2 = input("Choose what wou would like to do. ('hit', 'stay'): ")

                    #dealt with an ace hand and hit with a non-ace card
                    elif type(psum2) == type([2, 3, 4, 5]) and type(card_values[w]) == type(50):
                        psum2 = [x+card_values[w] for x in psum2]
                        if psum2[0] < 21 and psum2[1] < 21:
                            sleep(.7)
                            print("You have %d or %d" % (psum2[0], psum2[1]))
                            sleep(.7)
                            sub_action_2 = input("Choose what wou would like to do for your 2nd hand. ('hit', 'stay'): ")
                            while sub_action_2 != "hit" and action != "stay":
                                if sub_action_2 == "split":
                                    sub_action_2 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_2 == "double down":
                                    sub_action_2 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_2 = input("Choose what wou would like to do. ('hit', 'stay'): ")
                        elif psum2[0] == 21 or psum1[1] == 21:
                            sleep(.7)
                            print("21!")
                            break
                        elif psum2[0] > 21 and psum2[1] > 21:
                            psum2 = min(psum2)
                            sleep(.7)
                            print("You have %d" %psum2)
                            break
                        else:
                            sleep(.7)
                            print("You have %d" %min(psum2))
                            sleep(.7)
                            sub_action_2 = input("Choose what wou would like to do for your 2nd hand. ('hit', 'stay'): ")
                            while sub_action_2 != "hit" and action != "stay":
                                if sub_action_2 == "split":
                                    sub_action_2 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_2 == "double down":
                                    sub_action_2 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_2 = input("Choose what wou would like to do. ('hit', 'stay'): ")

                    #deal with a non-ace hand and hit with an ace
                    elif type(psum2) == type(50) and type(card_values[w]) == type([1, 2, 3]):
                        psum2 = [a+psum2 for a in card_values[w]]
                        if psum2[0] < 21 and psum2[1] < 21:
                            sleep(.7)
                            print("You have %d or %d" % (psum2[0], psum2[1]))
                            sleep(.7)
                            sub_action_2 = input("Choose what wou would like to do for your 2nd hand. ('hit', 'stay'): ")
                            while sub_action_2 != "hit" and action != "stay":
                                if sub_action_2 == "split":
                                    sub_action_2 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_2 == "double down":
                                    sub_action_2 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_2 = input("Choose what wou would like to do. ('hit', 'stay'): ")
                        elif psum2[0] == 21 or psum2[1] == 21:
                            sleep(.7)
                            print("21!")
                            break
                        elif psum2[0] > 21 and psum2[1] > 21:
                            psum2 = min(psum2)
                            sleep(.7)
                            print("You have %d" %psum2)
                            break
                        else:
                            sleep(.7)
                            print("You have %d" %min(psum2))
                            sleep(.7)
                            sub_action_2 = input("Choose what wou would like to do for your 2nd hand. ('hit', 'stay'): ")
                            while sub_action_2 != "hit" and action != "stay":
                                if sub_action_2 == "split":
                                    sub_action_2 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                elif sub_action_2 == "double down":
                                    sub_action_2 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                else:
                                    sub_action_2 = input("Choose what wou would like to do. ('hit', 'stay'): ")

                    #deal a hand with an ace and hit with a hand with an ace
                    elif type(psum2) == type([1, 2, 3, 4]) == type(card_values[w]):
                        psum2 = [a+b for a in psum1 for b in card_values[w]]
                        if psum2[0] == 21 or psum2[1] == 21 or psum2[2] == 21 or psum2[3] == 21:
                            sleep(.7)
                            print("21!")
                            break
                        else:
                            new_psum2 = [a for a in psum2 if a<21]
                            if newpsum2 == []:
                                psum2 = min(psum2)
                                sleep(.7)
                                print("You have %d" %psum2)
                                break
                            else:
                                sleep(.7)
                                print("You have: " + str(new_psum2))
                                sleep(.7)
                                sub_action_2 = input("Choose what wou would like to do for your 2nd hand. ('hit', 'stay'): ")
                                while sub_action_2 != "hit" and action != "stay":
                                    if sub_action_2 == "split":
                                        sub_action_2 = input("You cannot split your cards if your cards have different values or if you have already hit during this hand Choose what you would like to do. ('hit', 'stay')")
                                    elif sub_action_2 == "double down":
                                        sub_action_2 = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")
                                    else:
                                        sub_action_2 = input("Choose what wou would like to do. ('hit', 'stay'): ")

                if psum2 == 21 and len(phand2) == 2:
                    print("Blackjack!")
                    psum = "BJ"
        
        #DOUBLING DOWN

#        elif action == "double down" and len(phand) != 2:
 #           split = False
  #          action = input("You cannot double down after you have already hit. Choose what you would like to so. ('hit', 'stay'): ")

        

        elif action == "double down" and len(phand) == 2:
            split = False
            
            bet *= 2
            y = choice(shoe)
            shoe.remove(y)
            phand.append(y)
            sleep(1.5)
            print(y)

            #dealt a non-ace hand and hit with non-ace card
            if type(psum) == type(50) == type(card_values[y]):
                psum += card_values[y]
                if psum > 21:
                    sleep(.7)
                    print("You have %d" %psum)
                    break
                elif psum == 21:
                    sleep(.7)
                    print("21!")
                    break
                else:
                    sleep(.7)
                    print("You have %d" %psum)
                    break

            #dealt with an ace hand and hit with a non-ace card
            elif type(psum) == type([2, 3, 4, 5]) and type(card_values[y]) == type(50):
                psum = [a+card_values[y] for a in psum]
                if psum[0] < 21 and psum[1] < 21:
                    sleep(.7)
                    print("You have %d" % max(psum))
                    psum = max(psum)
                    break
                elif psum[0] == 21 or psum[1] == 21:
                    sleep(.7)
                    print("21!")
                    psum = 21
                    break
                else:
                    psum = min(psum)
                    sleep(.7)
                    print("You have %d" %psum)
                    break

            #deal with a non-ace hand and hit with an ace
            elif type(psum) == type(50) and type(card_values[y]) == type([1, 2, 3]):
                psum = [a+psum for a in card_values[y]]
                if psum[0] < 21 and psum[1] < 21:
                    sleep(.7)
                    print("You have %d" %max(psum))
                    psum = max(psum)
                elif psum[0] == 21 or psum[1] == 21:
                    sleep(.7)
                    print("21!")
                    psum = 21
                    break
                else:
                    psum = min(psum)
                    sleep(.7)
                    print("You have %d" %psum)
                    break

            #deal a hand with an ace and hit with a hand with an ace
            elif type(psum) == type([1, 2, 3, 4]) == type(card_values[y]):
                psum = [a+b for a in psum for b in card_values[y]]
                if psum[0] == 21 or psum[1] == 21 or psum[2] == 21 or psum[3] == 21:
                    sleep(.7)
                    print("21!")
                    psum = 21
                    break
                else:
                    new_psum = [a for a in psum if a<21]
                    if newpsum == []:
                        psum = min(psum)
                        sleep(.7)
                        print("You have %d" %psum)
                        break
                    else:
                        sleep(.7)
                        print("You have: " +max(new_psum))
                        psum = max(new_psum)
                        break
    #comparing hands if there was NO split
    if type(phand) != type((1, 2, 3)):        
        if type(psum) == type([1, 2, 3]):
            new_psum = [a for a in psum if a < 22]
            psum = max(new_psum)

        if type(psum) == type(5) and psum > 21:
            sleep(.7)
            print("Too high! You lose.")
            money_in_bank -= bet
            return money_in_bank
        
        #if player is dealt BLACKJACK
        elif psum == "BJ":
            if dsum == 10 or dsum == [1, 11]:
                z = choice(shoe)
                shoe.remove(z)
                dhand.append(z)
                print(z)
                if dsum == [11, 21]:
                    sleep(.7)
                    print("The dealer also has blackjack. We are equal.")
                else:
                    sleep(.7)
                    print("You win!")
                    money_in_bank += bet * 1.5
                    return money_in_bank
            else:
                sleep(.7)
                print("Winner winner, chicken dinner!")
                money_in_bank += bet * 1.5
                return money_in_bank

        else:
            print("Dealer's turn:")
            z = choice(shoe)
            shoe.remove(z)
            dhand.append(z)
            sleep(1.1)
            print(z)
            
            if 'A' not in dhand:      
                dsum += card_values[z]

            elif 'A' in dhand and (dhand[0] != dhand[1]):
                non_ace_index = (dhand.index('A') + 1) % 2
                dsum = [card_values[dhand[non_ace_index]] + 1, card_values[dhand[non_ace_index]] + 11]

            else:
                dsum = [2, 12]
            
            
            while type(dsum) == type(50) and dsum < 17:
                z = choice(shoe)
                shoe.remove(z)
                dhand.append(z)
                sleep(1)
                print(z)
                if z != 'A':
                    dsum += card_values[z]
                else:
                    dsum = [dsum + 1, dsum + 11]

            while type(dsum) == type([1, 2, 3]) and ((dsum[0] < 18  and dsum[1] < 18) or (dsum[0] < 18  and dsum[1] > 21) or (dsum[0] > 21  and dsum[1] < 18)):
                z = choice(shoe)
                shoe.remove(z)
                dhand.append(z)
                sleep(1)
                print(z)
                if z != 'A':
                    dsum = [dsum[0] + card_values[z], dsum[1] + card_values[z]] 
                else:
                    dsum = [a+b for a in dsum for b in card_values[z]]
                    dsum = [a for a in dsum if a < 22]    #This may be incorrect. What if there are 3 possible options????? Then the while loop will give an error.

            #comparing hands if dsum is integer
            if type(dsum) == type(50):
                if dsum > 21:
                    sleep(.7)
                    print("Total: %d" %dsum)
                    sleep(.3)
                    print("Over. You win.")
                    money_in_bank += bet
                    return money_in_bank
                else:
                    if psum > dsum:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("You win.")
                        money_in_bank += bet
                        return money_in_bank
                    elif psum < dsum:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("You lose.")
                        money_in_bank -= bet
                        return money_in_bank
                    else:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("We are equal")
                        return money_in_bank

            #comparing hands if dsum is a list (ACES)
            elif type(dsum) == type([1, 2, 3]):
                dsum_int = 0
                for item in dsum:
                    if item <= 21 and item > dsum_int:
                        dsum_int = item
                if dsum_int == 0:        #this means that all items in dsum are over 21
                    sleep(.7)
                    print("Total: %d" % min(dsum))
                    sleep(.3)
                    print("You win.")
                    money_in_bank += bet
                    return money_in_bank
                else:
                    if psum > dsum_int:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("You win.")
                        money_in_bank += bet
                        return money_in_bank
                    elif psum < dsum_int:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("You lose.")
                        money_in_bank -= bet
                        return money_in_bank
                    else:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("We are equal")
                        return money_in_bank

        
    #Comparing hands if there was a split
    else:
        ##Comparing hand1 with dealer's hand
        if type(psum1) == type([1, 2, 3]):
            new_psum1 = [a for a in psum1 if a < 22]
            psum1 = max(new_psum1)

        if type(psum1) == type(5) and psum1 > 21:
            sleep(.7)
            print("Too high! You lose.")
            money_in_bank -= bet
            return money_in_bank

        elif psum1 == "BJ":
            if dsum == 10 or dsum == [1, 11]:
                z = choice(shoe)
                shoe.remove(z)
                dhand.append(z)
                print(z)
                if dsum == [11, 21]:
                    sleep(.7)
                    print("The dealer also has blackjack. We are equal.")
                else:
                    sleep(.7)
                    print("You win!")
                    money_in_bank += bet * 1.5
                    return money_in_bank
            else:
                sleep(.7)
                print("Winner winner, chicken dinnery!")
                money_in_bank += bet * 1.5
                return money_in_bank

        else:
            print("Dealer's turn:")
            z = choice(shoe)
            shoe.remove(z)
            dhand.append(z)
            sleep(1.1)
            print(z)
            
            if 'A' not in dhand:      
                dsum += card_values[z]

            elif 'A' in dhand and (dhand[0] != dhand[1]):
                non_ace_index = (dhand.index('A') + 1) % 2
                dsum = [card_values[dhand[non_ace_index]] + 1, card_values[dhand[non_ace_index]] + 11]

            else:
                dsum = [2, 12]
            
            
            while type(dsum) == type(50) and dsum < 17:
                z = choice(shoe)
                shoe.remove(z)
                dhand.append(z)
                sleep(1)
                print(z)
                if z != 'A':
                    dsum += card_values[z]
                else:
                    dsum = [dsum + 1, dsum + 11]

            while type(dsum) == type([1, 2, 3]) and ((dsum[0] < 18  and dsum[1] < 18) or (dsum[0] < 18  and dsum[1] > 21) or (dsum[0] > 21  and dsum[1] < 18)):
                z = choice(shoe)
                shoe.remove(z)
                dhand.append(z)
                sleep(1)
                print(z)
                if z != 'A':
                    dsum = [dsum[0] + card_values[z], dsum[1] + card_values[z]] 
                else:
                    dsum = [a+b for a in dsum for b in card_values[z]]
                    dsum = [a for a in dsum if a < 22]    #This may be incorrect. What if there are 3 possible options????? Then the while loop will give an error.

            #comparing hands if dsum is integer
            if type(dsum) == type(50):
                if dsum > 21:
                    sleep(.7)
                    print("Total: %d" %dsum)
                    sleep(.3)
                    print("Over. You win.")
                    money_in_bank += bet
                    return money_in_bank
                else:
                    if psum1 > dsum:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("You win.")
                        money_in_bank += bet
                        return money_in_bank
                    elif psum1 < dsum:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("You lose.")
                        money_in_bank -= bet
                        return money_in_bank
                    else:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("We are equal")
                        return money_in_bank

            #comparing hands if dsum is a list (ACES)
            elif type(dsum) == type([1, 2, 3]):
                dsum_int = 0
                for item in dsum:
                    if item <= 21 and item > dsum_int:
                        dsum_int = item
                if dsum_int == 0:        #this means that all items in dsum are over 21
                    sleep(.7)
                    print("Total: %d" % min(dsum))
                    sleep(.3)
                    print("You win.")
                    money_in_bank += bet
                    return money_in_bank
                else:
                    if psum1 > dsum_int:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("You win.")
                        money_in_bank += bet
                        return money_in_bank
                    elif psum1 < dsum_int:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("You lose.")
                        money_in_bank -= bet
                        return money_in_bank
                    else:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("We are equal")
                        return money_in_bank


        
        #Comparing hand2 with dealer's hand   
        if type(psum2) == type([1, 2, 3]):
            new_psum2 = [a for a in psum2 if a < 22]
            psum2 = max(new_psum2)

        if type(psum2) == type(5) and psum2 > 21:
            sleep(.7)
            print("Too high! You lose.")
            money_in_bank -= bet
            return money_in_bank

        #if plazer is dealt BLACKJACK
        elif psum2 == "BJ":
            if len(dhand) == 1 and (dsum == 10 or dsum == [1, 11]):
                z = choice(shoe)
                shoe.remove(z)
                dhand.append(z)
                print(z)
                if dsum == [11, 21]:
                    sleep(.7)
                    print("The dealer also has blackjack. We are equal.")
                else:
                    sleep(.7)
                    print("You win!")
                    money_in_bank += bet * 1.5
                    return money_in_bank
            elif len(dhand) == 2 and dsum == 21:
                sleep(.5)
                print("The dealer also has blackjack. We are equal.")
            else:
                sleep(.7)
                print("Winner winner, chicken dinner!")
                money_in_bank += bet * 1.5
                return money_in_bank

        #if both split hand didnt bust and dealer hasnt hit yet after comparing 1st hand
        if (psum1 <= 21 or psum2 <= 21) and len(dhand) == 1:
            print("Dealer's turn:")
            z = choice(shoe)
            shoe.remove(z)
            dhand.append(z)
            sleep(1.1)
            print(z)
            
            if 'A' not in dhand:      
                dsum += card_values[z]

            elif 'A' in dhand and (dhand[0] != dhand[1]):
                non_ace_index = (dhand.index('A') + 1) % 2
                dsum = [card_values[dhand[non_ace_index]] + 1, card_values[dhand[non_ace_index]] + 11]

            else:
                dsum = [2, 12]
            
            
            while type(dsum) == type(50) and dsum < 17:
                z = choice(shoe)
                shoe.remove(z)
                dhand.append(z)
                sleep(1)
                print(z)
                if z != 'A':
                    dsum += card_values[z]
                else:
                    dsum = [dsum + 1, dsum + 11]

            while type(dsum) == type([1, 2, 3]) and ((dsum[0] < 18  and dsum[1] < 18) or (dsum[0] < 18  and dsum[1] > 21) or (dsum[0] > 21  and dsum[1] < 18)):
                z = choice(shoe)
                shoe.remove(z)
                dhand.append(z)
                sleep(1)
                print(z)
                if z != 'A':
                    dsum = [dsum[0] + card_values[z], dsum[1] + card_values[z]] 
                else:
                    dsum = [a+b for a in dsum for b in card_values[z]]
                    dsum = [a for a in dsum if a < 22]    #This may be incorrect. What if there are 3 possible options????? Then the while loop will give an error.

            #comparing hands if dsum is integer
            if type(dsum) == type(50):
                if dsum > 21:
                    sleep(.7)
                    print("Total: %d" %dsum)
                    sleep(.3)
                    print("Over. You win.")
                    money_in_bank += bet
                    return money_in_bank
                else:
                    if psum2 > dsum:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("You win.")
                        money_in_bank += bet
                        return money_in_bank
                    elif psum2 < dsum:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("You lose.")
                        money_in_bank -= bet
                        return money_in_bank
                    else:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("We are equal")
                        return money_in_bank

            #comparing hands if dsum is a list (ACES)
            elif type(dsum) == type([1, 2, 3]):
                dsum_int = 0
                for item in dsum:
                    if item <= 21 and item > dsum_int:
                        dsum_int = item
                if dsum_int == 0:        #this means that all items in dsum are over 21
                    sleep(.7)
                    print("Total: %d" % min(dsum))
                    sleep(.3)
                    print("You win.")
                    money_in_bank += bet
                    return money_in_bank
                else:
                    if psum2 > dsum_int:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("You win.")
                        money_in_bank += bet
                        return money_in_bank
                    elif psum2 < dsum_int:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("You lose.")
                        money_in_bank -= bet
                        return money_in_bank
                    else:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("We are equal")
                        return money_in_bank
        

        else:
            if type(dsum) == type(50):
                if dsum > 21:
                    sleep(.7)
                    print("Total: %d" %dsum)
                    sleep(.3)
                    print("Over. You win.")
                    money_in_bank += bet
                    return money_in_bank
                else:
                    if psum2 > dsum:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("You win.")
                        money_in_bank += bet
                        return money_in_bank
                    elif psum2 < dsum:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("You lose.")
                        money_in_bank -= bet
                        return money_in_bank
                    else:
                        sleep(.7)
                        print("Total: %d" %dsum)
                        sleep(.3)
                        print("We are equal")
                        return money_in_bank

            #comparing hands if dsum is a list (ACES)
            elif type(dsum) == type([1, 2, 3]):
                dsum_int = 0
                for item in dsum:
                    if item <= 21 and item > dsum_int:
                        dsum_int = item
                if dsum_int == 0:        #this means that all items in dsum are over 21
                    sleep(.7)
                    print("Total: %d" % min(dsum))
                    sleep(.3)
                    print("You win.")
                    money_in_bank += bet
                    return money_in_bank
                else:
                    if psum2 > dsum_int:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("You win.")
                        money_in_bank += bet
                        return money_in_bank
                    elif psum2 < dsum_int:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("You lose.")
                        money_in_bank -= bet
                        return money_in_bank
                    else:
                        sleep(.7)
                        print("Total: %d" %dsum_int)
                        sleep(.3)
                        print("We are equal")
                        return money_in_bank
            


    
'''
    #if player is dealt BLACKJACK
    elif psum == "BJ":
        if dsum == 10 or dsum == [1, 11]:
            z = choice(shoe)
            shoe.remove(z)
            dhand.append(z)
            print(z)
            if dsum == [11, 21]:
                sleep(.7)
                print("The dealer also has blackjack. We are equal.")
            else:
                sleep(.7)
                print("You win!")
                money_in_bank += bet * 1.5
                return money_in_bank
        else:
            sleep(.7)
            print("Winner winner, chicken dinner!")
            money_in_bank += bet * 1.5
            return money_in_bank

    else:
        print("Dealer's turn:")
        z = choice(shoe)
        shoe.remove(z)
        dhand.append(z)
        sleep(1.1)
        print(z)
        
        if 'A' not in dhand:      
            dsum += card_values[z]

        elif 'A' in dhand and (dhand[0] != dhand[1]):
            non_ace_index = (dhand.index('A') + 1) % 2
            dsum = [card_values[dhand[non_ace_index]] + 1, card_values[dhand[non_ace_index]] + 11]

        else:
            dsum = [2, 12]
        
        
        while type(dsum) == type(50) and dsum < 17:
            z = choice(shoe)
            shoe.remove(z)
            dhand.append(z)
            sleep(1)
            print(z)
            if z != 'A':
                dsum += card_values[z]
            else:
                dsum = [dsum + 1, dsum + 11]

        while type(dsum) == type([1, 2, 3]) and ((dsum[0] < 18  and dsum[1] < 18) or (dsum[0] < 18  and dsum[1] > 21) or (dsum[0] > 21  and dsum[1] < 18)):
            z = choice(shoe)
            shoe.remove(z)
            dhand.append(z)
            sleep(1)
            print(z)
            if z != 'A':
                dsum = [dsum[0] + card_values[z], dsum[1] + card_values[z]] 
            else:
                dsum = [a+b for a in dsum for b in card_values[z]]
                dsum = [a for a in dsum if a < 22]    #This may be incorrect. What if there are 3 possible options????? Then the while loop will give an error.

        #comparing hands if dsum is integer
        if type(dsum) == type(50):
            if dsum > 21:
                sleep(.7)
                print("Total: %d" %dsum)
                sleep(.3)
                print("Over. You win.")
                money_in_bank += bet
                return money_in_bank
            else:
                if psum > dsum:
                    sleep(.7)
                    print("Total: %d" %dsum)
                    sleep(.3)
                    print("You win.")
                    money_in_bank += bet
                    return money_in_bank
                elif psum < dsum:
                    sleep(.7)
                    print("Total: %d" %dsum)
                    sleep(.3)
                    print("You lose.")
                    money_in_bank -= bet
                    return money_in_bank
                else:
                    sleep(.7)
                    print("Total: %d" %dsum)
                    sleep(.3)
                    print("We are equal")
                    return money_in_bank

        #comparing hands if dsum is a list (ACES)
        elif type(dsum) == type([1, 2, 3]):
            dsum_int = 0
            for item in dsum:
                if item <= 21 and item > dsum_int:
                    dsum_int = item
            if dsum_int == 0:        #this means that all items in dsum are over 21
                sleep(.7)
                print("Total: %d" % min(dsum))
                sleep(.3)
                print("You win.")
                money_in_bank += bet
                return money_in_bank
            else:
                if psum > dsum_int:
                    sleep(.7)
                    print("Total: %d" %dsum_int)
                    sleep(.3)
                    print("You win.")
                    money_in_bank += bet
                    return money_in_bank
                elif psum < dsum_int:
                    sleep(.7)
                    print("Total: %d" %dsum_int)
                    sleep(.3)
                    print("You lose.")
                    money_in_bank -= bet
                    return money_in_bank
                else:
                    sleep(.7)
                    print("Total: %d" %dsum_int)
                    sleep(.3)
                    print("We are equal")
                    return money_in_bank
'''        
              
def start_game(shoe):
    
    commence = False
    start = input("Would you like to play Blackjack? (y/n): ")
    
    while commence != True:

        if start.lower() == 'y' or start.lower() == 'yes':
            sleep(.1)
            print("Let's play!")
            commence = True

        elif start.lower() == 'n' or start.lower() == 'no':
            sleep(.1)
            print("Alright.")
            break

        else:
            print("I'm sorry, I didn't quite get that.")
            start = input("Would you like to play Blackjack? (y/n): ")

    if commence == False:
        pass

    else:
        
        player_bank = cash_in()
        
        play_hand = True
        while play_hand == True and player_bank >= minimum_bet:

            if len(shoe) < 12:
                sleep(.5)
                print("One moment. The shoe is empty. We must reshuffle the cards")
                sleep(1)
                print("....Ssssrrpt....Ssssrrpt")
                sleep(.5)
                print("....Ssssrrpt....Ssssrrpt")
                shoe = cards * 4 * number_of_decks
            else:
                bet = place_bet(player_bank)
                player_bank = play_turn(player_bank, bet)
                play_hand = input("You have $%d. Would you like to play another hand? (y/n): " %player_bank)
                while play_hand.lower() != 'y' and play_hand.lower() != 'yes' and play_hand.lower() != 'n' and play_hand.lower() != 'no':
                    play_hand = input("I'm sorry I didn't quite get that. You have $%d. Would you like to play another hand? (y/n): " %player_bank)
                if play_hand.lower() == 'y' or play_hand.lower() == 'yes':
                    play_hand = True
                elif play_hand.lower() == 'n' or play_hand.lower() == 'no':
                    sleep(.7)
                    print("See you next time.")

        if player_bank < minimum_bet:
            sleep(.7)
            print("You gambled all your money away.... better luck next time sucker. See ya bud.")


start_game(shoe)
