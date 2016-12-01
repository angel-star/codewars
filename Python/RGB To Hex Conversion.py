The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3


————————————————————————————————————————————————————————————————————————————————————————————
Solution:
def rgb(r, g, b):
    #your code here :)
    
————————————————————————————————————————————————————————————————————————————————————————————    
Example Tests:
test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")

————————————————————————————————————————————————————————————————————————————————————————————



直接转化为16进制的是hex()
下面是自己的方法

def rgb(r, g, b):
    list1= [r/1,g/1,b/1]
    for x in xrange(len(list1)):
        if list1[x] < 0: list1[x] =0
        elif list1[x] > 255 : list1[x] =255
        pass
    # print list1
    list1[0]*=2**16
    list1[1]*=2**8
    
    final = hex(list1[0] +list1[1] +list1[2] ).upper()
    # final = final
    while len(final)< 8 :
        final = final[:2] + '0' + final[2:]
    return final[-6:]

————————————————————————————————————————————————————————————————————————————————————————————


def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
    
    
    
————————————————————————————————————————————————————————————————————————————————————————————
def rgb(r, g, b):
    clamp = lambda x: max(0, min(x, 255))
    return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))
————————————————————————————————————————————————————————————————————————————————————————————
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
————————————————————————————————————————————————————————————————————————————————————————————
def rgb(r, g, b):
    return '{0:02X}{1:02X}{2:02X}'.format(max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0))
————————————————————————————————————————————————————————————————————————————————————————————

def rgb(*args):
  return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args));
