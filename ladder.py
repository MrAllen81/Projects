#This Program will calculate the height of a ladder 
#based on the height of a building and the angle of the ladder on the building


height = eval(input("What is the height of the building?"))
angle = eval(input("What is the angle between the ladder and the building?"))
import math
radians = math.radians(angle)
ladder = height / math.sin(radians)
              
print("the length of a ladder required to reach " + str(height) + " when leaned against a house is " + str(round(ladder,1)))
      
