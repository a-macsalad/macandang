from ps6 import *

def decrypt_story():
    story = get_story_string()

    cypher = CiphertextMessage(story)
    x = cypher.decrypt_message()

    return x

decrypt_story()
    

