def getGuessedWord(secretWord, lettersGuessed):
    ans = ''
    for c in secretWord:
        if c not in lettersGuessed:
            ans += '_'
        else:
            ans += c
    return ans