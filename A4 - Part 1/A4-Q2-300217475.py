# Course: IT1 1120
# Assignment number: 4
# Chantiri, Majd
# Student number: 300217475

def two_length_run(l):
    '''(List)->bool
    Returns true if l contains a run of at least length 2
    and false Otherwise
    '''
    for i in range(1,len(l)):
        if(l[i]==l[i-1]):
            return True
    return False

#main
s=input("Please enter a list of numbers separated by spaces: ").strip().split()
print(two_length_run(s))

