from card import Card


def get_player_count():
    while True:
        try:
            player_count = int(input('Give the number of players: ').strip())
            if player_count == 0:
                continue

        except ValueError:
            print('Wrong data!')
            continue
        break

    return player_count


def get_difficulty_level():
    while True:
        difficulty_level = input('Give the difficulty level Easy (1), Medium (2), Hard (3): ').strip()

        # Check data
        if difficulty_level not in ['1', '2', '3']:
            print('Wrong data!')
            continue
        break

    return difficulty_level


def create_cards_list(difficulty_level='1'):
    """
    Create a list containing all cards

    Unicode characters
    Red heart: U+2665
    Black spades: U+2660
    Red diamond: U+2666
    Black club: U+2663

    >>> create_cards_list('2')[0].value == 2
    True
    >>> create_cards_list()[5].symbol == 'Q'
    True
    >>> create_cards_list('3')[-1].symbol
    '10'
    >>> create_cards_list()[0].value
    10
    """
    cards = []

    if difficulty_level != '1':
        # Number cards
        for n in range(2, 10):
            cards.append(Card(str(n), '\u2665', n, False))
            cards.append(Card(str(n), '\u2660', n, False))
            cards.append(Card(str(n), '\u2666', n, False))
            cards.append(Card(str(n), '\u2663', n, False))

        # Ace cards
        cards.append(Card('A', '\u2665', 1, False))
        cards.append(Card('A', '\u2660', 1, False))
        cards.append(Card('A', '\u2666', 1, False))
        cards.append(Card('A', '\u2663', 1, False))

    if difficulty_level != '2':
        # Symbol cards
        for n in ['J', 'Q', 'K']:
            cards.append(Card(n, '\u2665', 10, False))
            cards.append(Card(n, '\u2660', 10, False))
            cards.append(Card(n, '\u2666', 10, False))
            cards.append(Card(n, '\u2663', 10, False))

    # Number 10 cards
    cards.append(Card('10', '\u2665', 10, False))
    cards.append(Card('10', '\u2660', 10, False))
    cards.append(Card('10', '\u2666', 10, False))
    cards.append(Card('10', '\u2663', 10, False))

    return cards


def show_board(m, n, cards):
    """ Print a board m x n dimensions """
    cards_iter = iter(cards)  # Get an iterator from the cards list
    line = '\t'

    # Print first header line
    for j in range(1, n + 1):
        line += str(j) + '\t'
    print(line + '\n')

    # Print every other line
    for i in range(1, m + 1):
        line = str(i) + '\t'
        for j in range(1, n + 1):
            card = next(cards_iter)

            # Check if the card is hidden
            if card.hidden:
                line += 'X\t'
            else:
                line += str(card) + '\t'

        print(line + '\n')

    print('\n\n')


def check_game_over(cards):
    """
    Check if the game is over by checking if all cards are hidden or not

    >>> check_game_over(create_cards_list())
    True
    >>> cards = create_cards_list()
    >>> cards[0].hidden = True
    >>> check_game_over(cards)
    False
    """
    for card in cards:
        if card.hidden:
            return False

    return True


def get_dimensions(m, n, input_message):
    while True:
        try:
            i, j = [int(x) for x in input(input_message).strip().split(' ')]
            if i not in range(1, m + 1) or j not in range(1, n + 1):
                print('Wrong data!')
                continue
        except:
            print('Wrong data!')
            continue
        break

    return i, j


def get_card(n, i, j, cards):
    """
    Get a card given its dimensions

    >>> str(get_card(4, 1, 2, create_cards_list()))
    'J♠'
    >>> str(get_card(10, 1, 9, create_cards_list('2')))
    '4♥'
    """
    return cards[i * n - (n + 1 - j)]


def guess_card(m, n, cards, prompt):
    """ Checks if a card guess is valid and return the valid card """
    while True:
        i, j = get_dimensions(m, n, prompt)
        card = get_card(n, i, j, cards)
        if not card.hidden:
            print('The card is already open, try again')
        else:
            break

    card.hidden = False
    return card


def compare_cards(card1, card2):
    """ Compare the two given cards and return success if successful """
    success = False
    if card1.symbol == card2.symbol:
        success = True  # Success

    return success


def increase_score(card, player, player_scores):
    """ Increase the given player's score """
    player_scores[player] += card.value
    print('Match +' + str(card.value) + ' points! Player ' + str(player) + ' has ' + str(player_scores[player]) + ' points totaly.')


def choose_next_player(card1, card2, player, player_count):
    """ Check for J & J, K & K combinations and return the new player """
    if card1.symbol == card2.symbol:
        if card1.symbol == 'J':
            return player
        elif card1.symbol == 'K':
            if player_count == 2:
                return player  # Same player plays again
            return player + 2
        else:
            return player + 1

    return player + 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
