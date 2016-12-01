An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: Exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write the function findMissing (list) , list will always be atleast 3 numbers. The missing term will never be the first or last one.

Example :

findMissing([1,3,5,9,11]) == 7
PS: This is a sample question of the facebook engeneer challange on interviewstreet. I found it quite fun to solve on paper using math , derive the algo that way. Have fun!

Solution:
def find_missing(sequence):
    return sequence[0]

Example Tests:
test.assert_equals(find_missing([1, 2, 3, 4, 6, 7, 8, 9]), 5)
————————————————————————————————————————————————————————————————————————————————————————————————————

sequence = [1, 2, 3, 4, 6, 7, 8, 9]
dict1 = {}
for x in xrange(len(sequence)-1):
    cha = sequence[x + 1] - sequence[x]
    if dict1.get(cha, 0):
        dict1[cha] += 1
    else:
        dict1[cha] = 0
print dict1

思路是把差放到字典里 然后再加变量用来存储位置  x浅拷贝。 
自己写的是这样的 但是
输出结果是这样的
{1: 0, 2: 0}

具体问题出在哪？？？？  

2016年11月29日10:57:42 
看答案
————————————————————————————————————————————————————————————————————————————————————————————————————
def find_missing(sequence):
    interval = (sequence[-1] - sequence[0])/len(sequence)
    for previous, item in enumerate(sequence[1:]):
        if item - sequence[previous] != interval:
            return item - interval
            
————————————————————————————————————————————————————————————————————————————————————————————————————
def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)
————————————————————————————————————————————————————————————————————————————————————————————————————
def find_missing(sequence):
    return (sequence[-1] + sequence[0]) * (len(sequence) + 1) / 2 - sum(sequence)
————————————————————————————————————————————————————————————————————————————————————————————————————
def find_missing(sequence):
    totalGap=sequence[len(sequence)-1]-sequence[0]
    eachGap = totalGap/len(sequence)
    for i in range(len(sequence)-1):
        if sequence[i]+eachGap != sequence[i+1]:
            return sequence[i]+eachGap
————————————————————————————————————————————————————————————————————————————————————————————————————

def find_missing(nums):
    a, b, c = nums[:3]
    diff = min(b - a, c - b, key=abs)
    for d in nums:
        if d != a:
            return a
        a += diff
        

————————————————————————————————————————————————————————————————————————————————————————————————————
def find_missing(sequence):
    diff = []
    last = None
    for element in sequence:
        if last is None:
            last = element
        else:
            diff2 = element - last
            last = element
            diff.append(diff2)
            
    i = -1
    #print(diff)
    last = diff[0]
    for element in diff:
        if element != last:
            i += 1
            break
        i += 1
    return sequence[i] + last
————————————————————————————————————————————————————————————————————————————————————————————————————
def find_missing(s):
       return (len(s)+1)*(s[0]+s[len(s)-1])/2-sum(s)   

————————————————————————————————————————————————————————————————————————————————————————————————————

find_missing=lambda s:(s[0]+s[-1])*(len(s)+1)/2-sum(s)



——————————————————————————————————————————————————————————————————————————————————————————————

def find_missing(sequence):
    list1 = sequence[1:]
    list2 = sequence[:-1]
    list3 = map(lambda x,y:x-y,list1,list2)
    if list3[0]*2 in list3:
        return list1[list3.index(list3[0]*2)] - list3[0]
    else:
        return list1[0] - list3[0]/2
        
        
        
——————————————————————————————————————————————————————————————————————————————————————————————
from pprint import pprint
from math import fabs

def find_missing(sequence):
    #pprint(sequence)
    c = sequence[2] - sequence[1]
    for i in range(0, len(sequence)):
        if fabs(sequence[i + 1] - sequence[i]) != fabs(c):
            return sequence[i] + c
    return sequence[0]

——————————————————————————————————————————————————————————————————————————————————————————————
def find_missing(sequence):
    dif1=sequence[1]-sequence[0]
    dif2=sequence[2]-sequence[1]
    dif = min(dif1,dif2) if dif1 >= 0 else max(dif1,dif2)
    missing = set(range(sequence[0],sequence[-1],dif))-set(sequence)
    return missing.pop()

——————————————————————————————————————————————————————————————————————————————————————————————


def find_missing(s):
    diff = set(range(s[0], s[-1]+1, (s[-1] - s[0])/len(s))) - set(s)
    return diff.pop() if diff else 0
