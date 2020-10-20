#
# Nupoor Joshi
# Deck : Assignment 1: Unit 5
#
#
#



from random import shuffle
orderedDeck = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC',
                 'KC', 'AC', '2D', '3D','4D', '5D', '6D', '7D', '8D', '9D', '10D',
                 'JD', 'QD', 'KD','AD', '2H', '3H', '4H', '5H', '6H', '7H', '8H',
                 '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2S', '3S', '4S', '5S', '6S',
                 '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
class Deck:
    deck_cards_rev = []
    deck_set = []
    def __init__(self,orderedDeck):
        self.deck_set = orderedDeck.copy()
        print(self.deck_set)
    def deal(self):
        dealt_card = self.deck_set[0]
        self.deck_set.pop(0)
        return dealt_card
    def fan(self):
        print(self.deck_set)
    def order(self):
        self.deck_set = orderedDeck.copy()
    def shuffling(self):
        self.deck_set = orderedDeck.copy()
        print("The cards have been shuffled.")
        return shuffle(self.deck_set)
    def isOrdered(self):
        print("Deck_set",self.deck_set)
        deck_cards_rev = self.deck_set[::-1]
        print("Ordering")
        #print("Rev_set",deck_cards_rev)
        ordered_rev = orderedDeck[::-1]
        #print("Ordered Rev",ordered_rev)
        length = len(deck_cards_rev)
        i = 0
        count = 1
        while(i<length):
            if deck_cards_rev[i] == ordered_rev[i]:
                count +=1
            else :
                print("The deck is not ordered")
                return False
                break
            i+=1
            return True
print ("Welcome to the Game!")              
deck = Deck(orderedDeck)
print("___deal____")
print(deck.deal())
print("___Fan____")
print(deck.fan())
print("___Shuffling____")
print(deck.shuffling())
print(deck.isOrdered())





        
        

        
    
