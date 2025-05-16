import random

# Class to represent a single card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit        # Suit of the card (hearts, spades, etc.)
        self.rank = rank        # Rank of the card (2, 3, J, etc.)

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"  # String representation of the card


# Class to represent a deck of cards
class Deck:

    def __init__(self):
        self.cards_in_deck = []   # List to hold the cards in the deck
        suits = ["spades", "clubs", "hearts", "diamonds"]  # List of card suits
        ranks = [   # List of card ranks and their values
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        # Create all 52 cards in the deck by combining suits and ranks
        for suit in suits:
            for rank in ranks:
                self.cards_in_deck.append(Card(suit, rank))

    def shuffle_deck(self):
        if len(self.cards_in_deck) > 1:
            random.shuffle(self.cards_in_deck)  # Shuffle the deck

    def deal_cards(self, number):
        dealt_cards = []  # List to hold the dealt cards
        for _ in range(number):
            if len(self.cards_in_deck) > 0:
                card = self.cards_in_deck.pop()  # Pop a card from the deck
                dealt_cards.append(card)
        return dealt_cards  # Return the dealt cards


# Class to represent a player's or dealer's hand
class Hand:

    def __init__(self, is_dealer=False):
        self.cards_in_hand = []  # List to hold the cards in the hand
        self.is_dealer = is_dealer  # Boolean to check if it's a dealer's hand
        self.hand_value = 0  # Value of the hand

    def add_cards(self, cards_to_add):
        self.cards_in_hand.extend(cards_to_add)  # Add new cards to the hand

    def calculate_hand_value(self):
        self.hand_value = 0
        has_ace = False  # Flag to check if there's an Ace in the hand

        # Loop through each card in the hand to calculate the total value
        for card in self.cards_in_hand:
            card_value = int(card.rank["value"])
            self.hand_value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        # Adjust for Ace value if hand exceeds 21
        if has_ace and self.hand_value > 21:
            self.hand_value -= 10

    def get_hand_value(self):
        self.calculate_hand_value()  # Recalculate hand value
        return self.hand_value

    def is_blackjack(self):
        return self.get_hand_value() == 21  # Check if the hand has Blackjack

    def display_hand(self, show_dealer_cards=False):
        # Display the player's or dealer's hand
        print(f'''{"Dealer's" if self.is_dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards_in_hand):
            # If it's the dealer's hand and the card should be hidden
            if index == 0 and self.is_dealer and not show_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)

        if not self.is_dealer:
            print("Value:", self.get_hand_value())  # Display the value for the player's hand
        print()


# Main game class
class Game:

    def play(self):
        current_game = 0  # Counter for current game number
        total_games = 0   # Total number of games to play

        # Get valid input for number of games to play
        while total_games <= 0:
            try:
                total_games = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number.")

        # Play the specified number of games
        while current_game < total_games:
            current_game += 1

            # Create and shuffle the deck
            deck = Deck()
            deck.shuffle_deck()

            # Initialize hands for player and dealer
            player_hand = Hand()
            dealer_hand = Hand(is_dealer=True)

            # Deal two cards to both the player and dealer
            for _ in range(2):
                player_hand.add_cards(deck.deal_cards(1))
                dealer_hand.add_cards(deck.deal_cards(1))

            print()
            print("*" * 30)
            print(f"Game {current_game} of {total_games}")
            print("*" * 30)
            player_hand.display_hand()  # Display player's hand
            dealer_hand.display_hand()  # Display dealer's hand

            # Check if there is an immediate winner (e.g., Blackjack or bust)
            if self.check_winner(player_hand, dealer_hand):
                continue

            action = ""
            # Player's turn to hit or stand
            while player_hand.get_hand_value() < 21 and action not in ["s", "stand"]:
                action = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while action not in ["h", "s", "hit", "stand"]:
                    action = input("Please enter 'Hit' or 'Stand' (or H/S) ").lower()
                    print()
                if action in ["hit", "h"]:
                    player_hand.add_cards(deck.deal_cards(1))  # Player chooses to hit
                    player_hand.display_hand()  # Display updated hand

            # Check if player busts or wins after their turn
            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_hand_value()  # Get the value of player's hand
            dealer_hand_value = dealer_hand.get_hand_value()  # Get the value of dealer's hand

            # Dealer's turn to hit until hand value is at least 17
            while dealer_hand_value < 17:
                dealer_hand.add_cards(deck.deal_cards(1))
                dealer_hand_value = dealer_hand.get_hand_value()

            dealer_hand.display_hand(show_dealer_cards=True)  # Display dealer's hand with all cards shown

            # Check if dealer busts or wins after their turn
            if self.check_winner(player_hand, dealer_hand):
                continue

            # Final results comparison
            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            # Check the final winner
            self.check_winner(player_hand, dealer_hand, True)

        print("Thanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        # Determine if there's a winner based on the hand values
        if not game_over:
            if player_hand.get_hand_value() > 21:
                print("You busted. Dealer wins! ")
                return True
            elif dealer_hand.get_hand_value() > 21:
                print("Dealer busted. You win! ")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have blackjack! Tie! ")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack. You win! ")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack. Dealer wins! ")
                return True
        else:
            # Final comparison of player and dealer hands
            if player_hand.get_hand_value() > dealer_hand.get_hand_value():
                print("\nYou win! ")
            elif player_hand.get_hand_value() == dealer_hand.get_hand_value():
                print("\nTie! ")
            else:
                print("\nDealer wins. ")
            return True
        return False


# Start the game
game = Game()
game.play()
