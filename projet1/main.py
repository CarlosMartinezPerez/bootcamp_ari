import requests as rq

def deck_default(deck_count=1):
    deck = rq.get(f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}').json()
    return deck

print(deck_default(4))  # Especificando o número de baralhos entre os parênteses



