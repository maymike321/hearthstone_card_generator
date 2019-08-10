class HearthstoneCard:
    def __init__(self, name, description, manaCost, attack, health, playerClass, cardType, rarity, race):
        self.name = name
        self.description = description
        self.manaCost = manaCost
        self.attack = attack
        self.health = health
        self.playerClass = playerClass
        self.cardType = cardType
        self.rarity = rarity
        self.race = race
    def __eq__(self, other):
        if isinstance(other, HearthstoneCard):
            return\
                self.name == other.name and\
                self.description == other.description and\
                self.manaCost == other.manaCost and\
                self.attack == other.attack and\
                self.health == other.health and\
                self.playerClass == other.playerClass and\
                self.cardType == other.cardType and\
                self.rarity == other.rarity and\
                self.race == other.race