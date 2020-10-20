from Deck import Deck
import random
class AceyDeucey :
    deckCards = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC',
                 'KC', 'AC', '2D', '3D','4D', '5D', '6D', '7D', '8D', '9D', '10D',
                 'JD', 'QD', 'KD','AD', '2H', '3H', '4H', '5H', '6H', '7H', '8H',
                 '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2S', '3S', '4S', '5S', '6S',
                 '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
    execute = 1;
    if(execute == 1):
        amount = int(input("Enter the initial amount:"))

    def assign_value(deal):
        list2 = ['2C','2H','2S','2D']
        list3 = ['3C','3H','3S','3D']
        list4 = ['4C','4H','4S','4D']
        list5 = ['5C','5H','5S','5D']
        list6 = ['6C','6H','6S','6D']
        list7 = ['7C','7H','7S','7D']
        list8 = ['8C','8H','8S','8D']
        list9 = ['9C','9H','9S','9D']
        list10 = ['10C','10H','10S','10D']
        listJ = ['JC','JH','JS','JD']
        listQ = ['QC','QH','QS','QD']
        listK = ['KC','KH','KS','KD']
        listA = ['AC','AH','AS','AD']
        if (deal in list2):
            return 2
        elif (deal in list3):
            return 3
        elif (deal in list4):
            return 4
        elif (deal in list5):
            return 5
        elif (deal in list6):
            return 6
        elif (deal in list7):
            return 7
        elif (deal in list8):
            return 8
        elif (deal in list9):
            return 9
        elif (deal in list10):
            return 10
        elif (deal in listJ):
            return 10
        elif (deal in listQ):
            return 10
        elif (deal in listK):
            return 10
        elif (deal in listA):
            return 11
    playcards = Deck(deckCards)
    playcards.shuffling()
    while(execute == 1):
        deal1 = playcards.deal()
        deal2 = playcards.deal()
        print("Here are your first two cards:")
        deal1Value = assign_value(deal1)
        deal2Value = assign_value(deal2)
        print(assign_value(deal1))
        print(assign_value(deal2))
        betAmount = int(input("Enter the bet amount:"))
        if(betAmount>amount):
            print("Bet amount should be less than the deposit")
            break
        elif(betAmount>0 and betAmount<amount):
            if (deal1Value == deal2Value):
                print("Its a tie, You loss")
                execute = 1
            elif(deal1Value>0 and deal2Value>0):
                deal3 = playcards.deal()
                dealerCard = assign_value(deal3)
                print("The third card is ",dealerCard)
                if dealerCard > deal1Value and dealerCard < deal2Value:
                    betAmount = betAmount*2
                    amount += betAmount
                    print("Congrats you won")
                    print("Amount",amount)
                elif dealerCard < deal1Value and dealerCard > deal2Value:
                    print("You won")
                    amount+= betAmount
                    print("Total amount",amount)
                else:
                    amount-= betAmount
                    print("You Lost!!! Total Funds --> $",amount)
                execute = int(input("Do you wish to continue playing? (1 for yes and 0 for no): "))
            else :
                execute = int(input("Do you wish to continue playing? (1 for yes and 0 for no): "))
        else:
            execute = int(input("Do you wish to continue playing? (1 for yes and 0 for no): "))

        
