7 kyu
You're a square!

A square of squares

You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task

Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.
The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples

is_square (-1) # => false
is_square   3 # => false
is_square   4 # => true
is_square  25 # => true
is_square  26 # => false





————————————————————————————————————————————————————————————————————

Example Tests:


import random

test.describe("is_square")
test.it("should work for some examples")
test.expect(not is_square(-1), "Negative numbers cannot be square numbers")
test.expect(not is_square( 3))
test.expect(    is_square( 4))
test.expect(    is_square(25))
test.expect(not is_square(26))

test.it("should work for random square numbers")
for i in range(1,100):
        r = random.randint(0, 0xfff0)        
        test.expect(is_square(r * r), "{number} is a square number".format(number=(r * r)))
        
        
        
————————————————————————————————————————————————————————————————————


Solution:



def is_square(n):
    for x in xrange(0, n):
        if x*x == n :
            return True  
    return False
                
最初的想法是用开方取整再平方看是不是等于原来的  但是不能导入math包              
通过了 但是时间很长，这种算法题最好用C   



______________________________________________________________
2016年11月21日14:32:54

更新两个答案

1.
from math import sqrt

def is_square(n):
    return n > 0 and sqrt(n).is_integer()
    
2.
def is_square(n):  
    return n>0 and (n**0.5).is_integer()
    
这两个本质上是差不多的   

3.
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

4.
is_square = lambda n: n > 0 and int(float(n) ** 0.5) ** 2 == n

lambda表达式一定要用好 上面就是一个例子

    

