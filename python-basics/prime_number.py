def isPrime(num):
    # i is not prime number
    if num==1:
        return False
    # 2 and 3 are prime number and we didnt get there square root
    if num==2 or num==3:
        return True
    #find the square root of the number and check 2 to squareroot+1 range 
    #if except 1 n own number any other nmber can devide it
    # if only two factor then it is prme number
    #eg 25 = square root of 25 = 5, range(2,6)= no one devide to 5 
    # only 1 and 5 is divide so 5 is prime number , 
    # 1 is bydefualt 1 is devide to every number so we are not added into range
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            return False
        return True
    
_num = int(input("Enter Number = "))
checkPrime = isPrime(_num)
if checkPrime == True:
 print(f"{_num} is prime number")
else:
    print(f"{_num} is not a prime number")    

