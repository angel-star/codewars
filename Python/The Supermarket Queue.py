There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

The function has two input variables:

customers: an array (list in python) of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
The function should return an integer, the total time required.

Assume that the front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free. So, for example:

queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool

————————————————————————————————————————————————————————————————————————————————————————
Solution:

def queue_time(customers, n):
    # TODO
    
————————————————————————————————————————————————————————————————————————————————————————    
Example Tests:
Test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
Test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
Test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
Test.assert_equals(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
Test.assert_equals(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
Test.assert_equals(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")
 
# add your own test cases here
————————————————————————————————————————————————————————————————————————————————————————

def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
    
    
————————————————————————————————————————————————————————————————————————————————————————
def queue_time(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c
    return max(qn)
    
————————————————————————————————————————————————————————————————————————————————————————    
def queue_time(customers, n):
    tills = [0 for i in range(n)]

    for time in customers:
        min_index = tills.index(min(tills))
        tills[min_index] += time

    return max(tills)
————————————————————————————————————————————————————————————————————————————————————————    
def queue_time(customers, n):
  fcus=customers[:n]
  for c in range(n,len(customers)):
    fcus[fcus.index(min(fcus))] += customers[c]
  if len(fcus)== 0:
    return 0
  else:
    return max(fcus)    
————————————————————————————————————————————————————————————————————————————————————————

from collections import Counter

def queue_time(customers, n):

  i = n
  c = Counter(customers[:n])
  
  while i < len(customers):
    m = min(c)
    z = c[m]
    c.pop(m)
    
    c += Counter(x+m for x in customers[i:i+z])
    i += z
  
  return max(c, default=0)
————————————————————————————————————————————————————————————————————————————————————————

def queue_time(cu, n):
    q=[0]*n
    for i in cu:
        s=q.index(min(q))
        q[s]+=i
    return max(q)  

