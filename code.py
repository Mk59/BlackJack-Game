import random

# Class to represent a single card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


# Class to represent a deck of cards
class Deck:

    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
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

        # Create all 52 cards in the deck
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)  # Shuffle the deck

    def deal(self, number):
        return [self.cards.pop() for _ in range(number)]  # Deal cards to players


# Class to represent a player's or dealer's hand
class Hand:

    def __init__(self, dealer=False):
        self.cards = []
        self.dealer = dealer
        self.value = 0

    def add_cards(self, new_cards):
        self.cards.extend(new_cards)  # Add dealt cards to the hand

    def calculate_value(self):
        self.value = 0
        ace_count = 0

        for card in self.cards:
            self.value += card.rank["value"]
            if card.rank["rank"] == "A":
                ace_count += 1

        # Adjust for Aces: If the value is over 21 and there's an Ace, change Ace to 1
        while self.value > 21 and ace_count:
            self.value -= 10
            ace_count -= 1

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21  # Check if hand has Blackjack

    def display(self, show_dealer_cards=False):
        print(f"{'Dealer' if self.dealer else 'Your'} hand: ")
        for index, card in enumerate(self.cards):
            # If it's the dealer's first card and we aren't showing it
            if self.dealer and index == 0 and not show_dealer_cards:
                print("hidden")
            else:
                print(card)

        if not self.dealer:
            print(f"Value: {self.get_value()}")
        print()


# Main game class
class Game:

    def play(self):
        # Ask for number of games
        num_games = int(input("How many games do you want to play? "))

        for game_num in range(1, num_games + 1):
            print(f"\nStarting Game {game_num}")

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            # Deal two cards to both player and dealer
            player_hand.add_cards(deck.deal(2))
            dealer_hand.add_cards(deck.deal(2))

            # Show initial hands
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue  # Check if the player has won or lost right away

            # Player's turn: hit or stand
            while player_hand.get_value() < 21:
                choice = input("Choose 'Hit' or 'Stand': ").lower()
                if choice in ['hit', 'h']:
                    player_hand.add_cards(deck.deal(1))
                    player_hand.display()
                elif choice in ['stand', 's']:
                    break

            if self.check_winner(player_hand, dealer_hand):
                continue  # Check if the player has won or lost after their turn

            # Dealer's turn: hits until the value is 17 or more
            while dealer_hand.get_value() < 17:
                dealer_hand.add_cards(deck.deal(1))
                dealer_hand.display(show_dealer_cards=True)

            # Final result after both hands are played
            self.check_winner(player_hand, dealer_hand, game_over=True)

        print("Thanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        # Check for win/loss conditions
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted! Dealer wins!")
                return True
            if dealer_hand.get_value() > 21:
                print("Dealer busted! You win!")
                return True
            if player_hand.is_blackjack():
                print("You have Blackjack! You win!")
                return True
            if dealer_hand.is_blackjack():
                print("Dealer has Blackjack! You lose!")
                return True
        else:
            # Final comparison between player and dealer hands
            player_value = player_hand.get_value()
            dealer_value = dealer_hand.get_value()
            if player_value > dealer_value:
                print(f"You win! Your hand: {player_value}, Dealer's hand: {dealer_value}")
            elif dealer_value > player_value:
                print(f"Dealer wins! Your hand: {player_value}, Dealer's hand: {dealer_value}")
            else:
                print(f"It's a tie! Both have {player_value}")
        return False

# Start the game
game = Game()
game.play()
