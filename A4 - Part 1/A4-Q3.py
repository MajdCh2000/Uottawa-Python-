# Course: IT1 1120
# Assignment number: 4
# Chantiri, Majd


def longest_run(li):
    '''(list)=>number
    that takes a list of numbers and returns the length of the longest run
    of consecutive numbers'''
    count=1
    max_count=0

    if (len(li) == 1):
        return 1
    
    for i in li[1:]:
        if (eval(i) == eval(li[0])):
            count = count + 1
        else:
            if (count > max_count):
                max_count = count
            li[0] = i
            count = 1

    return(max_count)


#main
list1=input("Please enter a list of numbers separated by spaces: ").strip().split()
print(longest_run(list1))    
