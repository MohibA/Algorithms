from random import randint

# instead of having to type a list, just creat a function than can make a random list for you. For learninng purpose max size is set to 50
def create_random_list(size = 10, max = 50):
    return [randint(0, max) for _ in range(size)]




def bubble_sort(unsorted_list):
    #start by setting a variable to True to run our while loop
    swapped = True
    while swapped:
        # we want to iterate through the list and compare the adjacent values.
        for i in range(1, len(unsorted_list)):
            #check if the number before i is larger. If so we want to swap the numbers 
            if unsorted_list[i-1] > unsorted_list[i]:
                unsorted_list[i], unsorted_list[i-1] = unsorted_list[i-1],unsorted_list[i]
                #if we did swap the numbers, then swapped will continue to be true and we will run the while loop again
                swapped = True
            #else swapped is set to false and we can break out of the loop
            else:
                swapped = False
    return unsorted_list

# Example:

print("Bubble sort: \n")
bubble_list = create_random_list()
print("Unsorted ", bubble_list)
new_bubblesort = bubble_sort(bubble_list)
print("sorted: ", new_bubblesort
