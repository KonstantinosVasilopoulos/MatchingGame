class Card:

    def __init__(self, symbol, row, value, hidden):
        self.symbol = symbol
        self.row = row
        self.value = value
        self.hidden = hidden

    def __str__(self):
        return str(self.symbol) + self.row
