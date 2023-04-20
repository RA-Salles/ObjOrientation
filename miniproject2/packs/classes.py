import numpy as np
import matplotlib.pyplot as plt

CONST_DEFAULTPRECISION = 100 #constant of default precision for linspace used along the program

class point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class circle(point):
    def __init__(self, x, y, radius, precision): #needs a center and a radius. We can reuse point to do just that.
        self.radius = radius
        self.precision = precision #greater precision means more points
        super(circle, self).__init__(x, y)

    def genpointlist(self): #generates point lists to be plotted.
        ts = np.linspace(0, 7, self.precision)
        self.list = [[],[]] #x and y. These need to be in order
        
        for t in ts:
            self.list[0].append(self.radius*np.sin(t) + self.x) #this will create a parametric thingy, which will be very funny funny.
            self.list[0].append(self.radius*np.cos(t) + self.y)

class line(): #finit init points in a pair, assuming there's a line of points in between. 
    def __init__(self,):
        pass

class curve(): #collection of open lines made with an function
    pass

class figure(): #collection of lines
    pass

class plotter(): #takes a list of geoclasses and extracts the to-be-plotted points, shoves them in a single shingle and plots 'em!
    def __init__(self):
        self.listolists = [] #this guy intakes 2dlists

    def saveclass(self,geoclass):
        self.listolists.append(geoclass.list) #this guy extracts the pointlist from the bawsy bastard geoclass he got. should have a structure like [[[],[]],[[],[]],[[],[]],...]
                                              #means plotter
    def run(self): #this guy should pass to plotter all he got and try to plt.show()
        plt.show()
        pass



