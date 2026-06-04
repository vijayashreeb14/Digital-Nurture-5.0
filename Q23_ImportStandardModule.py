import math

def area_of_circle(radius):
    if radius <= 0:
        print("Invalid Radius")
        return

    area = math.pi * radius ** 2

    print(f"Area of Circle: {area:.2f}")

area_of_circle(5)