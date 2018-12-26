import math
import turtle
global pi
global radius
global slantLength
pi=math.pi
radius=float(0)
def coneArea(radius):
    slantOrheight=input("Do you have the Height or the Slant Height? height or slantLength")
    if slantOrheight=='slantLength':
        slantLength=float(input("slantLength"))
        slantArea=(pi*radius*radius)+(pi*radius*slantLength)
        print(slantArea)
    elif slantOrheight=='height':
        height=float(input("Height"))
        slantLength=math.sqrt(radius**2+height**2)
        slantArea=pi*radius**2+pi*radius*slantLength
        print(slantArea)
def cuboidArea(width, side1, side2):
        pair1=side1*width*2
        pair2=side2*width*2
        pair3=side1*side2*2
        print(pair1+pair2+pair3)
def cylinderArea(radius, height):
        circles=pi*radius*radius*2
        wrap=2*pi*radius*height
        print(circles+wrap)
def sqrpyrmdArea(baseLength):
    basePer=baseLength*2
    baseArea=baseLength**2
    slantOrheight=input("Do you have the Height or the Slant Height? height or slantLength")
    if slantOrheight=='slantLength':
        slantLength=float(input("slantLength"))
        sqrpyrmdArea=baseArea+basePer*slantLength
        print(sqrpyrmdArea)
    elif slantOrheight=='height':
        height=float(input("Height"))
        b=float(input("half the base Length"))
        slantLength=math.sqrt(b**2+height**2)
        sqrpyrmdArea=baseArea+basePer*slantLength
        print(sqrpyrmdArea)
def sphereArea(radius):
        area=4*pi*radius*radius
        print(area)
def triprsmArea(width, height, side1, side2):
        caps=height*bottom/2
        face1=width*side1
        face2=width*side2
        face3=width*bottom
        print(caps+face1+face2+face3)
shape=str(input("Choose one. cone, cuboids, cylinders, square pyramid (sqrpyrmd), spheres, and triangular prism (triprsm)"))
if shape=='cone':
    coneArea(float(input("radius")))
elif shape=='cuboid':
    cuboidArea(float(input("width")), float(input("side1")), float(input("side2")))
elif shape=='cylinder':
    cylinderArea(float(input("radius")), float(input("height")))
elif shape=='sqrpyrmd':
    sqrpyrmdArea(input("baseLength"))
elif shape=='sphere':
    sphereArea(float(input("radius")))
elif shape=='triprsm':
    triprsmArea(float(input("width")), float(input("Height of triangular face")), float(input("side1")), float(input("side2")), float(input("Bottom of triangular face")))
