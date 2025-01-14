def solution(myString):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    l_index = alphabet.index('l')
    result = ''
    for char in myString:
        if alphabet.index(char) < l_index:
            result += 'l' 
        else:
            result += char
    return result
