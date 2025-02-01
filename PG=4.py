#check given is prime,perfect,armstron,palindrom,automorphic.
def prime(a):
    for i in range(2,a):
        if(a%i==0) and a!=2:
           return False
    return True
def  perfect(a):
    sum=0
    for i in range(1,a):
        if(a%i==0):
            sum=sum+i
    if(a==sum):
        return True
    return False
def armstrong(a):
   sum=0
    rem=0
    b=a
    c=str(a)
    d=len(c)
    if(d>=3):
        while(a!=0):
            rem=a%10
            sum = sum + rem**d
            a=a//10
        if(b==sum):
            return True
    return False
def pelindrom(a):
    rev=0
    rem=0
    b=a
    while(a!=0):
        rem=a%10
        rev = rev*10 + rem
        a=a//10
    if(b==rev):
        return True
    return False
def automorphic(a):
    rev=0
    rem=0
    b=a*a
    str(a)
    str(b)
    l=len(b)
    c=len(a)
    if(b.find(a,l-c,l+1):
        return true
    return false     
a=int(input("enter the number="))
pri=prime(a)
print("prime =",pri)
per=perfect(a)
print("perfect =",per)
arm=armstrong(a)
print("armstrong =",arm)
pelin=pelindrom(a)
print("pelindrom =",pelin)
auto=automorphic(a)
print("pelindrom =",auto)

    
