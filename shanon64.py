#!/usr/bin/python3

import math
import base64
import matplotlib.pyplot as plt 

def s_range(s): return (ord(c) for c in set(s))

def stringH(string):
    if not string:
        return 0
    entropy = 0
    for x in s_range(string):
        p_x = float(string.count(chr(x)))/len(string)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

def encodeXtimes(x, s):
    out = s.encode('ascii')
    for i in range(x):
        out = base64.b64encode(out)
    return out.decode('ascii')



base = 'complexmdpdfkgr'
xaxes = []
yaxes = []
for i in range(50):
    xaxes.append(i)
    subject = encodeXtimes(x=i, s=base)
    h = stringH(subject)
    yaxes.append(h)

print(xaxes)
print(yaxes)
plt.plot(xaxes, yaxes)

plt.savefig('res.png')
plt.show()
