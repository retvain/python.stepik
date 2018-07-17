#a = int(input())
#b = int(input())
#h = int(input())
#if a <= h <= b:
#    print ('Это нормально')
#elif h < a:
#    print ('Недосып')
#else:
#    print ('Пересып')
########################################################
#a = int(input())
#if (a % 4 == 0) and ((a % 100 != 0) or (a % 400 == 0)):
#        print ('Високосный')
#else:   print ('Обычный')
########################################################
#a = int(input())
#b = int(input())
#c = int(input())
#p = (a+b+c)/2
#print ((p*(p-a)*(p-b)*(p-c))**0.5)
########################################################
#a = int(input())
#print ((-15 < a <= 12) or (14 < a < 17) or (19 <= a))
########################################################
#a = float(input())
#b = float(input())
#c = input()
#if c == '+':
#    print (a + b)
#elif c == '-':
#    print (a - b)
#elif c == '*':
#    print (a * b)
#elif c == 'mod' and b != 0:
#    print (a % b)
#elif c == 'pow':
#    print (a ** b)
#elif c == 'div' and b != 0:
#    print (a // b)
#elif c == '/' and b != 0:
#    print (a / b)
#else:
#    print ('Деление на 0!')
########################################################
#name = input('Введите фигуру \n')
#if name == 'треугольник':
#    a = float(input())
#    b = float(input())
#    c = float(input())
#    p = (a+b+c)/2
#    print((p*(p-a)*(p-b)*(p-c))**0.5)
#elif name == 'прямоугольник':
#    a = float(input())
#    b = float(input())
#    print(a*b)
#elif name == 'круг':
#    r = float(input())
#    print(3.14*(r**2))
########################################################
#a = int(input())
#b = int(input())
#c = int(input())
#if a>=b and a>=c:
#    print(a)
#elif b>=a and b>=c:
#    print (b)
#else: print (c)
#if a<=b and a<=c:
#    print(a)
#elif b<=a and b<=c:
#    print (b)
#else: print (c)
#if (a>=b or a>=c) and (a<=b or a<=c):
#    print (a)
#elif (b>=a or b>=c) and (b<=a or b<=c):
#    print (b)
#else: print(c)
########################################################
#n = int(input())
#if (n % 10 == 1 or n % 100 == 1) and (n != 11) and (n % 100 != 11):
#    print(n, 'программист')
#elif (2 <= (n % 10) <= 4) and not (11 <= n % 100 <= 14):
#    print(n, 'программиста')
#else:
#    print(n, 'программистов')
########################################################
a = int(input())
if ((a//100000) + (a%10000) + (a%1000)) == ((a%10) + (a%100) + (a%1)): print ('Счастливый')
else: print('Обычный')












































