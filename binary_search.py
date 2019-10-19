from random import randint

# function to create a random list
def create_list(size = 10, max = 50):
    return[randint(0,max) for _ in range(size)]



def binary_search(data,target):
    #two variables we need one for starting point which is low and set to the zero index
    #and high which is set to the len -1 for list index
    low = 0
    high = len(data) - 1


    while low <= high:
        #middle term is needed as we use divide and conquer method. Also we need to use '//' for division because we need a integer and not decimal 
        middle_term = (low + high) // 2
        if target == data[middle_term]:
            #if target is the middle term simply return it
            return middle_term
        elif target < data[middle_term]:
            # if target is less than the middle term. we set a new high which will be the previous middle term - 1.
            high = middle_term - 1
        elif target > data[middle_term]:
            #if target is > than middle term the new low will = the previous middle term + 1
            low = middle_term + 1
    return False


data = create_list()
print(binary_search(data,3))
