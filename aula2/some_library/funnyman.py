"""
    Made by locust, without any other known aliases in 040420231228 in format daymonthyearhourminute. 
    Could put some seconds there too, just for the funny, but ain't gonna work well. 

    
"""

import numpy as np

#constants block
c_FUNNYMAN: str = "triple funny man is funny funny funny man! 3x funnier!"

class supahdatetime:
    def __init__(self, hour, minute, second):
        self.tri = [str(hour), str(minute), str(second)] #storing as vector for iteration purposes!
        i = -1
        for bit in self.tri:  #<----- such as these
            i += 1
            if len(bit) < 2: #already checks for nonzeroed stuff. 
                bit = '0' + bit
            self.tri[i] = bit #for whatever reason, it only worked when i did this badness.
        #print(self.tri) #DEBUG
        self.string = ""

    def format(self, **kwarg):
        #clears up old string and makes a new string real quick.
        exec = 0
        self.string = "" #cleanup
        if 'format' in kwarg:
            if kwarg['format'] == 'mil': 
                exec = 1
                for bit in self.tri: #this guy probably already got formated in init, so lets just
                    self.string = self.string + bit + ':' #this here makes stuff like h:m:s:. we gotta get hid of that last :
                self.string = self.string[0: len(self.string) - 1] #kinda bad for processing, but, hey! It will work like a glove... i guess...   
            else: #aqui para indicar que, para implementar outros padrões, basta um elif.
                pass #if this guy passes, some bausy bastarudo went ahead and put some funny inside kwarg. that's why we use the exec flag.
        if exec == 0: #formato padrão é obtido ao não colocar nada no kwarg. Ou colocar um padrão não existente no format
            if int(self.tri[0]) % 12 == 0: 
                h = self.tri[0]
            else: 
                h = str(int(self.tri[0])%12)
            self.string = h + ":" + self.tri[1] + ":" + self.tri[2]
            if int(self.tri[0]) >= 12:
                self.string = self.string + " da tarde"
            else:
                self.string = self.string + " da manhã"
        #print(self.string)
        return self.string
    
    def get(self): #use this to save computation times when you'll use the same format type multiple times.
        return self.string
    
    def funny(self) -> None:
        print(c_FUNNYMAN)
if __name__ == '__main__':
    print(c_FUNNYMAN)
