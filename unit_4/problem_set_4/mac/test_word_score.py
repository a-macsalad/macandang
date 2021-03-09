from ps4a import getWordScore

HAND_SIZE = 7

# def test_always_passes():
#     assert True

def test_three_letter_word():
    word = "app"
    assert getWordScore(word, HAND_SIZE) == 21

def test_two_letter():
    word = "it"
    assert getWordScore(word, HAND_SIZE) == 4

def test_seven_letter_word():
    word = "waybill"
    assert getWordScore(word, HAND_SIZE) == 155

def test_complex_word():
    word = "outgnaw"
    assert getWordScore(word, HAND_SIZE) == 127

def test_weird_four_letter_word():
    word = "fork"
    hand = 4
    assert getWordScore(word, hand) == 94