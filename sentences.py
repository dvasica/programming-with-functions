import random
def main():
    print(f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, -1)} {get_prepositional_phrase(2)}")
    print(f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, 0)} {get_prepositional_phrase(1)}")
    print(f"{get_determiner(1).capitalize()} {get_adjective()} {get_noun(1)} {get_verb(1, 1)} {get_prepositional_phrase(1)}")
    print(f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, -1)} {get_prepositional_phrase(1)}")
    print(f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, 0)} {get_prepositional_phrase(1)}")
    print(f"{get_determiner(2).capitalize()} {get_adjective()} {get_noun(2)} {get_verb(2, 1)} {get_prepositional_phrase(2)}")

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_preposition():
    prepositions = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_adjective():
    adjectives = ["charming", "cruel", "fantastic", "gentle", "huge", "perfect", "rough", "beautiful", "smart"]
    adjective = random.choice(adjectives)
    return adjective

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    
def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

def get_verb(quantity, tense):
    # I will use -1 instead of past
    if tense == -1:
        verbs = [ "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    # I will use 0 instead of present
    elif tense == 0 and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 0 and quantity != 1:
        verbs = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write" ]
    # I will use 1 instead of future
    elif tense == 1:
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
main()