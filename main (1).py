#1.1 Implient a recursiv funtion to calculate the factorial of given number.

"""
1!=1*1
2!=2*1!--->2
3!=3*2!--->3*2*1
.
.
10!=10*9!--->10*9*8*...*1

"""



def fact rec(n)
if n==0 or n==1:
return 1
else:
return n*fac rec(n-1)

number=int(input("Enter a value :"))
res=fact rec(number)

print("The fatoril of{} is {}".format(number,res))
 