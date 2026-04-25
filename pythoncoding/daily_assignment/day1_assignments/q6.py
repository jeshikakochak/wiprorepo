#grade system in match case
grade= input("enter grade: ")

match grade:
    case 'A' | 'a':
        print("excellent")
    case 'B' | 'b':
        print("good")
    case 'C' | 'c':
        print("average")
    case 'D' | 'd':
        print("poor")
    case 'E' | 'e':
        print("fail")
    case _:
        print("invalid grade")