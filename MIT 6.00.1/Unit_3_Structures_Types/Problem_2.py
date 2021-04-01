def getGuessedWord(secretWord, lettersGuessed):
    kq = ''
    for c in secretWord:
        if c not in lettersGuessed:
            kq += '_'
        else:
            kq += c
    return kq