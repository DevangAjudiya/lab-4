#print npr and ncr
def fact(a):
    fact=1
    for i in range(1,a+1):
        fact = fact*i
    return fact
        
def npr(n,r):
    npr=fact(n)/fact(n-r)
    return npr
def ncr(n,r):
     ncr=fact(n)/(fact(r)*fact(n-r))
     return ncr
n=int(input("enter the value of n="))
r=int(input("enter the value of r="))
print("the value of ncr is ",ncr(n,r))
print("the value of npr is ",npr(n,r))

