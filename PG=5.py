#generate all pythagorean triplets with side length
def pyth(a):
    count=0
    for i in range(1,a+1):
        for j in range(1,a+1):
            for k in range(1,a+1):
                if(i**2 + j**2 ==k**2 or i**2 + k**2 ==j**2 or k**2 + j**2 ==i**2):
                    count=count+1
    return count
a=int(input("enter the number="))
n=pyth(a)
print(n)
      
