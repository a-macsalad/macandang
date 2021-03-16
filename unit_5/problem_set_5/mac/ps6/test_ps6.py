from ps6 import *

def test_always_passes():
    assert True

def test_three_letter_shift_lowercase():
    shift = 2
    message = Message('hello')
    assert (message.apply_shift(shift)) == "jgnnq"

def test_zero_letter_shift_lowercase():
    shift = 0
    message = Message('hello')
    assert (message.apply_shift(shift)) == "hello"

def test_five_letter_shift_lowercase_with_numbers():
    shift = 6
    message = Message("we are taking 6.00.1x")
    assert (message.apply_shift(shift)) == "ck gxk zgqotm 6.00.1d"

def test_five_letter_shift_lowercase_with_numbers():
    shift = 21
    message = Message("th!s is Problem Set 6?")
    assert (message.apply_shift(shift)) == "oc!n dn Kmjwgzh Nzo 6?"

def test_PlaintextMessage_changes_shift():
    plaintext = PlaintextMessage('hello', 2)
    assert plaintext.get_shift() == 2
    assert plaintext.get_message_text_encrypted() == "jgnnq"

    plaintext.change_shift(5)
    assert plaintext.get_shift() == 5
    assert plaintext.get_message_text_encrypted() == "mjqqt"