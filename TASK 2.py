def likes(array):

    
    if len(array)== 0 :
        print('no one likes this item')

    elif len(array) == 1:
        print(array[0], 'likes this item')

    elif len(array) == 2:
        print(array[0], 'and', array[1], 'likes this item')

    elif len(array) == 3:
        print(array[0], ',', array[1], 'and' , array[2] , 'likes this item')

    else :
        print(array[0], ',', array[1], 'and' , len(array[2:]), 'others likes this item')
        


likes(["Soji", "Samuel", "Jane", "Kelechi", "Peter", "Buhari"])
