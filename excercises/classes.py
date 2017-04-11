

"""
A calculator that keeps a memory of its past executions. 

Your job is to finish MyCalculator class. It must inheirit from 
BaseCalculator, and should work like the following:

    c = MyCalculator()     # to start with total=0
    c = MyCalculator(290)  # to start with total=290

You should be able to use the following operations with two
arguments x and y to perform stateless operations:

    print c.add(5, 4)         # 9
    print c.multiply(2, 5.5)  # 11
    print c.subtract(12, 100) # -88
    print c.divide(10, 2)     # 2.5

And stateful operations using the same functions, but with single args:

    c = MyCalculator()           # to start with total=0
    c.add(2)
    print c.get_current_total()  # prints 12
    c.multiply(10) 
    print c.get_current_total()  # prints 120

    # And you should be able to get a list of all past states of total
    print c.get_past_totals()    # print [0, 12, 120]

Run tests with:

    $ py.test tests/test_classes.py::ClassesExcercises
"""

class BaseCalculator(object):
    def __init__(self, starting_total):
        self.total = starting_total

    def get_current_total(self):
        return self.total

class MyCalculator(BaseCalculator):
    def __init__(self, starting_total=0):
        BaseCalculator.__init__(self, starting_total)
        self.past_totals = []
        
    def get_past_totals(self):
        return self.past_totals

    def add(self, n1 , n2 = None):
      if n2 == None:
        n2 = self.total
      self.past_totals.append(self.total)
      BaseCalculator.__init__(self, n1 + n2)
      return n1 + n2

    def subtract(self, n1 , n2 = None):
      if n2 == None:
        n2 = self.total
        self.past_totals.append(self.total)
        BaseCalculator.__init__(self, n2 - n1)
        return n2 - n1
      self.past_totals.append(self.total)
      BaseCalculator.__init__(self, n1 - n2)
      return n1 - n2

    def multiply(self, n1 , n2 = None):
      if n2 == None:
        n2 = self.total
      self.past_totals.append(self.total)
      BaseCalculator.__init__(self, n1 * n2)
      return n1 * n2

    def divide(self, n1 , n2 = None):
      if n2 == None:
        n2 = self.total
        self.past_totals.append(int(self.total))
        BaseCalculator.__init__(self, float(n2)/float(n1))
        return float(float(n2)/float(n1))
      self.past_totals.append(int(self.total))
      BaseCalculator.__init__(self, float(n1)/float(n2))
      return   float(float(n1)/float(n2))
        
