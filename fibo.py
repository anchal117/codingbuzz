#fibonacci series 
def fibo(n):
a=0
b=1
if n<0:
print("Wrong input")
else if n==0:
return a=0
else if n==1:
return b=1
else:
for i in range(2,n):
c=a+b
a=b
b=c
return b
print(fibo(9))
