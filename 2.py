##########################################
#a = int(input())
#b = 0
#while a != 0:
#    b += a
#    a = int(input())
#print (b)
##########################################
#a = int(input())
#b = int(input())
#n = 1
#if a == b:
#    print (a)
#else:
#    while ((n % a) != 0) or ((n % b) != 0):
#        n += 1
#    print(n)
##########################################
#n = 0
#while n == 0:
#    a = int(input())
#    if a < 10:
#        continue
#    elif a > 100:
#        break
#    else: print (a)
##########################################
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#for e in range(c, (d+1)):
#    print ('\t', e, end='')
#print()
#for i in range(a, (b+1)):
#    print (i, end='')
#    for j in range(c, (d+1)):
#        print('\t', i*j, end='')
#    print()
##########################################
#a = int(input())
#b = int(input())
#s = 0
#n = 0
#for i in range(a, b+1):
#    if i%3 == 0:
#        s += i
#        n += 1
#print (s/n)
##########################################
#s = input()
#s = s.lower()
#print ((((s.count('c') + (s.count('g')))) / len(s)) * 100)
##########################################
s: str = input()
print (len(s))
k = 0
i = 1
n = ''
ntemp = ''
while k < (len(s) -1):
    if (s[k] == s[k+1]):
        i += 1
        ntemp = s[k]
        k += 1
        continue
    n += ntemp + str(i)
    if (s[k] != s[k+1]) and (s[k] != s[k-1]):
        i = 1
        ntemp = s[k] + '1'
        k += 1
    else:
        i = 1
        ntemp = s[k]
        k += 1
        continue
    n += ntemp
print(n)







