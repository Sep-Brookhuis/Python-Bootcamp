from random import shuffle
import time

suits = ("Hearts", "Daimonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", 
         "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, 
          "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

game_on = True


class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit} of {self.rank}"


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        return f"This deck contains {len(self.deck)} cards."

    def shuffle(self):
        shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop(0)


class Hand():

    def __init__(self):
        self.cards = []  
        self.value = 0  
        self.aces = 0 


    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
         while self.value > 21 and self.aces:
            self.value -= 10  
            self.aces -= 1  
             

class Chips():
    
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet():

    while True:
        try:
            bet_amount = int(input("Enter your bet amount: "))
        except:
            print("Error: Please enter a valid amount of chips")
        else:
            if bet_amount > chips.total:
                print("You don't have enough chips for that bet!")
            else:
                print(f"You have succesfully betted {bet_amount} chips")
                return bet_amount
            

def show_some(player,dealer):
    player_cards = ", ".join(str(card) for card in player.cards)
    print(f"Your hand: {player_cards} | Total hand value: {player.value}")
    print(f"Dealer hand: {dealer.cards[0]}, Hidden Card | Total hand value: {values[dealer.cards[0].rank]}")


def show_all(player,dealer):
    player_cards = ", ".join(str(card) for card in player.cards)
    print(f"Your hand: {player_cards} | Total hand value: {player.value}")
    dealer_cards = ", ".join(str(card) for card in dealer.cards)
    print(f"Dealer hand: {dealer_cards} | Total hand value: {dealer.value}")


def hit_or_stand(deck,hand):
    while True:
        answer = input("Hit or stand: ").upper()
        if answer in ["HIT", "STAND"]:
            break
        else:
            print("Error: Please enter 'hit' or 'stand'")

    if answer == "HIT":
        hand.add_card(deck.deal())
        hand.adjust_for_ace()
        return True
    elif answer == "STAND":
        return False


def play_again():
    while True:
        answer = input("Do you want to play again? (Y/N) ").upper()
        if answer in ["Y", "N"]:
            break
        else:
            print("Error: Please enter 'Y' or 'N'")
    
    if answer == "Y":
        return True
    elif answer == "N":
        return False

             
if __name__ == "__main__":

    # Print welcome message to user
    print("Welcome to Blackjack!")

    # Create an instance of chips for user
    chips = Chips()
    
    # Start off the game 
    while game_on:

        # Print amount of chips user currently has
        print(f"You currently have {chips.total} chips!")

        # Create a deck of 52 cards and shuffle it
        deck = Deck()
        deck.shuffle()

        # Ask the player for their bet
        chips.bet = take_bet()

        # Deal two cards to the player and the dealer
        player = Hand()
        dealer = Hand()

        for _ in range(2):
            player.add_card(deck.deal())
            player.adjust_for_ace()

        for _ in range(2):
            dealer.add_card(deck.deal())
            dealer.adjust_for_ace()
        
        # Show one of the dealers cards and all the players cards
        show_some(player,dealer)

        # Loop as long as the player wants to hit
        playing = True
        while playing:

            # Ask player if he wants to hit or stand
            playing = hit_or_stand(deck, player)

            # Show players hand with newly drawn card
            if playing == True:
                show_some(player,dealer)
            elif playing == False:
                show_all(player,dealer)

            # If the player busted print a message and subtract the chips from the total
            if player.value > 21:
                print("You have busted!")
                chips.lose_bet()
                game_on = play_again()
                break
        
        # Play out the dealers hand if player didn't bust
        if player.value <= 21:

            # Waiting time for dealer to play hand
            print("Dealer playing out hand...")
            time.sleep(8)
            
            while dealer.value < 17:
                dealer.add_card(deck.deal())
                dealer.adjust_for_ace()

                if dealer.value > 21:
                    show_all(player,dealer)
                    print("Dealer has busted!")
                    chips.win_bet()
                    game_on = play_again()
                    break

            # If the player and dealer both didn't bust determine the winner
            if dealer.value <= 21:
                show_all(player,dealer)
                if player.value == dealer.value:
                    print("Push! No winner this round.")
                elif player.value > dealer.value:
                    print("Player has won!")
                    chips.win_bet()
                else:
                    print("Dealer has won!")
                    chips.lose_bet()
                
                game_on = play_again()
