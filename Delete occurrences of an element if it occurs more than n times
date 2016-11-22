Enough is enough!

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like this sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Task

Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example

  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
  



——————————————————————————————————————————————————————————————————————————————————————
Solution:

def delete_nth(order,max_e):
    # code here
    
    
——————————————————————————————————————————————————————————————————————————————————————

Example Tests:
Test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
Test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])



——————————————————————————————————————————————————————————————————————————————————————
自己的做法
def delete_nth(order,max_e):
    dict1 = {}
    for x, y in enumerate(order):
        if not dict1.get(y, 0):
            dict1[y] = 1
        else:
            if dict1[y] == max_e:
                order.pop(x)
            else:
                dict1[y] += 1
    return order
    # code here
    
    
    这种做法是会出错的 原因就是pop之后会改变这个列表的结构  导致进行下次循环的时候跳过一些数字，  debug的强大
    
    所以在修改后是这样的
    
    
    def delete_nth(order,max_e):
    dict1 = {}
    order1 = []
    for x, y in enumerate(order):
        if not dict1.get(y, 0):
            dict1[y] = 1
            order1.append(y)
        else:
    
            if dict1[y] == max_e:
                pass
            else:
                dict1[y] += 1
                order1.append(y)
    return order1
    # code here
    
    
    最后通过
    
    
    ——————————————————————————————————————————————————————————————————————————————————————

    日了狗了 别人的做法如下。。。。
    
    
    def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

    from collections import defaultdict

    def delete_nth(order,max_e):
        c = defaultdict(int)
        def count(x):
            c[x] += 1
            return c[x] <= max_e
        return filter(count, order)
