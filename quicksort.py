from random import randint

# instead of having to type a list, just creat a function than can make a random list for you. For learninng purpose max size is set to 50
def create_random_list(size = 10, max = 50):
    return [randint(0, max) for _ in range(size)]


#Quick sort uses the divide and conquer paradigm
def quick_sort(a):
    #check to see if list is ==  1 or is less than 1. In this case we don't have to do anything but return the list
    if len(a) <= 1:
        return a

    # create three empty lists to move values to. Smaller , eqaul and larger
    smaller,equal,larger = [],[],[]
    #choose a pivot number. You don't have to use a random number. 
    pivot = a[randint(0,len(a)-1)]

    #Iterate the list and append numbers smaller than pivot to smaller, if number is equal to the pivot append to equal
    # and if number is larger append to larger. Basically the idea is to continue breaking down the list using iteration and divide and conquer method.
    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    #return the list in sorted order
    return quick_sort(smaller) + equal + quick_sort(larger)


# Example:

print("quick sort: \n")
quicksort_list = create_random_list()
print("unsorted: ", quicksort_list)
new_quicksort = quick_sort(quicksort_list)
print("sorted: ", new_quicksort)


















