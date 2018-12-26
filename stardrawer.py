import turtle
t = turtle.Turtle()
def circleDrawing(diameter,rounds,color,rate):
    t.speed(rate)
	t.color(color)
	for x in range(1,rounds*180+1):
    	t.forward(diameter)
    	t.right(179)
    	print "Round "+ str(x) + " finished!"
circleDrawing(int(input("How big will the circle be?")),int(input("How many times will the circle be drawn?")),str(input("What color will the circle be?")), str(input("How fast will the circle be drawn? (0:Instant, 10:Fast, 6:Normal, 3:Slow, 1:Slowest)")))
