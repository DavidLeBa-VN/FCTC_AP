def isWordGuessed(secretWord, lettersGuessed):
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True