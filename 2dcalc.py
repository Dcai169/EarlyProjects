import math
import turtle
t=turtle.Turtle()
def triArea(base, height):
    area=base*height/2
    print(area)
def triPer(base, side1, side2):
    per=base+side1+side2
    print(per)
def paraArea(base, height):
    area=base*height
    print(area)
def paraPer(base, height):
    per=(base+height)*2
    print(per)
def trapArea(base1, base2, height):
    area=(base1+base2)/2*height
    print(area)
def trapPer(base1, base2, side1, side2):
    per=base1+base2+side1+side2
    print(per)
def pentArea(apothem, side): #note to self make side a float!
    area=(apothem*(side/2)/2)*10
    print(area)
def pentPer(side):
    per=side*5
    print(per)
def hexArea(apothem, side):
    area=6*((apothem*side)/2)
    print(area)
def hexPer(side):
    per=side*6
    print(per)