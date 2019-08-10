import unittest
from .card_generator import CardGenerator
from .hearthstone_card import HearthstoneCard

class CardGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.name = 'name'
        self.description = 'This is a description.'
        self.manaCost = 1
        self.attack = 2
        self.health = 3
        self.playerClass = 'playerClass'
        self.cardType = 'cardType'
        self.rarity = 'rarity'
        self.race = 'race'
        self.hearthstoneCard = HearthstoneCard(self.name, self.description, self.manaCost, self.attack, self.health, self.playerClass, self.cardType, self.rarity, self.race)
    
    def test_generate_random_card_with_set_values_uses_those_values(self):
        hearthstoneCard2 = HearthstoneCard('asdf', 'fdsa', 99, 102, 1000, 'madeup', 'nonsense', 'words', 'here')
        database = MockCardDatabase([self.hearthstoneCard, hearthstoneCard2])
        self.cardGenerator = CardGenerator(database)
        self.assertEqual(self.cardGenerator.generate_random_card(name=self.name).name, self.name)
        self.assertEqual(self.cardGenerator.generate_random_card(description=self.description).description, self.description)
        self.assertEqual(self.cardGenerator.generate_random_card(manaCost=self.manaCost).manaCost, self.manaCost)
        self.assertEqual(self.cardGenerator.generate_random_card(attack=self.attack).attack, self.attack)
        self.assertEqual(self.cardGenerator.generate_random_card(health=self.health).health, self.health)
        self.assertEqual(self.cardGenerator.generate_random_card(playerClass=self.playerClass).playerClass, self.playerClass)
        self.assertEqual(self.cardGenerator.generate_random_card(cardType=self.cardType).cardType, self.cardType)
        self.assertEqual(self.cardGenerator.generate_random_card(rarity=self.rarity).rarity, self.rarity)
        self.assertEqual(self.cardGenerator.generate_random_card(race=self.race).race, self.race)

    def test_get_card_information_gets_proper_card_info(self):
        database = MockCardDatabase([self.hearthstoneCard])
        self.cardGenerator = CardGenerator(database)
        self.assertEqual(self.cardGenerator.get_card_information(self.name), self.hearthstoneCard)

class MockCardDatabase:
    def __init__(self, cards):
        self.__cards = cards
    def get_card_information(self):
        return self.__cards