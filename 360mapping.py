
# 360 degree mapping
# add a equation to speed it up somehow. I wonder how I would integrate that into the program

def mapdegrees(initialdegrees, rotateval,count):
    '''
    Simulate the rotation around a circle. 
    A modified version of this with less detail that appends the currentdegrees to a list each iteration,
    is used in pythonanimations.py.
    '''
    currentdegrees=initialdegrees
    totalrotations=0
    for i in range(count):
        if i>=1:
            # this works to do it by loop
            currentdegrees+=rotateval
            # print(f'currentdegrees"{currentdegrees}rotateval={rotateval}')

            
            rotationiteration=currentdegrees//360
            currentdegrees-=(360*rotationiteration)

            # track total rotations around the circle

            if currentdegrees==initialdegrees:
                print(f'Current degrees {currentdegrees} is equal to initial {initialdegrees}')
                totalrotations+=1

            print(f'\nCurrent Degrees: {currentdegrees}\nCurrent Iteration {rotationiteration}')
            # add equation to control the changing of the rotateval
        # elif initialdegrees!=0:
        else:
            print('First Current Degrees')
            rotationiteration=currentdegrees//360

            print(f'\nCurrent Degrees: {currentdegrees}\nCurrent Iteration {rotationiteration}')
            

    print(f'Total Rotations was {totalrotations}')



mapdegrees(initialdegrees=0,rotateval=30,count=13)

def make_equation(startingx, count):
    print('Starting Equation\n')
    for i in range(startingx,(count+startingx)):
        equationoutput=((i)**2)+5*i-20
        print(equationoutput)
    return '\nEquation Done'
print(make_equation(10,3))

# use this to modify the scale val
def makeoscilatting_equation(count,scaleval):
    pass
