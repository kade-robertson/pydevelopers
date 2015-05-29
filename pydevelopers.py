import sys

def tobf(s):
    s = s.replace('\n'," ").replace('\r\n'," ")
    s = s.replace("Developers"*8, "]")
    s = s.replace("Developers"*7, "[")
    s = s.replace("Developers"*6, ".")
    s = s.replace("Developers"*5, ",")
    s = s.replace("Developers"*4, "<")
    s = s.replace("Developers"*3, ">")
    s = s.replace("Developers"*2, "-")
    s = s.replace("Developers", "+")
    s = s.replace(" ", "")
    return s

try:
    f = open(sys.argv[1], 'r')
    program = tobf(f.read())
    d={'>':'p+=1\n','<':'p-=1\n','+':'n[p]+=1\n','-':'n[p]-=1\n','.':'print(unichr(n[p]),end="")\n',',':'n[p]=raw_input()\n','[':'while n[p]:\n',']':''}
    s='from __future__ import print_function\nn=[0]*32768\np=0\n'
    i=0
    for c in program:
        s += ' '*i + d[c]
        if c=='[': i+=1
        if c==']': i-=1; s += '\r'
    exec(s)
    raw_input()
except:
    print "Unable to process program!"
    raw_input()
