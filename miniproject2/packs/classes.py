"""
    written by locust. 

    standard goes like this:
        every plot-able class should have a list, which should be accessible via name.list.
        classes to be plotted should be passed to the plotter in a list.
        the plotter goes on to extract these point lists and converge them in a single 
        big x, y listing.
        this bigxy is what matplotlib will use to plot everything.
    
    obs1:
        this is a smile :>
        this is angry >:, not sad.
        the angry complete would be >:, but the mouth doesn't look cute enough to pair with :>
        so we :>, >:, and :<. 
    
    donelist!
        plotting functions!
            everything that the classes need to be able to be plotted currently exists!
    
"""

import numpy as np
import matplotlib.pyplot as plt

CONST_DEFAULTPRECISION = 50 #constant of default precision for linspace used along the program
                             #ah yeah, more precision means more memory. Stay aware of that. 
                             #Change this in your own discretion.

class point(): #this guy should never be plotted. 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def update(self,**kw):
        if 'y' in kw:
            self.y = kw['y']
        if 'x' in kw:
            self.x = kw['x']

class circle(point):
    def __init__(self, x, y, radius): #needs a center and a radius. We can reuse point to do just that.
        self.radius = radius
        self.precision = CONST_DEFAULTPRECISION #greater precision means more points
        super(circle, self).__init__(x, y)
        self.genpointlist()

    def genpointlist(self): #generates point lists to be plotted.
        ts = np.linspace(0, 7, self.precision) #7 is just a constant greater than 2*pi. else we generate non whole circles.
        self.list = [[],[]] #x and y. These need to be in order
        for t in ts:
            self.list[0].append(self.radius*np.sin(t) + self.x) #this will create a parametric thingy, which will be very funny funny.
            self.list[1].append(self.radius*np.cos(t) + self.y) #supposedly, if we plot these guys, we get what we want.
        print(self.list)
    
    def getarea(self):
        return np.pi * (self.radius ** 2)
        
    def update(self, **kw): #this guy is keyword only! Therefore, it only updates what it gets passed.
        didsomething = 0
        if 'y' in kw:
            self.y = kw['y']
        if 'x' in kw:
            self.x = kw['x']
        if 'radius' in kw:
            self.radius = kw['radius']
        if 'precision' in kw:
            self.precision = kw['precision'] 
        if didsomething != 0: #meaning
            self.list = [[],[]] #this makes so the list goes back to default, cleaning leftover points
            self.genpointlist()
        pass

class line(): #finit init points in a pair, assuming there's a line of points in between. 
    def __init__(self, plist: list): #this little guy should receive a list of 2 points to work with. No less, no more.
        self.precision = CONST_DEFAULTPRECISION
        while len(plist) > 2: #if it gets more than 2 points, these get discarded
            plist.pop()
        self.points = [[],[]]
        for p in plist: #this should handle creating the init-finit alright.
            self.points[0].append(p.x)
            self.points[1].append(p.y)
        self.getpoints()

    def update(self, plist: list): #regenerates class. 
        while len(plist) > 2: 
            plist.pop()
        self.points = [[],[]]
        for p in plist: 
            self.points[0].append(p.x)
            self.points[1].append(p.y)
        self.getpoints()
    
    def getpoints(self): 
        m = (self.points[1][0] - self.points[1][1])/(self.points[0][0] - self.points[0][1])
        def whatthefunc(x): #this guy will get us the other points on the line.
            y = m*(x - self.points[0][1]) + self.points[1][1]
            return y
        self.generator = whatthefunc
        self.list = [[],[]] #every time we do a getpoints, we wipe the self.list :>
        self.list[0] = np.linspace(self.points[0][0], self.points[0][1], self.precision)
        for xval in self.list[0]:
            self.list[1].append(self.generator(xval))
    
    def getsize(self):
        return np.sqrt((self.points[1][0]-self.points[0][0])**2 + (self.points[1][1]-self.points[0][1])**2 )
                #         dif cords x squared                            dif cords y squared
    
class curve(): #collection of open lines made with an function
    
    def __init__(self, func, init, finit): #func  in this case should be a function of x. This IS a limitation.
        self.generator = func
        self.precision = CONST_DEFAULTPRECISION
        self.init = init
        self.finit = finit
        self.list = [[],[]]
        self.generatepoints()

    def generatepoints(self): #this guy assumes he already got init finit.
        self.list = [[],[]] #preparation.
        xvals = np.linspace(self.init, self.finit, self.precision)
        for val in xvals:
            self.list[0].append(val) #meaning he stores values of x
            self.list[1].append(self.generator(val)) # and y
        

class figure(): #collection of lines -> extract init finit, find points in between. BEWARE: figure class use 100 points FOR EACH LINE due to precision!
    """
        This guy actually needs some major explaining.
        He will generate "lines" from the point pairs you provide.
        thing is:
            he uses the line class and extracts the inner list from inside
            line class and consumes it to create its own biglist,
            which will be accessed by plotter later to create the
            bigxy, which is the defacto biglist of the script.

            The bigxy is in turn passed to matplotlib, which provides major
            lifting and plots the points, as well as displaying it. 
    """
    def __init__(self, plist): #needs pointlist. At least two points, else we might have major problems :>
        i = 0
        self.linelist = [] #this guy stores line class objects.
        while i < len(plist) - 1:
            i += 1 
            self.linelist.append(line([plist[i-1],plist[i]])) #this goes because line works with pointlists!
        self.getpoints()

    def getpoints(self): #generates biglist. 
        self.list = [[],[]] #first we wipe the object's list. 
        for line in self.linelist: #then we do this badness
            for xval,yval in zip(line.list[0],line.list[1]):
                self.list[0].append(xval)
                self.list[1].append(yval)

    def update(self,plist): #basically reinitializes the object. 
        i = 0
        self.linelist = [] #this guy stores line class objects.
        while i < len(plist):
            i += 1 
            self.linelist.append(line([plist[i-1],plist[i]])) #this goes because line works with pointlists!
        self.getpoints()
    
    def getperimeter(self):
        size = 0
        for line in self.linelist:
            size += line.getsize()
        return size
    
class plotter(): #takes a list of geoclasses and extracts the to-be-plotted points, shoves them in a single shingle and plots 'em!
    def __init__(self, classlist):
        self.listofclasses = classlist
        self.getpoints()
    
    def getpoints(self):
        self.bigxy = [[],[]] #cleanup!
        for clas in self.listofclasses: #Type n^2. Badly optimized. Might work on this next time around, but this should work for now.
            print(type(clas))
            for x,y in zip(clas.list[0], clas.list[1]):
                self.bigxy[0].append(x)
                self.bigxy[1].append(y)
        plt.scatter(self.bigxy[0], self.bigxy[1])
        
    def run(self): #this guy should pass to plotter all he got and try to plt.show()
        plt.grid()
        plt.show()

if __name__ == "__main__": #this here shouldn't be done, but i gotta preserve muh style, yeah?
    circ = circle(9, -10, 5)
    def func1(x):
        return x**2 + 3*x - 2
    curv = curve(func1, -10, 10)
    points = [point(1, 2), point(3, 4), point(4, -6), point(-6, 5), point(1, 2)]
    zeda = figure(points)
    print(zeda.getperimeter())
    tobeplotted = []
    tobeplotted.append(circ)
    tobeplotted.append(curv)
    tobeplotted.append(zeda)
    datashower = plotter(tobeplotted)
    datashower.run()
    pass
