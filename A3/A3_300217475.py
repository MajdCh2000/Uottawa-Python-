# Course: IT1 1120
# Assignment number: 3
# Chantiri, Majd
# Student number: 300217475


############
#question 1
############
def sum_odd_divisors(n):
    '''(number)=>int
    precondition: n>0
    this function returns the sum of all the postive odd divisors of n.'''
    s = 0
    import math
    if(n==0):
        return None
    for i in range(1,abs(n)+1):
        if (i%2 != 0 and n%i == 0):
            s=s+i
    return s



############
#question 2
############
def series_sum():
    '''()=>int
    precondition: n>0
    prompts the user for an non-negative integer n. If the user enters a negative
    integer the function should return None otherwise the function should return the sum of a series '''
    n = int(input("Please enter a non negative integer: "))
     
    if n < 0:
        return None
    else:
        summ=1000
        for i in range(1,n+1):
            summ = summ + (1/(i**2))
        return summ



############
#question 3
############
def pell(n):
    '''(number)=>number
    precondition: n>0
    that takes one integer parameter n, of type int. If n is negative, pell returns None. Else,
    pell returns the nth Pell number'''
    import math
    if(n<0):
        return None
    elif (n == 0):
        pn=0

    elif (n == 1):
        pn=1

    elif (n>1):
        pn=round(((1 + math.sqrt(2))**n - (1 - math.sqrt(2))**n)/(2 * math.sqrt(2)))

    return pn



############
#question 4
############
def countMembers(s):
    '''(str)=>int
    that takes a single input parameter s, of type str. countMembers then returns
    the number of characters in s, that are extraordinary'''
    r=0
    for i in s:
        if(i == "e"or i=="f" or i=="g" or i=="F" or i=="G" or i=="H" or i=="I" or i=="J" or i=="K" or i=="L" or i=="M" or i=="N" or i=="O" or i=="P" or i=="Q"
            or i=="R" or i=="S" or i=="T" or i=="U" or i=="V" or i=="W" or i=="X" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="!" or i=="," or i=="\\"):
            r=r+1
    return r



############
#question 5
############        
def casual_number(s):
    '''(str)=>none
    that has one parameter, s, as
    input where s is a string. Function casual_number(s) should return an integer
    representing a number in s.'''
    for i in s:
        if(s=="-"):
            return None
        elif (i=="," or i.isalpha()):
            s=s.replace(i,"")
            
    a=s
    if(a == "-"):
        return None
    elif(a[0] == "-" and a[1] == "-"):
        return None
    else:
        print(a)



############
#question 6
############
def alienNumbers(s):
    '''(str)=> int
    takes one string parameter s, and returns the integer value represented by
    s. Since aliens only know these characters you may assume that no character in s outside of this set: {T,y, !,a, N, U}'''
    return s.count("T") * 1024 + s.count("y") * 598 + s.count("!") * 121 + s.count("a") * 42 +  s.count("N") * 6 + s.count("U")



############
#question 7
############
def alienNumbersAgain(s):
    '''(str)=> int
    takes one string parameter s, and returns the integer value represented by
    s. Since aliens only know these characters you may assume that no character in s outside of this set: {T,y, !,a, N, U}'''
    r1=0
    r2=0
    r3=0
    r4=0
    r5=0
    r6=0
    for i in s:
        if (i == "T"):
            r1=r1+1024
        elif(i == "y"):
            r2=r2+598
        elif(i == "!"):
            r3=r3+121
        elif(i == "a"):
            r4=r4+42
        elif(i == "N"):
            r5=r5+6
        elif(i == "U"):
            r6=r6+1
    return (r1+r2+r3+r4+r5+r6)
     


############
#question 8
############
def encrypt(s):
    '''(str)=>str
    function called encrypt, that has one parameter s where s is a string and
    it return an new encrypted version of s called: new_str'''
    r= s[::-1]
    new_str = ""
    length = len(r)

    for i in range(length // 2):
        new_str = new_str + r[i] +r[length - 1 - i]

    if(length%2 == 1):
        new_str = new_str + r[length // 2 ]
    return new_str



############
#question 9
############
def oPify(s):
    '''(str)=>str
    It returns a string with the letters o and p inserted between every pair of
    consecutive characters of s, as follows'''
    new= ''
    nwe=''
    if len(s)<=1:
        return s
    elif s.isdigit():
        return s
    
    for i in range(len(s)-1):
        
        if s[i].isupper() and s[i+1].isupper():
            new= new + s[i]+ "OP"
        elif s[i].isupper():
            new= new + s[i]+ "Op"
        elif s[i+1].isupper():
            new= new + s[i]+ "oP"
        else:
            new= new + s[i]+ "op"
       
   
    if (len(s)>=2):
        new=new+s[len(s)-1]

    

    return new


        
############
#question 10
############
def nonrepetitive(s):
    '''(str)=> bool
    The function returns True if s is nonrepetitive and False otherwise.'''
    for i in range(len(s)):
        for j in range(i,len(s)):
            s1 = s[i:j]
            s2 = s[j:2*j - i]
            if (s1 == s2 and s1 != ""):
                return False
            
    return True
            














