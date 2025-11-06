#This program will calculate the distance between 2 points the user inputs
#using the distance formula
#9/19/23
#Tyler Allen

def main():
    x1 = eval(input("Enter an x coordinate for first point"))
    y1 = eval(input("Enter a y coordinate for first point"))
    x2 = eval(input("Enter an x coordinate for second point"))
    y2 = eval(input("Enter a y coordinate for second point"))

    leg1 = (x2 - x1)**2
    leg2 = (y2 - y1)**2

    import math
    distance = (math.sqrt(leg1 + leg2))
    print(" the distance to the nearest tenth " + str(round(distance,1)))
    print(" the distance is " + str(round(distance)))
    print( " the distance to the next highest integer is " + str(math.ceil(distance)))
           
main()

input("Press <Enter> to quit")
