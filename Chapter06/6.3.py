# ball
import math


def area(a):
    a = 4*math.pi*a**3
    return a


def volume(v):
    v = 4/3*math.pi*v**3
    return v


def main():
    r = int(input("r="))
    area(r)
    volume(r)
    print("a=", a)
    print("v=", v)


main()
