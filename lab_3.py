from rect import Rectange
from square import Square
from circle import Circle

r = Rectange("blue", 3, 5)
s = Square("red", 4)
c = Circle("dark", 10)
arr = [r, s, c]
for i in range(3):
    print (arr[i])