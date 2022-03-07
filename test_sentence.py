from cmath import sin
from pyparsing import Word
from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import random
import pytest
def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 10)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        noun = get_noun(1)
    assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(2,10):
        noun = random.choice(plural_nouns)
    assert noun in plural_nouns

def test_get_verb():
    past_verbs = [ "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(5):
        word = get_verb(1,-1)
    assert word in past_verbs

    singular_present_verbs = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(5):
        word = get_verb(1, 0)
    assert word in singular_present_verbs

    plural_present_verbs = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(5):
        word = get_verb(2,0)
    assert word in plural_present_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(5):
        word = get_verb(1, 1)
    assert word in future_verbs

def test_get_preposition():
    prepositions = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(5):
        preposition = get_preposition()
    assert preposition in prepositions

def test_get_prepositional_phrase():
    
    prepositions = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    singular = get_prepositional_phrase(1).split(" ")
    for _ in range(5):
        single_determiner = ["a", "one", "the"]
        single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
        assert singular[0] in prepositions
        assert singular[1] in single_determiner
        assert singular[2] in single_noun
    
    plural = get_prepositional_phrase(2).split(" ")
    for _ in range(5):
        plural_determiner = ["two", "some", "many", "the"]
        plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        assert plural[0] in prepositions
        assert plural[1] in plural_determiner
        assert plural[2] in plural_noun




pytest.main(["-v", "--tb=line", "-rN", __file__])