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
        self.durability = 4
        self.playerClass = 'playerClass'
        self.cardType = 'cardType'
        self.rarity = 'rarity'
        self.race = 'race'
        self.expansion = 'expansion'
        self.image = 'image'
        self.goldImage = 'goldImage'
        self.hearthstoneCard = HearthstoneCard(self.name, self.description, self.manaCost, self.attack, self.health, self.durability, self.playerClass, self.cardType, self.rarity, self.race, self.expansion, self.image, self.goldImage)
    
    def test_generate_random_card_with_set_values_uses_those_values(self):
        hearthstoneCard2 = HearthstoneCard('asdf', 'fdsa', 99, 102, 1000, 1020, 'madeup', 'nonsense', 'words', 'here', 'for', 'testing', 'properties')
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
        self.assertEqual(self.cardGenerator.generate_random_card(expansion=self.expansion).expansion, self.expansion)
        self.assertEqual(self.cardGenerator.generate_random_card(image=self.image).image, self.image)
        self.assertEqual(self.cardGenerator.generate_random_card(goldImage=self.goldImage).goldImage, self.goldImage)

    def test_generate_random_card_properly_handles_card_type_spell(self):
        database = MockCardDatabase([self.hearthstoneCard])
        self.cardGenerator = CardGenerator(database)
        spell = self.cardGenerator.generate_random_card(cardType='Spell')
        self.assertEqual(spell.attack, 0)
        self.assertEqual(spell.health, 0)
        self.assertEqual(spell.durability, 0)

    def test_generate_random_card_properly_handles_card_type_weapon(self):
        database = MockCardDatabase([self.hearthstoneCard])
        self.cardGenerator = CardGenerator(database)
        weapon = self.cardGenerator.generate_random_card(cardType='Weapon')
        self.assertEqual(weapon.health, 0)
    
    def test_generate_random_card_properly_handles_card_type_minion(self):
        database = MockCardDatabase([self.hearthstoneCard])
        self.cardGenerator = CardGenerator(database)
        minion = self.cardGenerator.generate_random_card(cardType='Minion')
        self.assertEqual(minion.durability, 0)

    def test_get_card_information_gets_proper_card_info(self):
        database = MockCardDatabase([self.hearthstoneCard])
        self.cardGenerator = CardGenerator(database)
        self.assertEqual(self.cardGenerator.get_card_information(self.name), self.hearthstoneCard)


class MockCardDatabase:
    def __init__(self, cards):
        self.__cards = cards
    def get_cards(self):
        return self.__cards