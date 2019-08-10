import json
import urllib.request
from .hearthstone_card import HearthstoneCard

class CardInformationDatabase:
    def __init__(self):
        self.__card_information = []

    def get_card_information(self):
        if self.__card_information == []:
            headers = {"X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com", "X-RapidAPI-Key": "Lfe8TETbojmshf0pd9N1Gvqd3G1vp1tjf9DjsnWoteo40kBZEq"}
            request = urllib.request.Request("https://omgvamp-hearthstone-v1.p.rapidapi.com/cards?collectible=1", headers=headers)
            with urllib.request.urlopen(request) as response:
                content = response.read()
            jsonContent = json.loads(content)
            unflattenedCards = map(lambda key: jsonContent[key], filter(lambda key: len(jsonContent[key]) > 0, jsonContent))
            cards = list(x for y in unflattenedCards for x in y)
            for card in cards:
                if lookup(card, 'text') != '':
                    card['text'] = cleanDescription(card['text'])
            self.__card_information = list(map(lambda card: HearthstoneCard(
                lookup(card, 'name'),
                cleanDescription(card['text']) if lookup(card, 'text') != '' else '',
                lookup(card, 'cost'),
                lookup(card, 'attack'),
                lookup(card, 'health'),
                lookup(card, 'playerClass'),
                lookup(card, 'type'),
                lookup(card, 'rarity'),
                lookup(card, 'race')), cards))
        return self.__card_information

def cleanDescription(description):
    return description\
        .replace("\"", "")\
        .replace("$", "")\
        .replace("#", "")\
        .replace("[x]", "")\
        .replace("<b>", "")\
        .replace("</b>", "")\
        .replace("<i>", "")\
        .replace("</i>", "")\
        .replace("{0}", "")\
        .replace("{1}", "")\
        .replace("@", "")\
        .replace("\\u00a0", " ")\
        .replace("\\u2019", "'")\
        .replace("\\n", " ")

def lookup(dictionary, field):
    return dictionary[field] if field in dictionary else ''