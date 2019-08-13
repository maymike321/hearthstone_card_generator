import json
import urllib.request
from .hearthstone_card import HearthstoneCard

class CardInformationDatabase:
    def __init__(self):
        self.__card_information = []

    def get_cards(self):
        if self.__card_information == []:
            headers = {"X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com", "X-RapidAPI-Key": "Lfe8TETbojmshf0pd9N1Gvqd3G1vp1tjf9DjsnWoteo40kBZEq"}
            request = urllib.request.Request("https://omgvamp-hearthstone-v1.p.rapidapi.com/cards?collectible=1", headers=headers)
            with urllib.request.urlopen(request) as response:
                content = response.read()
            jsonContent = json.loads(content)
            unflattenedCards = map(lambda key: jsonContent[key], filter(lambda key: len(jsonContent[key]) > 0, jsonContent))
            cards = list(x for y in unflattenedCards for x in y)
            self.__card_information = list(map(lambda card: HearthstoneCard(
                lookup(card, 'name'),
                lookup(card, 'text'),
                lookup(card, 'cost'),
                lookup(card, 'attack'),
                lookup(card, 'health'),
                lookup(card, 'durability'),
                lookup(card, 'playerClass'),
                lookup(card, 'type'),
                lookup(card, 'rarity'),
                lookup(card, 'race'),
                lookup(card, 'cardSet'),
                lookup(cards, 'img'),
                lookup(cards, 'imgGold')), cards))
        return self.__card_information

def lookup(dictionary, field):
    return dictionary[field] if field in dictionary else ''