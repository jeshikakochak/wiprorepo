#custom package
from my_math.arithmetic import add, subtract, multiply,divide
from my_math.geometry import area_circle, area_rectangle
print("add:",add(12,4))
print("subtract:",subtract(12,4))
print("multiply:",multiply(12,4))
print("divide:",divide(12,4))
print("circle area(r=7):",round(area_circle(7),2))
print("rectangle area(5*9):",area_rectangle(5,9))