from packs.classes import *

jobs = []

def exec(): #here we should enable the user to actually use the functions via cmd.
    def func1():
        pass
    def func2():
        pass
def test():
    circ = circle(9, -10, 5)
    def func1(x):
        return x**2 + 3*x - 2
    curv = curve(func1, -10, 10)
    points = [point(1, 2), point(3, 4), point(4, -6), point(-6, 5), point(1, 2)]
    zeda = figure(points)
    print(zeda.getperimeter()) #this guy in general tests both himself and the ability to find a line's size.
    tobeplotted = []
    tobeplotted.append(circ)
    tobeplotted.append(curv)
    tobeplotted.append(zeda)
    datashower = plotter(tobeplotted)
    datashower.run()
    
if __name__ == "__main__":
    test()