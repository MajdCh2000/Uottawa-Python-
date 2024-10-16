# Course: IT1 1120
# Assignment number: 2
# Chantiri, Majd
# Student number: 300217475


############
#question 1
############
def repeat(string, n, delim):
    '''(string,number,string)=> string
        returns a string repeated n times seperated by the string delim'''
    return n*(string+delim)


############
#question 2
############
def points(x1, y1, x2, y2):
    '''(number,number,number,number)=>none
        takes coordinates of 2 points and computes the slope of the
        line throught those points unless the line is vertical(prints infinity)
        and it computes the distance bettween those 2 points '''
    a = y2-y1
    b = x2-x1
    dist= str(( b**2 + a**2 )**0.5)
    if(x1 == x2):
        print("the slope is infinity and the distance is:", dist)
    else:
        slope=str(a/b)
        print("the slope is:",slope," and the distance is:", dist)

############
#question 3
############
def rps(c1,c2):
    '''(string,string)=>number
        precondition: ensert choices (R,P,S) in capitale letters
        determines the winner of a rock paper and scissors game'''
    if (c1==c2):
        return 0
    elif ((c1 == 'R' and c2 == 'P') or (c1 == 'S' and c2 == 'R') or (c1 == 'P' and c2 == 'S')):
        return 1
    else:
        return -1

############
#question 4
############
def leap(y):
    '''(number)=>bool
        returns true if the year is leap and false otherwise'''
    if (( y%400 == 0)or (( y%4 == 0 ) and ( y%100 != 0))):
        return True
    else:
        return False

############
#question 5
############
#we use the || just to return a positive value and (m1-m2)*31 because in some cases
#we are not in the same month and we add them to (d1-d2) to obtain the exact
#numbers of days apart   
def month_apart(m1, d1, m2, d2):
    '''(number,number,number,number)=>bool
        preconditions: Dates should be inserted as month (1 to 12)
        and days(1 to 31) 
        this function returns true if their is at least
        a month apart between the 2 dates and false otherwise'''
    import math
    result= abs((31*(m1-m2)) + (d1-d2)) 
    if(result>=31):
        return True
    else:
        return False
    

############
#question 6
############
def allTheSame(x,y,z):
    '''(any type)=>bool
        returns true if the arguments are all the same and false otherwise
        Precondition: all 3 arguments shoulb be
        from the same data type to compare'''
    return bool(x == y and x == z and y == z)

def allDifferent(x,y,z):
    '''(any type)=>bool
        returns true if the arguments are all different and false otherwise
        Precondition: all 3 arguments shoulb
        be from the same data type to compare'''
    return bool(x != y and x != z and y != z)

def sorted(x,y,z):
    '''(any type)=>bool
        returns true if the arguments are sorted with the smallest comming
        first and false otherwise
        Precondition: all 3 arguments shoulb
        be from the same data type to compare'''
    return bool (x<y and x<z and y<z)


############
#question 7
############
def letter2number(grade):
    '''(string)=>number
        preconditions: Please enter the grade (A to D and F) in capital letter
        converts lettered grade to numeric grade'''
    if (grade== 'A+'):
        n= 4+0.3
    elif(grade== 'A'):
        n=4
    elif (grade== 'A-'):
        n= 4-0.3
    elif (grade== 'B+'):
        n= 3+0.3
    elif (grade== 'B'):
        n= 3
    elif (grade== 'B-'):
        n= 3-0.3
    elif (grade== 'C+'):
        n= 2+0.3
    elif (grade== 'C'):
        n= 2
    elif (grade== 'C-'):
        n= 2-0.3
    elif (grade== 'D+'):
        n= 1+0.3
    elif (grade== 'D'):
        n= 1
    elif (grade== 'D-'):
        n= 1-0.3
    elif (grade== 'F+'):
        n= 0+0.3
    elif (grade== 'F'):
        n= 0    
    return n



############
#question 8
############
def is_nneg_f(string):
    '''(string)=>bool
        returns false if the number is negative or written in scientific form
        and true otherwise'''
    a=string
    if (a.find("-") == 0 or a.find("e") >= 0):
        return False
    
    elif(a.find(".")>=0 or a.isdigit()):
        return True




############
#question 9
############
def min_enclosing_rectangle(r,x,y):
    '''(number,number,number)=>(number,number)
        precondition: if r<0 (number,number,number)=>(None)
        computing the coordinates of the bottom left of a rectangle
        inclosing a circle'''
    if (r<0):
        return None
    elif (r>=0):
        xr0= x-r
        yr0= y-r
    return (xr0,yr0)




############
#question 10
############
def l2lo(w):
    '''(number)=>(tuple)
        precondition: w>0
        converts weight given in lbs as lbs and oz'''
    a= w*16
    l= int(a//16)

    m=w-l
    o= float(m*16)

    return (l,o)




############
#question 11
############
def vote_percentage(vote):
    '''(string)=>float
        count the number of substrings yes and its % result along with counting
        the number of substrings no'''
    a=vote.count("yes")
    b=vote.count("no")
    c=vote.count("abstained")
    result= ((a*100)/((a+b+c)-c))/100
    
    return result




############
#question 12
############
def vote():
    '''()=>none
        count the number of substrings yes no and abstained
        compute the results and tells if the proposal passes unanimously
        or with supper majority or with simple majority or
        if the poposal fails'''
    input1=input("Enter the yes no abstained votes one by one and the press enter: ")
    
    b=input1.count("no")
    
    d=vote_percentage(input1)
    if(b==0):
        print("Proposal passes unanimously")
    elif(d >= (((2/3)*100)/100)):
        print("Proposal passes with supper majority")
    elif(d > (((1/2)*100)/100) and d < (((2/3)*100)/100)):
        print("Proposal passes with simple majority")
    else:
        print("Proposal FAILS")




############
#question 13
############
def count_even_digits(n,l):
    '''(number,number)=> number
        precondition: values passed to the finction are not negative
        accepts 2 integers in the parameter. n is the number and l is the lengh
        of n.
        this function returns the number of even digits in n '''
    count = 0
    for i in range(0,l):
        digit = n % 10
        n = n // 10
        if (digit % 2 == 0):
            count = count + 1
 
    return count
        
    

        
        
    
        
