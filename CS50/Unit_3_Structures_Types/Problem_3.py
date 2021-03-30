def getAvailableLetters(lettersGuessed):
    kq = ''
    for i in range(ord('a'), ord('z') + 1):
        c = chr(i)
        if c not in lettersGuessed:
            kq += c
    return kq