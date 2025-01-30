#print multipication table
def table(a):
    for i in range(1,11):
        b=a*i
        print(a,"*",i,"=",b)
n=int(input("enter the number ="))
table(n)
