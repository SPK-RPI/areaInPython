def main():
    print('+=============================================+')
    print('| 1.Circle                                    |')
    print('| 2.Rectangle                                 |')
    print('| 3.Square                                    |')
    print('+=============================================+')
    option = int(input('Option(1,2,3) => '))
    if(option == 1):
        print(circle(), 'units')
        rep()
    elif(option == 2):
        print(rectangle(), 'units')
        rep()
    elif(option == 3):
        print(square(), 'units')
        rep()
    else:
        print('Select the correct option')


def circle():
    radius = int(input('Enter radius :- '))
    area = 3.14*radius*radius
    return area


def square():
    side = int(input('Enter side :- '))
    area = 3.14*side*side
    return area


def rectangle():
    Longside = int(input('Enter long side :- '))
    Shortside = int(input('Enter short side :- '))
    area = Longside*Shortside
    return area


def rep():
    i = input('Do you want to try another shape? (y,n):- ')
    if i in ('y', 'Y'):
        main()
    else:
        print('Good by....')


main()
