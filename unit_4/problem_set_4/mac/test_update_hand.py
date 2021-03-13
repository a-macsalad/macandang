from ps4a import updateHand

HAND_SIZE = 7


def test_always_passes():
    assert True


def test_for_quail():
    word = "quail"
    hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
    assert updateHand(hand, word) == {
        'a': 0, 'q': 0, 'l': 1, 'm': 1, 'u': 0, 'i': 0}


def test_for_hello():
    word = "hello"
    hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    expected = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    assert updateHand(hand, word) == expected
