'''Exercise: Iterators
Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.
The iterator should stop when it reaches a limit defined in the constructor.'''
class Fibonacci:
    def __init__(self,limit):
        self.previous=0
        self.current=1
        self.n=1
        self.limit= limit

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < self.limit:
            result= self.previous+ self.current
            self.previous= self.current
            self.current= result
            self.n +=1
            return result
        else:
            raise StopIteration
        
fib_iterator= iter(Fibonacci(9))
while True:
    try:
        print(next(fib_iterator))
    except StopIteration:
        break