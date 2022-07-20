a=20
def f1():
    print("outer fun")
    def f2():
        print("inner fun")
    f2()
f1()    
