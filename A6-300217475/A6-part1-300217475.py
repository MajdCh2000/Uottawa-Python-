# Course: IT1 1120
# Assignment number: 6
# Chantiri, Majd
# Student number: 300217475

def largest_34(a):
    '''{this function does about 140 000 operations}
    (list,int) => int
    function takes a list of ints as input return the sum of the 3rd and 4th
    largest value in the list'''

    a.sort()
    length = len(a)
    s=(a[length-3]) + (a[length-4])

    return s


def largest_third(a):
    '''{this function does about 140 000 operations}
    (list,int) => int
    function takes a list of ints as input and returns the sum of the len(a)
    //3 largest numbers in the list'''
    
    a.sort()
    s = 0

    for i in range(len(a) // 3):
        i = i + 1
        s = s + a[len(a)-i]

    return s


def third_at_least(a):
    '''{this function does about ln(a) operations}
    (list,int) => int
    function takes a list of ints and returns a value in a which occurs len(a)//3 +1 times'''

    for i in range(len(a)):
        count = a.count(a[i])
        if (count == (len(a)//3 + 1)):
            return a[i]

    return None


def sum_tri(a,x):
    '''{this function does about (10.000)^3 operations}
    (list,int) => bool
    Returns true if any three numbers in the list
    have a sum which equals x and Flase otherwise.'''

    for i in range(len(a)):
        num1 = a[i]
        for j in range(len(a)):
            num2 = a[j]
            for k in range(len(a)):
                num3 = a[k]
                if (num1 + num2 + num3 == x):
                    return True

    return False
