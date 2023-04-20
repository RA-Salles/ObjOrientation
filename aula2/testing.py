# Para contornar o problema do spyder 5.1.5 faça:
# conda remove spyder
# conda remove python-language-server
# conda update anaconda
# conda install spyder=5.3.3
# https://stackoverflow.com/questions/69704561/cannot-update-spyder-5-1-5-on-new-anaconda-install


from some_library.funnyman import supahdatetime as temp
from some_library.funnyman import c_FUNNYMAN as FUNNY


def testfunction1():
    time = temp(13,1,12)
    time.format()
    time.format(format = 'mil')

def testfunction2():
    time = temp(20, 8, 3)
    time.format(format = 'mil')
    print(time.get())


if __name__ == "__main__":
    print(FUNNY)
    testfunction1()
    testfunction2()
