# Course: IT1 1120
# Assignment number: 5
# Chantiri, Majd
# Student number: 300217475

import random

#########################################################################
#helper functions
#########################################################################

def get_index(network, user):
    '''(2Dlist, int)->int
    returns the index of the user in the 2D-list friendship network.'''
    
    placement=-1
    for i in range(len(network)):
        if network[i][0]== user:
            placement=i
    return placement

def binary_search(lst, value):
    '''(2D list, int) -> int
    Returns index of the value if it is in the list and -1 otherwise.'''

    begining = 0
    end = len(lst)- 1

    while begining <= end:
        midpoint = (begining + end) // 2

        if (value < lst[midpoint][0]):
            end = midpoint - 1

        elif (value > lst[midpoint][0]):
            begining=midpoint+1

        else:
            return midpoint
               
    return -1

#########################################################################
# End of the helper functions
#########################################################################

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int
    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    
    # YOUR CODE GOES HERE
    
    del friends[0] #To avoid list out of range Error
    
    for i in range(len(friends)):
        Variable = friends[i].split(" ")
        friends[i] = [int(Variable[0]),int(Variable[1])]#int(Variable[0]) stands for current ID, and int(Variable[1]) stands for connection
        friends.append([int(Variable[1]), int(Variable[0])])
    if len(friends) >= 2:
        friends.sort()
        OldUser = friends[0][0] - 1
        count = -1

        #transforming the network to a sorted friends pair data.
        for i in range(len(friends)): 
            if (OldUser) == (friends[i][0]):
                network[count][1].append(friends[i][1])
            else:
                OldUser = friends[i][0]
                count = count + 1
                network.append((friends[i][0],[friends[i][1]]))#friends[i][0] stands for current user,
                                                               #and friends[i][1]stands for the connection.              
    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    
    LocationUser1=get_index(network, user1)#getting location of user 1
    LocationUser2=get_index(network,user2)#getting location of user 2

    friends1=network[LocationUser1][1]
    friends2=network[LocationUser2][1]
    
    for i in friends1:
        if i in friends2:#if the user is in the 1st friend and second friend => we found the Common friend
            common.append(i)
    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''
    # YOUR CODE GOES HERE

    placement=get_index(network, user)
    Max=-1
    recommendation=None

    if (placement == -1):
        return recommendation
    
    for i in network:
        if (i[0]!= user):

            if (user not in i[1]):
                common=getCommonFriends(user, i[0],network)#searching for common friends

                if (len(common)>Max and len(common)>0):#if common friends exists, then logicaly
                                                       #we can give recommondation
                    Max=len(common)
                    recommendation=i[0]
    
    return recommendation
    

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE

    count=0
    for i in network:
        if (len(i[1]) >= k):
            count=count+1
    return count
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE

    Max=0
    for i in network:
        if (len(i[1]) >= Max):
            Max=len(i[1])
    return Max

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE

    maximum=maximum_num_friends(network)
    for i in network:
        if (len(i[1]) == maximum):
            max_friends.append(i[0])
    return max_friends

def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    total = 0
    for i in network:
        total = total + len(i[1])
    average = total/len(network)
    return average

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    for i in network:
        if (len(i[1]) == len(network)-1):
            return True
    return False

####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    ID = -1

    while (ID == -1):
        
        try:
            UserId = int(input("Enter an integer for a user ID: ").strip())
            ID = binary_search(network, UserId)
            
            if (ID == -1):
                print("That user ID does not exist. Try again")
                
        except ValueError:
            print("That was not valid integer. Please try again.")
            
    return UserId

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")
