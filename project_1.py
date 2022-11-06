#no guessing project 

import random as r
num=r.randrange(100)
Guess=5
while Guess>=0:
    your_guess=int(input("enter your Guess"))
    def check(x):
        if your_guess==x:
            print("you win")
        elif your_guess>x:
            print("you are close,keep trying lower") 
        else:
            print("you are close,keep trying higher")
    if Guess>1:
        check(num)
    elif Guess==1:
        check(num)
        print("this is your last chance,make the most of it")
    else:
        print("you lost")
    Guess=Guess-1


# next3 scientific calculator project

import math
from unittest import result
from xml.sax.xmlreader import InputSource

from numpy import result_type
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide(a,b):
    return a/b
def sqrt(a):
    result=math.sqrt(a)
    return result
def exp(a):
    return a**2
def sin(x):
    result=math.sin(x)
    z=math.ceil(result)
    return z
def cos(x):
    result=math.cos(x)
    z=math.ceil(result)
    return z
def tan(x):
    result =math.tan(x)
    z=math.floor(result)
    return z
print("""
choose a number for the following operation
1-Addition(x,y)
2-Substraction(x,y)
3-Multiplication(x,y)
4-Divide(x,y)
5-square root(x)
6-square(x)
7-sin(x)
8-cos(x)
9-tan(x)

""")
op=int(input("what operation do you want to perform?"))
while op<10:
    if op==1:
        print("enter the parameters")
        x1=int(input("enter x"))
        y1=int(input("enter y"))
        res1=add(x1,y1)
        print("Addition=",res1)
    elif op==2:
        x2=int(input("enter x"))
        y2=int(input("enter y"))
        res2=substract(x2,y2)
        print("Substract=",res2)
    elif op==3:
        x3=int(input("enter x"))
        y3=int(input("enter y"))
        res3=multiply(x3,y3)
        print("multiply=",res3)
    elif op==4:
        x4=int(input("enter x"))
        y4=int(input("enter y"))
        res4=divide(x4,y4)
        print("divide=",res4)
    elif op==5:
        x5=int(input("enter x"))
       
        res5=sqrt(x5)
        print("Sqrt=",res5)
    elif op==6:
        x6=int(input("enter x"))
       
        res6=exp(x6)
        print("exp=",res6)
    elif op==7:
        x7=int(input("enter x"))
       
        res7=sin(x7)
        print("Sin(x)=",res7)
    elif op==8:
        x8=int(input("enter x"))
        
        res8=cos(x8)
        print("cos(x)=",res8)
    elif op==9:
        x9=int(input("enter x"))
        
        res9=tan(x9)
        print("tan(x)=",res9)
    else:
        print("choose another operation")
    
    new=int(input("do you want to continue -(yes-1),(no-0)"))
    if new==1:
        op=int(input("enter operation"))
    elif new==0:
        print("thanks for using the scientific calculator ")
        break


  #next pattern type
       
       
n=int(input("enter any no. :"))
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
   
    for j in range(i,n):
        print('*',end=' ')
    print()
        
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
    

# next


print("welcome to my computer quize!")
playing=input("Do you want to play?")

if playing!="yes":
    quit()
print("okay! lets play:")
score=0

answer=input("what does cpu stand for? ")

if answer=="central processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect")

answer=input("whaowert does gpu stand for? ")
if answer=="graphics processing unit":
    print("correct!")
    score+=1
else:
    print("incorrect")

answer=input("what does RAM stands for? ")
if answer=="Random Access Memory":
    score+=1
    print("correct!")
else:
    print("incorrect")

answer=input("what does PSU stand for? ").lower()
if answer=="power supply":
    print("correct!")
    score+=1
else:
    print("incorrect")
print("you got" +str(score)+"questions correct!")
print("you got" +str((score/4)*100)+"%")



# next guessing no.


import random
top_or_range=input("type a number:  ")
if top_or_range.isdigit():
    top_or_range=int(top_or_range)
    if top_or_range<=0:
        print("please type a number large than 0 next time")
else:
    print("please type a number next time")
    quit()
random_number=random.randint(0,top_or_range)
guesses=0
while True:
    guesses+=1
    user_guess=input("make a guess:")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    
    else:
        print("please type a number next time")
        continue
    if user_guess==random_number:
        print("you got it!")
    else:
        print("you got it wrong!")
    print("you guess your no. in"+str(guesses)+"guess")



# next random no. guessing

import random as r
x=r.randrange(50)
while True:
    num=int(input("guess the no. which you want:"))
    if num>x:
        print("go for smaller no.")
    elif num<x:
        print("go for greater no.")
    else:
        print("you are right.")
        break



