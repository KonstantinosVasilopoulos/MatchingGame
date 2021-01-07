import random
import functions


# Welcome the player(s)
print('Welcome to the Matching Game')

# Get player count
player_count = functions.get_player_count()

# Get the difficulty level and set the board dimensions and cards
DIFFICULTY_LEVEL = functions.get_difficulty_level()
if DIFFICULTY_LEVEL == '1':
    m = 4
    n = 4
elif DIFFICULTY_LEVEL == '2':
    m = 4
    n = 10
else:
    m = 4
    n = 13

# Create cards and shuffle them
cards = functions.create_cards_list(DIFFICULTY_LEVEL)
random.seed()
random.shuffle(cards)

# Show board and hide all cards
functions.show_board(m, n, cards)
for card in cards:
    card.hidden = True

# Dictionary containing player scores
player_scores = {}
for player in range(1, player_count + 1):
    player_scores[player] = 0

# Main loop
while not functions.check_game_over(cards):

    player = 1
    while player <= player_count and not functions.check_game_over(cards):
        # Let each player guess 2 cards
        card1 = functions.guess_card(m, n, cards, 'Player ' + str(player) + ': Give row and column of the first card (eg 1 10): ')
        functions.show_board(m, n, cards)
        card2 = functions.guess_card(m, n, cards, 'Player ' + str(player) + ': Give row and column of the second card: ')
        functions.show_board(m, n, cards)


        # Compare the 2 cards
        if functions.compare_cards(card1, card2):
            functions.increase_score(card1, player, player_scores)

        # Check for a K & Q combination
        card3_success = False
        if (card1.symbol == 'Q' and card2.symbol == 'K') or (card1.symbol == 'K' and card2.symbol == 'Q'):
            # Let the player open a third card
            card3 = functions.guess_card(m, n, cards, 'Player ' + str(player) + ': Give row and column of the third card: ')
            functions.show_board(m, n, cards)

            # Compare the 1st with the 3rd card
            if functions.compare_cards(card1, card3):
                functions.increase_score(card3, player, player_scores)
                card2.hidden = True  # Hide the 2nd card
                card3_success = True

            # Compare the 2nd with the 3rd card
            elif functions.compare_cards(card2, card3):
                functions.increase_score(card3, player, player_scores)
                card1.hidden = True  # Hide the 1st card
                card3_success = True

            else:  # Hide all cards
                card1.hidden = True
                card2.hidden = True
                card3.hidden = True

        # Decide who the next player is
        if not card3_success:
            player = functions.choose_next_player(card1, card2, player, player_count)
        else:
            if functions.compare_cards(card1, card3):
                player = functions.choose_next_player(card1, card3, player, player_count)
            else:
                player = functions.choose_next_player(card2, card3, player, player_count)

# Show results
print('Results')
for player in player_scores:
    print('\tPlayer ' + str(player) + ': ' + str(player_scores[player]))
