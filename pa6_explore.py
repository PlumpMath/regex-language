#Exploring Python's generators for Project 6

###Simplest generator examples
def simple_generator_function():
  yield 1
  yield 2
  yield 3

#Two ways to call generators
for value in simple_generator_function():
  print(value)

#Should output:
# 1
# 2
# 3

our_generator = simple_generator_funciton()

next(our_generator)
#Should ouput:
# 1

next(our_generator)
#Should ouput:
# 2

next(our_generator)
#Should ouput:
# 2


###Generator pattern

#This boilerplate code:

class firstn(object):
  def __init__(self, n):
    self.n = n
    self.num, self.nums = 0, []

  def __iter__(self):
    return self

  #For Python 3 compatiability
  def __next__(self):
    return self.next()

  def next(self):
    if self.num < self.n:
      cur, self.num = self.num, self.num+1
      return cur
    else:
      raise StopIteration()

#is equivalent to this Python idiom:

def firstn(n):
  num = 0
  while num < n:
    yield num
    num += 1

#Both can be called with:

sum_of_first_n = sum(firstn(10000))

###Cannonical examples:

#We can rewrite this non-working solution:

def get_primes(start):
    for element in magical_infinite_range(start):
        if is_prime(element):
            return element

def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

#with generator functions as follows:

def get_primes(number):
  while True:
    if is_prime(number):
      yield number
    number += 1

def solve_number_10():

    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

#RangeGenerator:
total = 0
for i in irange(1000000):
	total += 1

#Composing a generator:
square = (i*i for i in irange(100000))
total = 0
for i in square:
	total += i

###Passing values into generators:

def print_successive_primes(iterators, base=10):
  prime_generator = get_primes(base)
  prime_generator.send(None)
  for power in range(iterations):
		print(prime_generator.send(base ** power))