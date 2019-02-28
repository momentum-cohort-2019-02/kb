from greeting import greeting


def test_greeting():
    assert greeting("Avery") == "Hello, Avery!"


test_greeting()
