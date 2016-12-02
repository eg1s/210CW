def NO_VOVELS(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if string:
        if string[0] in vowels:
            return ''+NO_VOVELS(string[1:])    
        else:
            return string[0]+NO_VOVELS(string[1:])
    else:
        return ''


string = input('Enter a word:\n')

print(NO_VOVELS(string))
