import random

def madlib_generator():
    """
    This function generates a mad lib story based on user-selected levels of formality and sophistication for nouns, verbs, adjectives, and adverbs.
    """

    # Define lists of nouns, verbs, adjectives, and adverbs with varying levels of formality and sophistication
    nouns = {
        "common": ["dog", "cat", "elephant", "giraffe", "zebra"],
        "formal": ["gentleman", "lady", "scholar", "artist", "entrepreneur"],
        "whimsical": "dragon", "unicorn", "mermaid", "wizard", "fairy"
    }

    verbs = {
        "common": ["ran", "jumped", "swam", "flew", "climbed"],
        "action": "dashed", "leapt", "dove", "soared", "scaled",
        "poetic": "scampered", "bounded", "glided", "sailed", "ascended"
    }

    adjectives = {
        "common": ["happy", "sad", "angry", "excited", "sleepy"],
        "descriptive": "jolly", "glum", "furious", "thrilled", "drowsy",
        "vibrant": "ecstatic", "dejected", "frenzied", "elated", "languid"
    }

    adverbs = {
        "common": ["quickly", "slowly", "carefully", "happily", "sadly"],
        "manner": "swiftly", "diligently", "joyfully", "mournfully",
        "elegantly": "gracefully", "nimbly", "exuberantly", "melancholically"
    }

    # Prompt the user to select levels of formality and sophistication for each word type
    noun_level = input("Enter noun level (common, formal, whimsical): ")
    verb_level = input("Enter verb level (common, action, poetic): ")
    adjective_level = input("Enter adjective level (common, descriptive, vibrant): ")
    adverb_level = input("Enter adverb level (common, manner, elegantly): ")

    # Validate user input to ensure valid levels are chosen
    if noun_level not in nouns:
        print("Invalid noun level. Please choose from 'common', 'formal', or 'whimsical'")
        return

    if verb_level not in verbs:
        print("Invalid verb level. Please choose from 'common', 'action', or 'poetic'")
        return

    if adjective_level not in adjectives:
        print("Invalid adjective level. Please choose from 'common', 'descriptive', or 'vibrant'")
        return

    if adverb_level not in adverbs:
        print("Invalid adverb level. Please choose from 'common', 'manner', or 'elegantly'")
        return

    # Randomly select a word from each list based on the chosen levels
    noun = random.choice(nouns[noun_level])
    verb = random.choice(verbs[verb_level])
    adjective = random.choice(adjectives[adjective_level])
    adverb = random.choice(adverbs[adverb_level])

    # Generate the mad lib story
    story = f"The {adjective} {noun} {adverb} {verb}."

    # Print the mad lib story
    print(story)

# Call the madlib_generator function
madlib_generator()
