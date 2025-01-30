#calculate sin(x) ;x is a radian value.
def fect(c):
    fact=1
    for i in range(1,c+1):
        fact = fact*i
    return fact
def value(x,y):
    r=x*3.14159/180
    sum=0
    for i in range(1,1+y):
        sum=sum+(r**(2*i-1))*((-1)**(1+i))/fect(2*i-1)
    return sum
a=int(input("enter the value of x in sin(x)= "))
y=int(input("how many termsn you want = "))
print("sum = ",value(a,y))
        
