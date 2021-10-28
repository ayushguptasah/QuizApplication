import time

score = 0

name = str(input("Enter your name: "))
college = str(input("Enter your College name: "))
enroll = str(input("Enter your Enrollment No. : "))
print("================================= ONLINE QUIZ =================================")
print("Name: "+name)
print("College Name: "+college)
print("Enrollment No. "+enroll)
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("Date: ", d1)
print("========================== WELCOME TO MY ONLINE QUIZ ==========================")

def q1():
    global score
    print("\n1.In python, print type(type(int))")
    time.sleep(0.5)
    print("a) type 'type' ")
    print("b) Error")
    print("c) 0")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
        
    else:
        print("Sorry, that was the wrong answer!")

    q2()
    
def q2():
    global score
    time.sleep(0.5)
    print("\n2.Where is the Headquarter of MicroSoft office located")
    print("a) Washington")
    print("b) NewYork")
    print("c) California")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
        
    q3()
def q3():
    global score
    time.sleep(0.5)
    print("\n3.Which one of the following is an ‘Air-to-Air’ missile?")
    print("a) Astra")
    print("b) Akash")
    print("c) Prithvi")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
        
    q4()
def q4():
    global score
    time.sleep(0.5)
    print("\n4.Which Company First Developed the Java Programing?")
    print("a) Sun Microsystems")
    print("b) Google")
    print("c) IBM")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
        
    q5()
def q5():
    global score
    time.sleep(0.5)
    print("\n5.Who is popularly known as ‘Missile Man of India’?")
    print("a) Dr.C.V Raman")
    print("b) Dr.S. chandrasekhar")
    print("c) Dr.A.P.J. Abdul Kalam")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "c":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
        
    q6()
def q6():
    global score
    time.sleep(0.5)
    print("\n6. Which state became the first in India to launch a free email address in Hindi for residents? ")
    print("a) Uttar Pradesh")
    print("b) Rajasthan")
    print("c) Madhya Pradesh")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
        
    q7()
def q7():
    global score
    time.sleep(0.5)
    print("\n7.Which one is the first search engine in internet")
    print("a) archie")
    print("b) google")
    print("c) WAIS")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
        
    q8()
def q8():
    global score
    time.sleep(0.5)
    print("\n8. First Computer virus is known as")
    print("a) SCA virus")
    print("b) Creeper virus")
    print("c) Elk Cloner")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")
        
    q9()
def q9():
    global score
    time.sleep(0.5)
    print("\n9. What is Apple's latest device?")
    print("a) iPhone")
    print("b) MacBook Pro")
    print("c) iPod Touch")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")

    q10()

def q10():
    global score
    time.sleep(0.5)
    print("\n10.Network Interface Car(NIC) is generally used for")
    print("a) Connectivity")
    print("b) Programming")
    print("c) Printing")
    print("d) None of these\n")

    answer = str(input("What's the right answer: "))

    if answer == "a":
        print("well done, that's correct!")
        score+=1
    else:
        print("Sorry, that was the wrong answer!")

q1()
if(score>=7):
    print("Excellent!!!  "+name)
    print("Your scored: ",score)
elif(3<score<7):
    print("Good ! "+name)
    print("Your scored: ",score)
else:
    print("better luck next time ! "+name)
    print("Your scored: ",score)
