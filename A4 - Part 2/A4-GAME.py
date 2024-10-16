# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

# Course: IT1 1120
# Assignment number: 4
# Chantiri, Majd


import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     a = 0 
     for i in range(26):
             a = a + 1
             dealer.append(deck[i])

     b = 0
     for i in range(26, 51):
             b = b + 1
             other.append(deck[i])
         
     
     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    
    l.sort()

    for j in range(len(l)):
        no_pairs.append(l[j])
        
    i = -1
    while ( (no_pairs != []) and (i <= (len(no_pairs)-1)) ):
         i=i+1
         if (i <= len(no_pairs)-1):
             op1 = no_pairs[i]

             if (i+1 <= len(no_pairs)-1):
                 op2 = no_pairs[i+1]

                 if (op1[0] == op2[0]):
                     no_pairs.remove(no_pairs[i])
                     no_pairs.remove(no_pairs[i])
                     i = i-2
            
    
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    for i in deck:
        print(i, end=" ")
    
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     
     l=str(len(n))
     a=int(input("\nI have "+l+" cards. If 1 stands for my first card and "+l+" for my last card,\nwhich of my cards would you like!\nGive me an integer between 1 and "+l+" : "))
     while (a<1 or a>len(n)):
         a=int(input("Invalid number. Please enter integer between 1 and "+l+" : "))

     
     return a


     

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print (' ')
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     
     while (len(human)>0 and len(dealer)>0):
         print ('Your Turn....')
         print (' ')
         print('your current deck of cards is:')
         print_deck(human)
         print (' ')
         choice=get_valid_input (dealer)
         if (choice==1):
             print('\nYou asked for my',choice,'st card')
         if (choice==2):
             print('\nYou asked for my',choice,'nd card')
         if (choice==3):
             print('\nYou asked for my',choice,'rd card')
         if (choice>=4):
             print('\nYou asked for my',choice,'th card')
        
         HP=dealer[choice-1]
         print ('\nthe card you picked is',HP)
         human.append (HP)
         dealer.remove (HP)
         print ('\nWith',HP,'added, Your current deck is:')
         print_deck (human)
         print ('\nAnd after removing pairs and shuffling, your deck is:')
         human=remove_pairs(human)
         shuffle_deck(human)
         print_deck (human)
         print (' ')
         wait_for_player()
         if len(human)==0:
             print('Ups. You do not have any more cards\nCongratulations! You, Human, have won !!!!')
         else:
             print ('***********************************')
             print ('***********************************')
             print ('\nNow it is my turn....')
             print (' ')
             dealerpick=random.randint (1,len(human))
             if (dealerpick==1):
                 print ('I took your',dealerpick,'st card\n')
             if (dealerpick==2):
                 print('I took your',dealerpick,'nd card\n')
             if (dealerpick==3):
                 print('I took your',dealerpick,'rd card\n')
             if (dealerpick>=4):
                 print('I took your',dealerpick,'th card\n')
             print ('\n***********************************')
             print ('***********************************')    
             dealer.append (human[dealerpick-1])
             human.remove (human[dealerpick-1])
             dealer=remove_pairs(dealer)
             
         if (len(dealer)==0):
             
             print('Ups. I do not have any more cards\nYou lost! I, Robot, Have won !!!!')
     	 
# main
play_game()
