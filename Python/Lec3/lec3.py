#lec3 with the man Sunday 20th August

#find the square root of a perfect square
#x= 16
#ans = 0
#while ans*ans<x:
#    ans = ans +1
#print ans

# better way to write the code uppove
#x=16
#ans = 0
#if x>=0:
#    while ans*ans <x:
#        ans = ans+1
#    if ans*ans != x:
#        print x, 'is not a perfect square'
#    else: print ans
#else: print x, 'is a negative number'

# Example on iteration
#x = 10
#i = 1
#while i<x:
#    if x%i == 0:
#        print 'divisor ', i
#    i = i+1
#=================================
#for loop
#x = 10
#for i in range(1,x):
#    if x%i == 0:
#        print 'divisor ', i
#=================================
# using Tuple to collect results
#x = 100
#divisors = ()
#for i in range(1,x):
#    if x%i == 0:
#        divisors = divisors + (i,)
#print(divisors)
#=================================

#Dealing with Strings(selection and sclicing)
#s1 = 'abcdefg'
#s2 = 'hihklmn'

#print s1 + s2
#print s1[3]
#print s1[1:6]
#===============
#Generalizing the idea of iteration
sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print sumDigits
