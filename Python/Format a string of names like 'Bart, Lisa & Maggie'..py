Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

————————————————————————————————————————————————————
Solution:

def namelist(names):
    
    #your code here
    
————————————————————————————————————————————————————


Example Tests:

Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
"Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
"Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
"Must work with two names")
Test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
Test.assert_equals(namelist([]), '', "Must work with no names")

————————————————————————————————————————————————————

首先我的思路是判断长度 0 1 2 3和3以上这几种 但是太傻了

那么其次的思路就是用逗号来给它们都分割开，然后把最后一个逗号替换成& 

然后的思路就是用' & '.join 这种 然后判断最后一个name的长度 来进行切片修改 但是这样也比较弱智

那么能想到的最好的方法就应该是


self.ziduan = ['linkman', 'telephone', 'crawler_time', 'data_source', 'url', 'city', 'district', 'scope','location']
self.seq = ['"', '"', '', '"', '"', '"', '"', '"', '"']

        
sql = "insert into house.house_sale_jingjiren ({}) values ({})".format(
                        ",".join([item for item in self.ziduan]),
                        ",".join([j + house_dict[i] + j for j, i in zip(self.seq, self.ziduan)]))

类似这种用法的 zip   

——————————————————————————————————————————————————————————————————、
2016年11月22日10:25:06

zip的方法先不管    现在的思路是把这个所有都换成& 然后把除了最后一个都换成，

所以现在的方法是这样的

import re
#正则
def namelist(names):
    kong = []
    for x in range(len(names)):
        kong.append(names[x]['name'])
    zuizhong = '& '.join(kong)
    return re.sub('&', ',' ,zuizhong,len(names)-2)
    #your code here
    
但是问题就是
Must work with many names: 'Bart, Lisa, Maggie, Homer& Marge' should equal 'Bart, Lisa, Maggie, Homer & Marge'

而且放下这个错误不管 这个可以换成replace 因为没有-1这个功能 所以只能先&后， （仔细理解） 
    
def namelist(names):
    kong = []
    for x in range(len(names)):
        kong.append(names[x]['name'])
    zuizhong = '& '.join(kong)
    return zuizhong.replace('&', ',' ,len(names)-2)
    #your code here
    
    
这时再回头看这个代码  应该这样做

def namelist(names):
    kong = []
    for x in range(len(names)):
        kong.append(names[x]['name'])
    zuizhong = ' & '.join(kong)
    return zuizhong.replace(' &', ',' ,len(names)-2)
    #your code here
    
改成这样   通过 


最后看到里面有这两种答案 

def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
        
———————————————————————————————————————————————
def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
    

思路差不多 可以看




re.sub?
Signature: re.sub(pattern, repl, string, count=0, flags=0)
Docstring:
Return the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string by the replacement repl.  repl can be either a string or a callable; if a string, backslash escapes in it are processed.  If it is a callable, it's passed the match object and must return a replacement string to be used.
File:      f:\winpython-32bit-2.7.10.3\python-2.7.10\lib\re.py
Type:      function


re.sub？
签名：re.sub（pattern，repl，string，count = 0，flags = 0）
Docstring：
返回通过替换字符串中模式的最左边的不重叠的出现通过替换repl获得的字符串。 repl可以是字符串或可调用; 如果一个字符串，反斜杠转义在其中被处理。 如果它是一个可调用，它传递的匹配对象，并必须返回一个替换字符串使用。
文件：f：\ winpython-32bit-2.7.10.3 \ python-2.7.10 \ lib \ re.py
类型：函数
