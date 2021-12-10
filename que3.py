# palindromic border

def numberOfPalindromicBorders(n: str):
    palindromicSubString = []
    count = 1
    while(count > len(n)):
        check = n[count]
        pos = 1
        while(pos < len(n)):
            check = check + n[pos]
            if(checkIfPalindrome(check)):
                palindromicSubString.append(check)
            pos += 1
        count += 1
    return len(palindromicSubString)


def checkIfPalindrome(word: str):
    count = len(word)
    for i in len(0, len(word)):
        count -= 1
        check = word[i] = word[count]
        if(check == False):
            return False
    return True
