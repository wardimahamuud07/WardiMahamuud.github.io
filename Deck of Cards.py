import random

# List of card suit symbols (white versions)
card_suits = ['♡', '♢', '♧', '♤']

# Initialize an empty list for the deck
deck = []

# Outer loop for each suit
for suit in card_suits:
    # Inner loop for each rank from 1 (Ace) to 13 (King)
    for x in range(1, 14):
        # Determine the rank representation
        if x == 1:
            rank = "A"
        elif x == 11:
            rank = "J"
        elif x == 12:
            rank = "Q"
        elif x == 13:
            rank = "K"
        else:
            rank = str(x)
        
        # Create a card as a string "rank of suit" and add it to the deck
        card = f"{rank} of {suit}"
        deck.append(card)

# Shuffle the deck
random.shuffle(deck)

# Create two new lists for player1 and player2
player1 = []
player2 = []

# Populate each new list with half of the shuffled deck
half_deck_size = len(deck) // 2
player1 = deck[:half_deck_size]
player2 = deck[half_deck_size:]

# Print the cards for each player to verify
print("Player 1's cards:")
for card in player1:
    print(card)

print("\nPlayer 2's cards:")
for card in player2:
    print(card)