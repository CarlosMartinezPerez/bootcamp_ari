import requests

def deck_default(deck_count):
    deck = requests.get(f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}').json()
    return deck

qty_baralhos = 2  # Número de baralhos a embaralhar
print(deck_default(qty_baralhos))
