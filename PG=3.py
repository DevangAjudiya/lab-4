#count no of alphabet,digits
def count(st):
    alpha=0
    number=0
    for ch in st:
        if('a'<=ch<='z' or 'A'<=ch<='Z'):
            alpha=alpha+1
        elif('0'<=ch<='9'):
            number=number+1
    print("alphabets=",alpha,"number =",number)
a=input("enter the string")
count(a)
     
