# Hearthstone Card Generator
Generates completely random hearthstone cards (random mana cost, attack, health, name, and a description generated using markov chains from existing descriptions)

# Usage
```python
from hearthstone_card_generator import CardGenerator, CardInformationDatabase
cardGenerator = CardGenerator(CardInformationDatabase())

completelyRandomCard = cardGenerator.generate_random_card()
fixedNameRandomCard = cardGenerator.generate_random_card(name='Fixed name') #Name of the card will be 'Fixed name', other fields are randomized.

utherHeroCard = cardGenerator.get_card_information('uther of the ebon blade') #Gets the HearthstoneCard 'Uther of the Ebon Blade'
```

# Classes

## HearthstoneCard
Represents information about a particular card.

Has the following fields:  ```name, description, manaCost, attack, health, durability, playerClass, cardType, rarity, race, expansion, image, goldImage```

## CardInformationDatabase
Has one method, ```get_card_information```, which pulls all collectible cards from https://rapidapi.com/omgvamp/api/hearthstone when first called, then stores that information for repeated calls.

## CardGenerator
The main class, used to generate either random hearthstone cards or pull information from existing ones.

Constructor requires a card database in its constructor, which must have a method ```get_cards``` which returns a list of hearthstone cards.

Optionally takes in a descriptionClarity (number between 1 and 5 that rates how clear random descriptions should be, default value 2) and a phraseLength (how many sentences long random descriptions should be, default value 2).

Has two methods:

```generate_random_card``` generates a random card.  Each of ```name, description, manaCost, attack, health, durability, playerClass, cardType, rarity, race, expansion, image, goldImage``` can be passed in as optional parameters to fix that value for the random card.

```get_card_information``` takes in a card name and returns card information for that card.
