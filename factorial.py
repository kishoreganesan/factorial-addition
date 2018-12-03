import math

n = int(input("Enter the number : ")) 

factadd = 0 #used for factorial function

factadd1 = 0 #used for navie method

fact1 = 1 #used for navie method

factlist = [] #used for factorial function

factlist1 = [] #used for navie method

#using factorial function
for i in range(1, n+1):
    fact = math.factorial(i)
    factlist.append(fact)
print(f"The array of factorial numbers : {factlist}")

for i in factlist:
    factadd = factadd + i #this line does 1!+ 2! +.....+ n!
print(f"The addition of factorial numbers : {factadd} \n ")

#using navie method to compute factorial
for i in range(1, n+1):
    fact1 = fact1 * i
    factlist1.append(fact1)
print(f"The array of factorial numbers : {factlist1}")
    
for i in factlist1:
    factadd1 = factadd1 + i #this line does 1!+ 2! +.....+ n!
print(f"The addition of factorial numbers : {factadd1}")