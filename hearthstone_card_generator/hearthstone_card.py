class HearthstoneCard:
    def __init__(self, name, description, manaCost, attack, health, durability, playerClass, cardType, rarity, race, image, goldImage):
        self.name = name
        self.description = description
        self.manaCost = manaCost
        self.attack = attack
        self.health = health
        self.durability = durability
        self.playerClass = playerClass
        self.cardType = cardType
        self.rarity = rarity
        self.race = race
        self.image = image
        self.goldImage = goldImage
    def __eq__(self, other):
        if isinstance(other, HearthstoneCard):
            return\
                self.name == other.name and\
                self.description == other.description and\
                self.manaCost == other.manaCost and\
                self.attack == other.attack and\
                self.health == other.health and\
                self.durability == other.durability and\
                self.playerClass == other.playerClass and\
                self.cardType == other.cardType and\
                self.rarity == other.rarity and\
                self.race == other.race and\
                self.image == other.image and\
                self.goldImage == other.goldImage