def main():
    print('+=============================================+')
    print('| 1.Circle                                    |')
    print('| 2.Rectangle                                 |')
    print('| 3.Square                                    |')
    print('+=============================================+')
    option = int(input('Option(1,2,3) => '))
    if(option == 1):
        #print(circle(), 'units')
        # rep()
        subCircleMenu()
    elif(option == 2):
        #print(rectangle(), 'units')
        # rep()
        subRectangleMenu()
    elif(option == 3):
        #print(square(), 'units')
        # rep()
        subSquareMenu()
    else:
        print('Select the correct option')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////


def subCircleMenu():
    print('+=============================================+')
    print('| 1.Area                                      |')
    print('| 2.Circumforence                             |')
    print('| 3.Surface Area                              |')
    print('+=============================================+')
    option = int(input('Option(1,2,3) => '))
    if(option == 1):
        print(circleArea(), 'units')
        repcir()

    elif(option == 2):
        print(circleCircumference(), 'units')
        repcir()
    elif(option == 3):
        print(circleSurfaceArea(), 'units')
        repcir()

    else:
        print('Select the correct option')


def subRectangleMenu():
    print('+=============================================+')
    print('| 1.Area                                      |')
    print('| 2.Perimiter                                 |')
    print('| 3.Surface Area                              |')
    print('+=============================================+')


def subSquareMenu():
    print('+=============================================+')
    print('| 1.Area                                      |')
    print('| 2.Circumforence                             |')
    print('| 3.Surface Area                              |')
    print('+=============================================+')

# /////////////////////////////////////////////   CIRCLE     ////////////////////////////////////////////////////


def circleArea():
    radius = int(input('Enter radius :- '))
    area = 3.14*radius*radius
    return area


def circleCircumference():
    radius = int(input('Enter radius :- '))
    area = 3.14*2*radius
    return area


def circleSurfaceArea():
    radius = int(input('Enter radius :- '))
    area = 3.14*4*radius*radius
    return area
# ////////////////////////////////////////////  SQUARE  /////////////////////////////////////////////////////////


def square():
    side = int(input('Enter side :- '))
    area = 3.14*side*side
    return area

# ////////////////////////////////////////////  RECTANGLE  /////////////////////////////////////////////////////////


def rectangle():
    Longside = int(input('Enter long side :- '))
    Shortside = int(input('Enter short side :- '))
    area = Longside*Shortside
    return area

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def repcir():
    i = input('What you want to do ? (m=Main menu,s=Sub menu,q=Quit):- ')
    if i in ('S', 's'):
        subCircleMenu()
    elif i in ('M', 'm'):
        main()
    else:
        print('Good by....')


def repsqr():
    i = input('What you want to do ? (m=Main menu,s=Sub menu,q=Quit):- ')
    if i in ('S', 's'):
        subRectangleMenu()
    elif i in ('M', 'm'):
        main()
    else:
        print('Good by....')


def reprec():
    i = input('What you want to do ? (m=Main menu,s=Sub menu,q=Quit):- ')
    if i in ('S', 's'):
        subSquareMenu()
    elif i in ('M', 'm'):
        main()
    else:
        print('Good by....')


main()
