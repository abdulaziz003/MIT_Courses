#sample code for use in Lecture 2, Fall 2016 created by Abdulaziz
# this is a special version of Atom editor

#==================================
# we use the method raw_input to return String
#print(txt*5)
# we use the method input to return num
#num = int(input("Type a number : "))
#print(5*num)

#example on repeating
#once = "umbr"
#repeat = "ella"
#u = once + (repeat+" ")*4
#print(u)
#===================================
#f more complicated with while loop
#n = 0
#while n<5:
#    print(n)
#    n = n+1

#shortcut with for loop
#for n in range(5):
#    print(n)

#example on while loop
#n= raw_input("You are in the Lost Forest. Go left or right?")
#while n=="right":
#    n=raw_input("Your are in the Lost Forest. Go left or right?")
#print("You got out of the Lost Forest!")

# example on compareson
#pset_time = 15
#sleep_time = 8
#print(sleep_time>pset_time)
#derive = True
#drink = False
#both = drink and derive
#print(both)

#====================================

# for loop by customizing range

#mysum = 0
#for i in range(7, 10):
#    mysum+=i
#print("Mysum :"+ str(mysum))

#another example using all arguments in range method

#for i in range(5, 11, 2):
#    mysum+=i
#print(mysum)

#example on branching
#x = float(input("Enter a number for x : "))
#y = float(input("Enter a number for y : "))
#if x==y:
#    if y!=0:
#        print("x / y is ", x/y)
#elif x<y:
#    print("x is smaller")
#else:
#    print(" y is smaller")
#=====================================

#using break statement

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum+=1
print(mysum)
