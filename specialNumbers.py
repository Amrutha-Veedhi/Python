#python 3.6
"""
The final project consists of multiple portions. The first three parts consists of writing functions and the final part consists of sorting a list of numbers using those functions. They are as follows:

Part 1
A palindrome is a number which reads the same forward and backwards.
To illustrate:
10101,131,1331,1225221,2 are examples of palindromes
122,100,19 are examples of numbers which are not palindromes.
Write a function that given a number determines if the number is a palindrome or not. Your function should take in a number and return “yes” or “no” depending if it’s a palindrome or not.

Part 2
Write a function that given a number determines if the number is near prime. To understand what is near prime let us first understand what a prime number is.
A number is prime is it is only divisible by 1 and itself.
2,5,13,23 are examples of prime numbers.
4,22,100,60 are examples of numbers which are not prime numbers.
Consider a number such as 49. It is not a prime number because it is divisible by 7. However, it is not divisible by anything else apart from 1, 7 and 49.
We call a number near prime if it is divisible by 1, itself and at most 2 other numbers. To illustrate:
49 is near prime as only 1,7 and 49 divide it.
22 is near prime as only 1,2,11,22 divide it.
4 is near prime as only 1,2,4 divide it.
60 is not near prime as 1,2,3,5,6,10,12,20,30,60 divide it.
17 is near prime as only 1,17 divide it
20 is not near prime as 1,2,4,5,10,20 divide it.
Write a function which determines if a number is near prime or not.
Your function should take in a number and return “yes” or “no” depending if it’s a near prime or not.

Part 3
We call a number an up number if the digits of the number increase (or stay the same) as we read the number. To illustrate:
123 is an up number
2577 is an up number
598 is not an up number
Similarly, in a down number the digits of the number decrease (or stay the same). To illustrate
321 is a down number
775 is a down number
123 is not a down number.
Finally combining the two we define an updown number. In an updown number the digits initially increase (or stay the same) and then they decrease (or stay the same). Once they have started to decrease they can not increase again.
To illustrate
123431 is an updown number
4577852 is an updown number
123758 is not an updown number (because it the digits increased and then decreased but then increased again)
4789089 is not an updown number.
We consider a number “nice” if its either an up, a down or an updown number.
Write a function which given a number determines if it is a nice number. Your function should take in a number and return “yes” if it is an up, a down or an updown number. Your function should return “no” otherwise. That is to say if the number is nice it should return yes and no otherwise.

Part 4.
You will be given a list of numbers. Each number is assigned a score. Its score is determined as follows:
A number’s base score is the value of the number itself.
If the number is a palindrome it scores is doubled.
If the number is a prime its score is doubled.
If the number is a nice number its score is tripled.
Consider how to determine the score of a number 89.
It is not a palindrome and but it is nice and near prime:
Base score: 89
Score after palindrome check: 89 (remains same as not a palindrome)
Score after prime check: 188 (doubled as 89 is prime)
Score after nice check: 534 (tripled as 89 is nice)
Consider the number 101:
It is a palindrome, it is prime but it is not a nice number:
Base score: 101
Score after palindrome check: 202 (doubled as it’s a palindrome)
Score after prime check: 404 (doubled as 101 a prime)
Score after nice check: 404 (not tripled as 101 is not nice)
Given a list of numbers entered by the user output the list of numbers in sorted order (ascending) of their scores.

"""
def isPalindrome(num):
        try:
                if isinstance(num,int):
                        if num == int(str(num)[::-1]):
                            ptr = "Yes"
                        else:
                            ptr = "No"
                return ptr
        except:
                print("{} is not a number".format(num))
def nearPrime(num):
        try:
                l=[]
                if isinstance(num,int):
                        for i in range(1,num):
                                if num%i==0:
                                        l.append(i)
                        count=len(l)
                        if count <=4:
                                ptr = "Yes"
                        else:
                                ptr = "No"
                return ptr
        except:
                print("{} is not a number".format(num))
                
def isNiceNumber(num):
        try:
                l=[]
                l2=[]
                l3=[]
                l4=[]
                l5=[]
                if isinstance(num,int):   
                        s=str(num)
                        for ss in s:
                                l.append(ss)
                        l1=list(map(int, l))
       
                        for i in range(len(l1)-1):
                                if l1[i]<=l1[i+1]:
                                        l2.append("Yes")
                                else:
                                        l2.append("No")
       
                        if all(x=="Yes" for x in l2):
                                ptr = "Yes"
                
                        else:
                                ptr = "No"
                        if ptr == "Yes":
                                return ptr
                
                        else:
                                for i in range(len(l1)-1):
                                        if l1[i]>=l1[i+1]:
                                                l3.append("Yes")
                                        else:
                                                l3.append("No")
                
                                if all(x=="Yes" for x in l3):
                                        ptr = "Yes"
                                else:
                                        ptr = "No"
                                if ptr == "Yes":
                                        return ptr
                                else:
                                        ind = l2.index("No")
                        
                                        for i in range(ind,len(l1)-1):
                                            if l1[i]>=l1[i+1]:
                                                l5.append("Yes")
                                            else:
                                                l5.append("No")
                            
                                        if all(x=="Yes" for x in l5):
                                            ptr = "Yes"
                
                                        else:
                                            ptr = "No"
                return ptr
        except:
                print("{} is not a number".format(num))

def score(li):
        try:
                if (isinstance(li,list) and all(isinstance(x, int) for x in li)):
                        l1=[]
                        for x in li:
                                if (palindrom(x)=="Yes"):
                                        
                                        if nearprime(x)=="Yes":
                                                if nice(x)=="Yes":
                                                        l1.append(12*x)
                                                        
                                                else:
                                                        l1.append(4*x)
                                                        
                                        elif nice(x)=="Yes":
                                                l1.append(6*x)
                                               
                                        else:
                                                l1.append(2*x)
                                                
                                else:
                                        l1.append(x)
                                if nearprime(x)=="Yes":
                                        
                                        if nice(x)=="Yes":
                                                l1.append(6*x)
                                                
                                        else:
                                               l1.append(2*x) 
                                else:
                                      l1.append(x)  
                                if (nice(x)=="Yes"):
                                        l1.append(2*x)
                                        
                                else:
                                        l1.append(x)
                l1=sorted(l1)
                return l1
        except:
                print("{} is not a list of numbers".format(li))
            
