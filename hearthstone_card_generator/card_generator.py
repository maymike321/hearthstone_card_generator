from .hearthstone_card import HearthstoneCard
from pyykov import Pyykov
import random

class CardGenerator:
    def __init__(self, cardInformationDatabase, descriptionClarity = 2, phraseLength = 2):
        self.__descriptionClarity = min(max(1, descriptionClarity), 5)
        self.__phraseLength = max(1, phraseLength)
        self.__cardInformationDatabase = cardInformationDatabase
        self.__load_card_information()

    def __load_card_information(self):
        self.__cards = self.__cardInformationDatabase.get_cards()
        self.__load_names()
        self.__load_descriptions()
        self.__load_player_classes()
        self.__load_card_types()
        self.__load_rarities()
        self.__load_races()
        self.__load_expansions()
        self.__load_images()
        self.__load_gold_images()

    def __load_names(self):
        self.__names = unique(map(lambda card: card.name, self.__cards))
    def __load_descriptions(self):
        self.__descriptions = list(filter(lambda description: description != '', map(lambda card: card.description, self.__cards)))
        self.__markovGenerator = Pyykov(self.__descriptionClarity)
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
    def __load_expansions(self):
        expansions = unique(map(lambda card: card.expansion, self.__cards))
        self.__expansions = expansions
        self.__expansionsWeights = list(map(lambda expansion: sum(1 for card in self.__cards if card.expansion == expansion), expansions))
    def __load_images(self):
        self.__images = unique(map(lambda card: card.image, self.__cards))
    def __load_gold_images(self):
        self.__goldImages = unique(map(lambda card: card.goldImage, self.__cards))

    def generate_random_card(self, name=None, description=None, manaCost=None, attack=None, health=None, durability=None, playerClass=None, cardType=None, rarity=None, race=None, expansion=None, image=None, goldImage=None):
        cardType = cardType or random.choices(self.__cardTypes, weights=self.__cardTypesWeights)[0]
        attack = attack or (random.choice(range(13)) if cardType != 'Spell' else 0)
        health = health or (random.choice(range(1, 13)) if cardType == 'Minion' else 0)
        durability = durability or (random.choice(range(1, 13)) if cardType == 'Weapon' else 0)
        race = race or (random.choices(self.__races, weights=self.__racesWeights)[0] if cardType == 'Minion' else '')
        return HearthstoneCard(
            name = name or random.choice(self.__names),
            description = description or self.__generate_description(),
            manaCost = manaCost or random.choice(range(11)),
            attack = attack,
            health = health,
            durability = durability,
            playerClass = playerClass or random.choices(self.__playerClasses, weights=self.__playerClassWeights)[0],
            cardType = cardType,
            rarity = rarity or random.choices(self.__rarities, weights=self.__raritiesWeights)[0],
            race = race,
            expansion = expansion or random.choices(self.__expansions, weights=self.__expansionsWeights)[0],
            image = image or random.choice(self.__images),
            goldImage = goldImage or random.choice(self.__goldImages))

    def __generate_description(self):
        description = ''
        for i in range(self.__phraseLength):
            description += self.__markovGenerator.generate_phrase()
            if i != self.__phraseLength - 1:
                if description[-1] != '.':
                    description += '.'
                description += '  '
        return description

    def get_card_information(self, name):
        return next((card for card in self.__cards if card.name.lower() == name.lower()), None)

def unique(collection):
    return list(set(collection))