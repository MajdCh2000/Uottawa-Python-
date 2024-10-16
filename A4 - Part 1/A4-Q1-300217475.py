# Course: IT1 1120
# Assignment number: 4
# Chantiri, Majd
# Student number: 300217475

def number_divisible(l,n):
    '''(list, number)=>number
    returns the number of elements is l that are divisible by n'''
    s = 0
    
    for i in range (0,len(l)):
        if (int(l[i])%n == 0):
            s=s+1
    return s

#main
list1=input("Please enter a list of numbers separated by spaces: ").strip().split()
input1=int(input("Please input an integer: "))
print("the number of elements divisible by ",input1," is ",number_divisible(list1,input1))
    
