The input is a string str of digits. Cut the string into chunks of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse it; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
Examples:
revrot("123456987654", 6) --> "234561876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "44668753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> ""

————————————————————————————————————————————————————————————
Solution:

def revrot(strng, sz):
    # your code
    
    
————————————————————————————————————————————————————————————    
Example Tests:

def testing(actual, expected):
    Test.assert_equals(actual, expected)
    
Test.describe("revrot")
Test.it("Basic tests")
testing(revrot("1234", 0), "")
testing(revrot("", 0), "")
testing(revrot("1234", 5), "")
s = "733049910872815764"
testing(revrot(s, 5), "330479108928157")
————————————————————————————————————————————————————————————
2016年11月23日14:31:15
自己的做法  但是不知道为什么提示有异常

后来整体加了try块  异常的问题解决了 新的问题又出现了  最后一长串的数字是这样的  
73304991087281576455176044327690580265896 8

然后导致了第二块的第一个0  在转化成int类型时  直接被省略了  这就比较操蛋了
所以加上了    while len(num_lb)< sz:
        num_lb.append(0)
        
        
        

def revrot(strng, sz):
    if len(strng)== 0 and sz == 0 :
        return ''
    zuizhong = ''
    linshi = []
    num_lb = []
    index = 0
    for x in xrange(len(strng)/sz):
        linshi.append(strng[index:index+sz])
        index += sz
    
    linshi = map(int, linshi)
    for y in linshi :
        while y >= 0:
            num_lb.append(y % 10)
            y /= 10
            if y == 0:
                break
        num_lb = num_lb[::-1]
        x = 0
        #各个位数相加
    
        for sum in num_lb:
            x += sum
        if x%2 ==0:
            #如果能整除 翻转
            x = str(x)
            num_lb = num_lb[::-1]
            num_lb = map(str,num_lb)
            num_lb = ''.join(num_lb)
            zuizhong += num_lb
        else:
            #不能整除，左移
            num_lb.append(num_lb[0])
            num_lb.pop(0)
            num_lb = map(str,num_lb)
            num_lb = ''.join(num_lb)
            zuizhong += num_lb
        num_lb = []
        
    return zuizhong
    # your code
    
——————————————————————————————————————————————————————————

最后自己的方法是这样的


def revrot(strng, sz):
    print strng,sz
    try:
        if len(strng) == 0 and sz == 0:
            return ''
        final_num = ''
        list1 = []
        num_lb = []
        index = 0
        for x in xrange(len(strng) / sz):
            list1.append(strng[index:index + sz])
            index += sz
    
        list1 = map(int, list1)
        for y in list1:
            while y >= 0:
                num_lb.append(y % 10)
                y /= 10
                if y == 0:
                    break
            while len(num_lb)< sz:
                num_lb.append(0)
            num_lb = num_lb[::-1]
            x = 0
            for sum in num_lb:
                x += sum
            if x % 2 == 0:
                x = str(x)
                num_lb = num_lb[::-1]
                num_lb = map(str, num_lb)
                num_lb = ''.join(num_lb)
                final_num += num_lb
            else:
                num_lb.append(num_lb[0])
                num_lb.pop(0)
                num_lb = map(str, num_lb)
                num_lb = ''.join(num_lb)
                final_num += num_lb
            num_lb = []
    except:pass
    
    return final_num
下面给出的话几个答案
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def revrot(s, n, res=""):
    if not s or n < 1 or n > len(s):
        return ""
    
    while len(s) >= n:
        group = s[:n]
        if sum([int(d)**3 for d in group]) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        s = s[n:]
    
    return res
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def revrot(strng, sz):
    func = lambda x : x[1:] + x[0] if sum(int(i) for i in x) % 2 else x[::-1]
    return "" if sz <= 0 or sz > len(strng) else "".join(func(strng[i:i+sz]) for i in xrange(0, len(strng) - sz + 1, sz))
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def revrot(strng, sz):
    
    def chunks():
        if sz <= 0:
            raise StopIteration
    
        string = strng
        while len(string) >= sz:
            chunk, string = string[:sz], string[sz:]
            yield chunk
    
    def rev_or_rotate(chunk):
        if sum(int(digit)**3 for digit in chunk) % 2 == 0:
            return chunk[::-1]
        
        else:
            return chunk[1:] + chunk[:1]
            
    return "".join(map(rev_or_rotate, chunks()))
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def revrot(strng, sz):
    if sz <= 0 or strng == "" or sz > len(strng):
        return ""
    
    out = ""
    
    for i in range(0, len(strng) // sz):
        part = strng[sz*i:sz*(i + 1)]
        
        if sum([int(x)**3 for x in part]) % 2 == 0:
            out += part[::-1]
        else:
            out += part[1:] + part[0]
    
    return out
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————




