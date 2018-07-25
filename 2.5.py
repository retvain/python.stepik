#n = [int(i) for i in input().split()]
#s = 0
#k = len(n)-1
#for c in range(k):
#    s += n[c]
#s += n[-1]
#print (s )
##############################################
#n = [int(i) for i in input().split()]
#t = ''
#c = len(n) - 1
#if c == 0:
#    temp = str(n[0])
#else:
#    for i in range (c):
#        temp = str(n[i-1] + n[i+1])
#        t += temp + ' '
#    temp = str(n[c-1]+n[0])
#t += temp
#print (t)
##############################################
n = [int(i) for i in input().split()]
srt = sorted(n)
c = len(srt) - 1
s = ''
temp = ''
if c == 0:
    s = ''
else:
    for i in range (c):
        if srt[i] == srt [i+1]:
            temp = str(srt[i]) + ' '
        else:
            s += temp
            temp = ''
    if srt[-1] == srt[-2]:
        s += str(srt[-1])
print (s)