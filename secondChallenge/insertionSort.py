# Sorting means arranging some unordered numbers in increasing order.
# Basic idea of Insertion Sort:
# You start with an unsorted list.
# With each step, you divide that list in two: the first part is sorted, the second one isn't yet sorted.
# Between these two parts is an element that will be put at the right place in the first part (sorted).
# You take this one element in the center, compare it to the ones before it and insert it at the right place between these already sorted elements.
# Basic algorithm looks like this:
# Go through each element (for i in range(1, len(toSort)):....) in the unsorted list, save it in a separate variable, then delete it from the list.
# Inside the for loop above, go through all the previous elements in the unsorted list (for j in range(i+1):), compare them to the currently saved element.
# If saved element smaller than element j: insert it before element j in the list.
# If no smaller elements found: insert saved element at the end.
# See: https://en.wikipedia.org/wiki/Insertion_sort

with open("sortInput.txt", 'r') as file:
    toSort = file.readlines() # Your list is saved in toSort
    #For python2, use this: toSort = map(int, toSort)
    toSort = list(map(int, toSort))
    print(toSort)
    for i in range(1, len(toSort)): ### INSERT YOUR CODE FROM HERE ###

    print(toSort)                   ### TO HERE                    ###

### DONT CHANGE THIS
with open("outInsertion.txt","w+") as output:
    output.write(str(toSort))