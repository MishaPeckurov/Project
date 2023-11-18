def check(num,string):
    match num:
        case 1:
            print(len(string))
        case 2:
            print(type(string))
        case 3:
            print(string[0])
        case _:
            print('Error')
check(1,'Misha')        