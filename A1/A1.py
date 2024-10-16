# Course: IT1 1120
# Assignment number: 1
# Chantiri, Majd



########################
#question 1
########################
def mh2kh (s):
    '''(number)->number
    takes the speed, s, expressed in miles/hour
    returns the same speed expressed in kilometres/hour'''
    
    kh = float(s * 1.60934)
    return kh



########################
#question 2
########################
def pythagorean_pair(a,b):
    '''(number,number)->bool
    takes two integers a and b as input and returns
    True if a and b are pythagorean pair and False otherwise '''
    
    return (bool(((a**2 + b**2)**(1/2))%1 == 0))



########################
#question 3
########################
def in_out(x,y,side):
    '''(number,number)->bool
    this function should print True if the given 
    query point (x,y,side) is inside of the given square,
    otherwise it should print False '''
    
    number1 = float (input("enter a number for the x coordinate of a query point:"))
    number2 = float (input("enter a number for the y coordinate of a query point:"))
    return (bool ((number1 <= x or number1 <=side)  and  (number2 <= side or number2 <= y)))



########################
#question 4
########################
def safe(n):
    '''(number,number)-> bool
    function that takes a non-negative integer n as input where n
    has at most 2 digits. The function determines if n is a safe number.
    A number is not safe if it contains a 9 as a digit, or if it can be
    divided by 9. The function should test if n is safe and
    return True if n is safe and False otherwise '''   

    return bool(n%9 != 0 and n // 10 != 9 and n % 10 != 9)



########################
#question 5
########################
def quote_maker(quote, name, year):
    '''(string,string,number)->none
    returns a sentence '''
    
    print('IN', year, 'a person called', name, 'said:', quote)

    

########################
#question 6
########################    
def quote_displayer():
    '''(none)->none
    prompts the user for a quote, name,
    and year. The function should then print a sentence using the same format as 
    specified in the previous question '''
    
    quote = input("Give me a quote: ")
    name = input("ho said that? ")
    year = input("What year did she/he say that? ")
    print('IN', year, 'a person called', name, 'said:', quote)



#######################
#question 7
#######################
def rps_winner():
    '''(none)->none
    prompts the user for choice of player 1 
    and then choice of player 2, and then it displays the result for player
    1 If both players make the same choice, we have a draw'''
    
    print('What choice did player 1 make?')
    input1 = input("Type one of the following options: rock, paper, scissors: ")
    print('What choice did player 2 make?')
    input2 = input("Type one of the following options: rock, paper, scissors: ")

    print('player 1 wins that is', (input1 =='scissors' > input2=='paper' or input1 =='paper' > input2=='scissors'
    or input1 =='rock' < input2=='paper'or input1 =='paper' < input2=='rock' or input1 =='rock' < input2=='scissors'))
    print('It is a tie that is ', input1 == input2)    
     


########################
#question 8
########################     
def fun(x):
    '''(number)->number
    takes as input a positive number x and solves
    the following equation for y and returns y. The equation is 10^4y=x+3 '''
    
    import math
    a= math.log(x+3)
    b= 4*(math.log(10))
    y = a/b
    return y



########################
#question 9
########################
def ascii_name_plaque(name):
   '''(string)->none
    that takes as input a string
    representing a person’s name and draws (using print function) a name plaque'''
   
   print('*************************************')
   print('*',"                                 ",'*')
   print('*',"_",name,"_",   "*")
   print('*',"                                 ",'*')
   print('*************************************')

   

########################
#question 10
########################   
def reverse(x):
    '''(number)->number
    takes a three-digit integer as input 
    and returns the integer obtained by reversing its digits '''
    
    r = x %10
    a = x//10
    y = a %10
    z = a//10
    return r*100 + y*10 + z



########################
#question 11
########################
#(2**x = n) => (x=log(n,2))
def alogical(n):
    '''(number)->number
    takes as input a number, n, where n is bigger or equal to 1, and 
    returns the minimum number of times that n needs to be
    divided by 2 in order to get a number equal or smaller than 1 '''

    import math 
    x = math.ceil(math.log(n,2))

    return x
        

    
########################
#question 12
########################
#To round to the nearest 5 cents => (precision=>"0.05")*[round(change/precision)]
def cad_cashier(p, c):
    '''(number,number)->number
    takes two real nonnegative numbers with two decimal places as input, where payment>=price and where
    the second decimal in payment is 0 or 5. They represent a price and payment in 
    Canadian dollars. The function should return a real number with 2 decimal places 
    representing the change the customer should get in Canadian dollars '''
    
    return round((round((c-p) / 0.05) * 0.05),10)



########################
#question 13
########################
def min_CAD_coins(p, c):
   '''(number,number)->(tuple)
    returns five numbers (t,l,q,d,n) that represent the smallest number of coins (toonies, loonies, quarters, 
   dimes, and nickels) that add up to the amount owed to the customer (here price and
   payment are defined as in the previous question). '''
   
   a = cad_cashier(p, c)
   t = int (a//2)
   l = round(a%2)
   
   s = round(a)
   j = a-s
   c = int(round((j*100),10))
   
   q = c//25
   
   e = c%25
   
   p = e//10
   
   g = e%10
   
   n = g//5

   return (t, l, q, p, n)



   
    








