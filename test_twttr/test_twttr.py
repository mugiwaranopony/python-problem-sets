from twttr import shorten


def test_lowercase_vowels():
    assert shorten("aeiou") == ""
    assert shorten("twitter") == "twttr"


def test_uppercase_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("Twitter") == "Twttr"


def test_consonants():
    assert shorten("rhythm") == "rhythm"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_spaces_and_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"