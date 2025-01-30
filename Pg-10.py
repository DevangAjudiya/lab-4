#genrate N number of fibonaki series.
def fibonaki(a):
    t1=1
    t2=1
    now= t1+t2
    print(t1,",",t2,",",now,",",end="")
    for i in range(a):
        t1=t2
        t2=now
        now=t1+t2
        print(now,",",end="")
n=int(input("enter the numer of terms you want= "))
fibonaki(n)
