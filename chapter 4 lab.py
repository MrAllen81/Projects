
from graphics import *
win = GraphWin()
win.close()
p = Point(50,60)
p.getX()
p.getY()
win = GraphWin()
win = GraphWin()
p.draw(win)
p2 = Point(140,100)
p2.draw(win)
win = GraphWin("Shapes")
center = Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)
label = Text(center, "red circle")
label.draw(win)
rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)
line = Line(Point(20,30), Point(180, 165))
line.draw(win)
oval = Oval(Point(20,150), Point(180,199))
oval.draw(win)


leftEye = Circle (Point (80 , 50) , 5)
leftEye.setFill ('yellow')
leftEye.setOutline ('red')
rightEye = leftEye
rightEye.move (20 , 0)
LefEye = rightEye
leftEye.setFill ('yellow')
leftEye.setOutline ('red')



from graphics import *
def main() :
    win = GraphWin("Click Me ! ")
    for i in range(10) :
        p = win.getMouse ()
        print ( "You clicked at :", p.getX(), p.getY())
main()
from graphics import *
def main2() :
    win = GraphWin("Draw a Triangle ")
    win . setCoords (0
    message = Text (Point (5 , 0.5) , "Click on three points ")
    message.draw(win)
# Get and draw three vertices of triangle
    p1 = win.getMouse ()
    p1 . draw(win)
    p2 = win.getMouse ()
    p2 . draw(win)
    p3 = win.getMouse ()
    p3.draw(win)
# Use Polygon object to draw the triangle
    triangle = Polygon (p1 , p2 ,p3)
    triangle.setFill ( "peachpuff ")
    triangle.setOutline ("cyan")
    triangle.draw(win)
# Wait for another click to exit
    message.setText ("Click anywhere to quit . ")
    win.getMouse ()

main2()



