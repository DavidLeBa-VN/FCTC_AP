import string
def getAvailableLetters(lettersGuessed):
    ans = string.ascii_lowercase
    i = 0
    while i < len(ans):
        if ans[i] in lettersGuessed:
            ans = ans[:i] + ans[i + 1:]
        else:
            i += 1
    return ans