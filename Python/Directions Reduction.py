'''
Once upon a time, on a way through the old wild west,…

… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed the desert the smart way.

The directions given to the man are, for example, the following:

plan = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST'].
You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

plan = ['WEST']
Other examples: In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away. What a waste of time! Better to do nothing. The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure). In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task

You have to write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South. The Clojure version returns nil when the path is reduced to nothing.

Examples

dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']) => ['WEST']
dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']) => []
Note

All paths can't be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].


————————————————————————————————————————————————————————————————————————————————————————————————————————

Solution:

def dirReduc(arr):
    ... your code
    
————————————————————————————————————————————————————————————————————————————————————————————————————————    
Example Tests:

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assert_equals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])

————————————————————————————————————————————————————————————————————————————————————————————————————————
'''


自己第一次写的

plan = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
basic = ['EAST', 'SOUTH', 'WEST', 'NORTH']
n = [10,2,3,3]
final = []
try:
    for i  in xrange(len(plan)):
        if abs(basic.index(plan[i])- basic.index(plan[i+1])) == 2 :
            plan.pop(i)
        else:
            final.append(plan[i])
except:
    pass
print final

虽然用单个pop加上append越过去了删除列表造成的索引混乱，但是还是问题很大 
1.最后两个没法处理，
2.而且不能多次遍历，一环套一环的没法解决

先解决第一个问题：
plan = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
basic = ['EAST', 'SOUTH', 'WEST', 'NORTH']
n = [10,2,3,3]
final = []
try:
    for i  in xrange(len(plan)):
        if abs(basic.index(plan[i])- basic.index(plan[i+1])) == 2 :
            plan.pop(i)
        else:
            final.append(plan[i])
except:
    # final.append(plan[-2])
    final.append(plan[-1])
old = len(final)
new = old.copy
print final

这个是这样的 执行结果是：['SOUTH', 'NORTH', 'WEST']

下面解决多次循环的问题

...好像解决不了  看答案吧。。2016年11月28日15:50:00

————————————————————————————————————————————————————————————————————————————————————————————————————————
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
    
————————————————————————————————————————————————————————————————————————————————————————————————————————
def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3
————————————————————————————————————————————————————————————————————————————————————————————————————————
def dirReduc(arr):
    i = 1
    while i < len(arr) and len(arr) > 1:
        if sorted([arr[i], arr[i-1]]) in [["NORTH", "SOUTH"], ["EAST", "WEST"]]:
            del arr[i-1:i+1]
            i = 1
        else:
            i += 1
    return arr
————————————————————————————————————————————————————————————————————————————————————————————————————————
def dirReduc(arr):
    dir_ = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    hold = []
    for index, dir in enumerate(arr):
        (hold.pop()) if hold and hold[-1] == dir_[dir] else hold.append(dir)
    return hold
————————————————————————————————————————————————————————————————————————————————————————————————————————
def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    
    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    
    return arr    
————————————————————————————————————————————————————————————————————————————————————————————————————————
def dirReduc(arr):
    d={"NORTH":1, "SOUTH":-1, "EAST":2, "WEST":-2,'REMOVED':3}
    while True:
        f=True
        for i in range(len(arr)-1):
            if d[arr[i]]+d[arr[i+1]]==0:                
                arr[i]='REMOVED'
                arr[i+1]='REMOVED'
                f=False
                break
        if f: break
        arr.remove('REMOVED')
        arr.remove('REMOVED')        
    return arr
————————————————————————————————————————————————————————————————————————————————————————————————————————
NULLABLES = [['NORTH', 'SOUTH'], ['SOUTH', 'NORTH'], ['EAST', 'WEST'], ['WEST', 'EAST']]

def dirReduc(arr):
    if len(arr) <= 2:
        return arr if arr not in NULLABLES else []
    for i in range(len(arr)-1):
        if arr[i:i+2] in NULLABLES:
            return dirReduc(arr[:i] + arr[i+2:])
    return arr
————————————————————————————————————————————————————————————————————————————————————————————————————————
def dirReduc(arr):
    ix = 0
    while ix < len(arr)-1:
      if arr[ix][0] + arr[ix+1][0] in ["NS", "SN", "EW", "WE"]:
        arr[ix:ix+2] = []
        if ix: ix -= 1
      else:
        ix += 1
    return arr
————————————————————————————————————————————————————————————————————————————————————————————————————————
def dirReduc(arr):
    check=-1
    while check!=len(arr):
        check,i=len(arr),0
        while i<len(arr)-1:
            if sorted(arr[i:i+2])==['NORTH','SOUTH'] or sorted(arr[i:i+2])==['EAST','WEST']: arr=arr[:i]+arr[i+2:]
            i+=1
    return arr
————————————————————————————————————————————————————————————————————————————————————————————————————————
def get_tos(stack):
  try :
       return stack[-1]
     except IndexError:
       return None
        
def dirReduc(arr):
  stack = list()
     for elem in arr:
       top = get_tos(stack)
       if top :
         if elem == 'SOUTH' and top == 'NORTH' or \
               elem == 'NORTH' and top == 'SOUTH' or \
                elem == 'EAST' and top == 'WEST' or \
               elem == 'WEST' and top == 'EAST' :
          stack.pop()
        else :
         stack.append(elem)
      else:
         stack.append(elem) 
  return stack

