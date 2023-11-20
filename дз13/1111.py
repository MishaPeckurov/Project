def valueList(List,index):
    try:
        print(List[index])
    
    except IndexError:
        print('-')

valueList([1,2,3],2)