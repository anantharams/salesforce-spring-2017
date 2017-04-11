class SimpleClass(object):
  def __init__(self, a, b=3):
    self.a=a
    self.b=b


c1 = SimpleClass(4)
print c1.a
print c1.b

c1.random = lambda i:i*i
print c1.random(5)

print getattr(c1,'b')
setattr(c1, 'a', 432)
print getattr(c1,'a')


class House (object):
  def __init__ (self, npets, sqft):
    self.number_of_pets = npets
    self.square_footage = sqft
  
  def __str__(self):
    return "<House: %d pets, %d sqft>" %(self.number_of_pets, self.square_footage)

  def __repr__(self):
    return "<House: %d , %d>" %(self.number_of_pets, self.square_footage)


h1 = House (4,950)
print h1
print [h1]



#COMPARISON

elements = [
    (14,"apple",True),
    (10,"banana",False),
    (15,"cantelope",True),
  ]

elements.sort()
print elements

elements.sort (key = lambda x: x[1])
print elements

