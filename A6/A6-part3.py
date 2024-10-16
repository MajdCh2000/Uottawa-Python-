# Course: IT1 1120
# Assignment number: 6
# Chantiri, Majd


def overlap(set1,list1):
    #set1={0,19,8,9,12,13,14,15}
    #list1=[0,19,2,4,5,9,10,11]
    '''(set, list)=>set
    returning the common values between both set and list'''

    set2=set()
    for i in set1:
        if i in list1:
            set2.add(i)
    return set2


def reverse(d):
    '''(dict)=>dict
    return a inversed form of the dictionary but with keeping the common values'''
    
    r_d = {}
    for i in d.values():
        r_d[i] = []#Names 
        for j in d.keys():#values
            if (d[j] == i):#if different values are found with common name in this iteration
                if (j not in r_d[i]):#if these new values are not in the new reversed list
                    r_d[i].append(j)#adding the values to the name with the form ({"name": values})
                                    #and since the key cannot be duplicated and should be unique no names will be found repeated.
    return r_d


def digit_sum(n):
    '''(int) -> int
    Returns the sum of all digits in a non-negative integer n.
    Precondition: n >= 0'''
    
    if n <= 9:
        return n
    else:
        unite = n % 10
        dizaine = n//10
        return unite + digit_sum(dizaine)


def digital_root(n):
    '''(int) -> int
    Returns the digital root of a number n
    Precondition: n >= 0'''
    
    if n <= 9:
        return n
    else:
        return digital_root(digit_sum(n))
