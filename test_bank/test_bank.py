from bank import value


def test_hello_greetings():
    assert value("hello") == 0
    assert value("Hello there") == 0
    assert value("HELLO, NEWMAN") == 0


def test_other_h_greetings():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("How are you?") == 20
    assert value("hell") == 20


def test_non_h_greetings():
    assert value("Good morning") == 100
    assert value("What's up?") == 100
    assert value("Welcome") == 100


def test_case_insensitive():
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("GOOD MORNING") == 100