'''

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"



Solution:
def primeFactors(n):

Example Tests:
test.assert_equals(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")


'''

—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
自己做的

# -*- coding: utf-8 -*-
a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
n = 7775460
final = ''
factor_list = []
for x in a:
    quotient, residule = n / x, n % x

    if quotient:
        while not residule:
            n /= x
            factor_list.append(x)
            quotient, residule = n / x, n % x
    else:
        break
print factor_list



输出结果是这样的：[2, 2, 3, 3, 3, 5, 7, 11, 11, 17]

但是目标的格式是这样的 字符串

 "(2**2)(3**3)(5)(7)(11**2)(17)"1

注：这里跟哥德巴赫猜想不一样
参考这里 ：
http://www.cnblogs.com/shiluocn/p/4906019.html




—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
2016年11月28日18:20:44
自己做的

a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
n = 7775460
final = ''
factor_list = []
from collections import Counter
from collections import OrderedDict
for x in a:
    quotient, residue = n / x, n % x

    if quotient:
        while not residue:
            n /= x
            factor_list.append(x)
            quotient, residue = n / x, n % x
    else:
        break
print factor_list
b = Counter(factor_list)
print b.most_common()
for x  in b.most_common():
    final += str(x)
print final.replace(', ', '**')

输出结果是这样的

[2, 2, 3, 3, 3, 5, 7, 11, 11, 17]
[(3, 3), (2, 2), (11, 2), (5, 1), (7, 1), (17, 1)]
(3**3)(2**2)(11**2)(5**1)(7**1)(17**1)
—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
然后最终版 2016年11月28日18:40:21


# -*- coding: utf-8 -*-
a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
n = 7775460
final = ''
factor_list = []
from collections import Counter
from collections import OrderedDict
for x in a:
    quotient, residue = n / x, n % x

    if quotient:
        while not residue:
            n /= x
            factor_list.append(x)
            quotient, residue = n / x, n % x
    else:
        break
print factor_list
b = Counter(factor_list)
L = [[key, val] for key, val in b.items()]
L.sort(key=lambda f: f[0], reverse=False)
L = [[str(v) for v in item] for item in L]
s = ''.join(['**'.join(item).join(['(',')']) for item in L])

print s



输出：
[2, 2, 3, 3, 3, 5, 7, 11, 11, 17]
(2**2)(3**3)(5**1)(7**1)(11**2)(17**1)

然后加上    s = s.replace('**1', '')
等于    "(2**2)(3**3)(5)(7)(11**2)(17)"


笔记：

      输入：
      print factor_list
      b = Counter(factor_list)
      print '1  ',b


      L = [[key, val] for key, val in b.items()]
      print '2 ' , L


      L.sort(key=lambda f: f[0], reverse=False)
      print '3  ',L


      L = [[str(v) for v in item] for item in L]
      print '4  ',L


      s = ''.join(['**'.join(item).join(['(',')']) for item in L])
      print '5  ',s


      输出： 
              [2, 2, 3, 3, 3, 5, 7, 11, 11, 17]
          1   Counter({3: 3, 2: 2, 11: 2, 5: 1, 7: 1, 17: 1})
          2   [[2, 2], [3, 3], [5, 1], [7, 1], [11, 2], [17, 1]]
          3   [[2, 2], [3, 3], [5, 1], [7, 1], [11, 2], [17, 1]]
          4   [['2', '2'], ['3', '3'], ['5', '1'], ['7', '1'], ['11', '2'], ['17', '1']]
          5   (2**2)(3**3)(5**1)(7**1)(11**2)(17**1)


2016年11月28日18:55:33

然后现在又有新问题了就是7919
✘ '' should equal '(7919)'

而我的最大的素数才到了71

所以
—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
2016年11月28日19:13:44
o_list = {2, 3, 3, 3, 5, 7, 11, 11, 17}
t_dict = {}
r_strs = ''
for k, v in enumerate(o_list):
     if v not in t_dict:
          t_dict.setdefault(v, [k,1])
          continue
     t_dict[v][-1] += 1
s_dict = sorted(t_dict.items(), key=lambda s:s[-1][0])
for item in s_dict:
    r_strs += '({0}'.format(item[0])
    if item[-1][-1] <= 1:
        r_strs += ')'
    else:
        r_strs += '**{0})'.format(item[-1][-1])
print r_strs

群里李满满的答案  这个里面没有素数那方面的去重


—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


