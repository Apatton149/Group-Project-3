#!/usr/bin/env python3
# Global imports.
import random

# Mad Lib word types.
ADJECTIVE        = 'Adjective'
ANIMAL           = 'Animal'
ANIMAL_PLURAL    = 'Animal (plural)'
BODY_PART        = 'Body Part'
BODY_PART_PLURAL = 'Body Part (plural)'
CELEBRITY        = 'Celebrity'
COLOR            = 'Color'
FRUIT            = 'Fruit'
NAME             = 'Name'
NOUN             = 'Noun'
NOUN_PLURAL      = 'Noun (plural)'
OCCUPATION       = 'Occupation'
PLACE            = 'Place'
PLANT_PLURAL     = 'Plant (plural)'
PHRASE           = 'Phrase'
SILLY_WORD       = 'Silly word'
SUPERLATIVE      = 'Superlative (ends in "est")'
VERB             = 'Verb'
VERB_ED          = 'Verb ending in "ed"'
VERB_ING         = 'Verb ending in "ing"' 

# Mad lib paragraphs.
madLibText0  = 'Be kind to your {0}-footed {1}. For a duck may be somebody\'s {2}. Be kind to your {1} in {3} where the weather is always {4}. You may think that this is the {5}, well it is.' 
madLibTypes0 = [NOUN, NOUN_PLURAL, NOUN, PLACE, ADJECTIVE, NOUN]
madLibText1  = 'The {0} Dragon is the {1} Dragon of all. It has {2} {3}, and a {4} shaped like a {5}. It loves to eat {6}, although it will feast on nearly anything. It is {7} and {8}. You must be {9} around it, or you may end up as it`s meal!'
madLibTypes1 = [COLOR, SUPERLATIVE, ADJECTIVE, BODY_PART_PLURAL, BODY_PART, NOUN, ANIMAL_PLURAL, ADJECTIVE, ADJECTIVE, ADJECTIVE]
madLibText2  = 'Dirty martinis are a good cocktail while you are on a date. Who can {0} a dirty martini? First get a martini {1}. Add {2} or {3}. Next add some {4} and some {5}. Put it in a {6} and drink. You can also have it {7}. Now {8}. You can also go to a {9} and get one ready already made. Many celebrities like this drink including {10}!'
madLibTypes2 = [VERB, NOUN, NAME, CELEBRITY, ANIMAL_PLURAL, NAME, NOUN, VERB_ED, VERB, PLACE, CELEBRITY, PHRASE]
madLibText3  = 'J.R.R Tolkien had been thrust into the {0}-light yet again with the release of his famous trilogy Lord of the {1} as a {2} series. The three books, {3} of the Ring, The Two {4} and the Return of the {5}, are preceded by another book The {6}, which may also be filmed later on.'
madLibTypes3 = [FRUIT, NOUN_PLURAL, NOUN, NOUN, NOUN_PLURAL, NOUN, SILLY_WORD]
madLibText4  = 'I was {0} down the hallway and some {1} grabbed my {2}, and I turned to him and said "so help me, if you {3} me again you will go the way of the {4}" And then he {5} away!'
madLibTypes4 = [VERB_ING, NOUN, BODY_PART, VERB, ANIMAL, VERB_ED]
madLibText5  = '{0} {1} Brothers is a popular video game where you contol a/an {2} as he/she runs through levels {3} on enemies and eating {4} to get {5} and fireworks so that he/she can throw {6} at enemies. He does all the to save the {7} from the evil {8}.'
madLibTypes5 = [ADJECTIVE, NAME, OCCUPATION, VERB_ING, PLANT_PLURAL, ADJECTIVE, NOUN_PLURAL, NOUN, NAME]

# Program.
gameRunning = True
while gameRunning:
    # Print title and instructions for user.
    print('Play Mad Libs!')
    print('Please type a word for each category! Press enter to submit a word.')
    
    # Fetch a mad lib.
    # Zip creates a list of tuples. Tuple contains (text0, type0).
    # Random.choice chooses one of the tuples from the list at random. 
    madLib = random.choice(list(zip([madLibText0,  madLibText1,  madLibText2,  madLibText3,  madLibText4,  madLibText5],
                                    [madLibTypes0, madLibTypes1, madLibTypes2, madLibTypes3, madLibTypes4, madLibTypes5])))

    # Accept user input for every type in list.
    userWordList = list()
    for wordType in madLib[1]:
        # Recieves user input.
        userWord = input('{type}: '.format(type=wordType)).strip()

        # Storing user input.
        userWordList.append(userWord)

    # Combining user input with Mad lib paragraph.
    completedMadLib = madLib[0].format(*userWordList)

    # Showing user the completed Mad lib.
    print(completedMadLib)

    # Asking user if they want to play again.
    validChoice = False
    while not validChoice:
        userChoice = input('Would you like to play again? Type "yes" or "no": ').strip().lower()
        # If yes then loop, if not end game. Don't allow other options.
        if userChoice == 'yes':
            # Restart the game.
            validChoice = True
        elif userChoice == 'no':
            # End game.
            validChoice = True
            gameRunning = False
        else:
            # Don't allow other options.
            validChoice = False
            print('Please type "yes" or "no".')