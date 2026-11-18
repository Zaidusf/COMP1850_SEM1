# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Point, Circle

c = Circle(5, Point(0, 0))
p1 = Point(2, 3)
p2 = Point(6, 0)

print(p1 in c)
print(p2 in c)
