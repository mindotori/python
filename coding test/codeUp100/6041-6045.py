# 6041
a,b = input().split()
c = int(a) % int(b)
print(c)

# 6042
a = input()
a = float(a)
print(format(a, ".2f")) #소수 둘째 자리까지 반올림하여 출력

# 6043 
a,b = input().split()
c = float(a) / float(b)
print(format(c, ".3f")) 

# 6044
a,b = input().split()
a = int(a)
b = int(b)
if b != 0:
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
    print(format(float(a)/float(b),".2f"))

# 6045
a,b,c = input().split()
sum = int(a)+ int(b)+ int(c)
avg = float(sum / 3)
print(sum, format(avg,".2f"))