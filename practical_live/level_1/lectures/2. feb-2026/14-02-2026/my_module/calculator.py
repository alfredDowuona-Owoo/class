import time


class Calculator:
    def __init__(self):
        self.__history= []
        
    def add(self,*args):
        total=0
        for i in args:
            total+=i

            t=time.time()

            self.__history.append({f"Add_{t}": {str(args) :total}})
            return total
        
    def get_history(self):
        print(self.__history)

    def hello_world(self):
        print("hello world")


print(__name__)
if __name__=='__main__':
    Calculator.hello_world()

    c = Calculator()
    c.add(1,2,3,4)
    c.add(1,2,3,4,1000)
    c.add(1,2,3,4,17821000)
    c.add(1,-100,3,4,1000)

