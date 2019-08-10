from .hearthstone_card import HearthstoneCard
from pyykov import Pyykov
import random

class CardGenerator:
    def __init__(self, cardInformationDatabase):
        self.__phraseLength = 2
        self.__cardInformationDatabase = cardInformationDatabase
        self.__load_card_information()
    
    def set_description_clarity(self, descriptionClarity):
        self.__phraseLength = descriptionClarity

    def __load_card_information(self):
        self.__cards = self.__cardInformationDatabase.get_card_information()
        self.__load_names()
        self.__load_descriptions()
        self.__load_player_classes()
        self.__load_card_types()
        self.__load_rarities()
        self.__load_races()

    def __load_names(self):
        self.__names = unique(map(lambda card: card.name, self.__cards))
    def __load_descriptions(self):
        self.__descriptions = list(filter(lambda description: description != '', map(lambda card: card.description, self.__cards)))
        self.__markovGenerator = Pyykov(2)
        self.__markovGenerator.set_source(self.__descriptions)
    def __load_player_classes(self):
        playerClasses = unique(map(lambda card: card.playerClass, self.__cards))
        self.__playerClasses = playerClasses
        self.__playerClassWeights = list(map(lambda playerClass: sum(1 for card in self.__cards if card.playerClass == playerClass), playerClasses))
    def __load_card_types(self):
        cardTypes = unique(map(lambda card: card.cardType, self.__cards))
        self.__cardTypes = cardTypes
        self.__cardTypesWeights = list(map(lambda cardType: sum(1 for card in self.__cards if card.cardType == cardType), cardTypes))
    def __load_rarities(self):
        rarities = unique(map(lambda card : card.rarity, self.__cards))
        self.__rarities = rarities
        self.__raritiesWeights = list(map(lambda rarity: sum(1 for card in self.__cards if card.rarity == rarity), rarities))
    def __load_races(self):
        races = unique(map(lambda card: card.race, self.__cards))
        self.__races = races
        self.__racesWeights = list(map(lambda race: sum(1 for card in self.__cards if card.race == race), races))

    def generate_random_card(self, name=None, description=None, manaCost=None, attack=None, health=None, playerClass=None, cardType=None, rarity=None, race=None):
        return HearthstoneCard(
            name = name or random.choice(self.__names),
            description = description or self.__generate_description(self.__phraseLength),
            manaCost = manaCost or random.choice(range(11)),
            attack = attack or random.choice(range(13)),
            health = health or random.choice(range(1, 13)),
            playerClass = playerClass or random.choices(self.__playerClasses, weights=self.__playerClassWeights),
            cardType = cardType or random.choices(self.__cardTypes, weights=self.__cardTypesWeights),
            rarity = rarity or random.choices(self.__rarities, weights=self.__raritiesWeights),
            race = race or random.choices(self.__races, weights=self.__racesWeights))

    def __generate_description(self, phraseLength):
        description = ''
        for i in range(phraseLength):
            description += self.__markovGenerator.generate_phrase()
            if i != phraseLength - 1:
                if description[-1] != '.':
                    description += '.'
                description += '  '
        return description
    def get_card_information(self, name):
        return next((card for card in self.__cards if card.name.lower() == name.lower()), None)

def unique(collection):
    return list(set(collection))