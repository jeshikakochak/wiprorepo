character=input("enter a character")
match character:
    case 'i' | 'a' | 'e' | 'o' |'u'|'A'|'U'|'I'|'O'|'E':
        print("vowel")
    case _:
        print("consonant")
