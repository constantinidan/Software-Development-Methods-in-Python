#encoding: utf8
#TDLOG TP 1


############# Task 1 #############	

def integer_to_string(number):
    L = []	                 	# Empty list
    string = ""             	# Empty string
    dictionnairy = {0:"0",1:"1",2:"2",3:"3",4:"4",
                    5:"5",6:"6",7:"7",8:"8",9:"9"
                    }
    while number:
        digit = number % 10		# Rest of the euclidean devision
        L.insert(0, digit)		# Add up the digits in the list
        number = int(number/10)

    for j in range(len(L)):
        string = string + dictionnairy[L[j]]
    return string




def float_to_string(number):
    string = ""
    rest = number%int(number)
    i = 0
    while int(rest) != rest :
        rest *= 10
        i += 1
    integer_after_dot = int(rest)
    string2 = integer_to_string(integer_after_dot)
    string = integer_to_string(int(number)) + "." + string2
    return string
    
    
def number_to_string(number):
    if number == int(number):
        return integer_to_string(number)
    else: 
        return float_to_string(number)


# The above code works well with integers but lacks efficiency for floats.




############# Task 2 ##############

"""
Piksrt function :
The first line of comments tells that the function sorts arrays in an ascending
order.
From the analysis of the code : the elements are sorted step by step. Taking a 
rank j, and classifying the j-th element through the ordered (j-1) list. 
From some testing : Works for lists and arrays. 
From the Internet : https://en.wikipedia.org/wiki/Insertion_sort. The sort is 
called insertion sort.

Shell function : 
The first comment line: Sorts an array using Shell's method.
From internet sources: sorts far away elements and exchanges them. 
https://en.wikipedia.org/wiki/Shellsort
Testing the function : the code does not work because of the wrong indentation.
"""


 ############# Task 3 #############

 
def piksrt(arr):
    # Sorts an array arr into ascending numerical order, by straight insertion.
    n = len(arr)
    for j in range(1, n): # Pick out each element in turn.
        a = arr[j]
        i = j - 1
        while (i >= 0 and arr[i] > a): # Look for the place to insert it.
            arr[i+1] = arr[i]
            i -= 1
            arr[i+1] = a               # Insert it.
    return arr



                                                                               
def shell(a):
    # Sorts an array a[] into ascending numerical order by 
    # Shell’s method (diminishing increment sort). 
    n = len(a)
    inc = 1 # Determine the starting increment.
    while True:
        inc *= 3
        inc += 1
        if inc > n:  break
    while True: # Loop over the partial sorts.
        inc = inc // 3
        for i in range(inc, n-1): # Outer loop of straight insertion.
            v = a[i]
            j = i
            while a[j-inc] > v: # Inner loop of straight insertion.
                a[j] = a[j-inc]
                j -= inc
                if j < inc:
                    break
                a[j] = v
        if inc <= 1:
            break
    return a
# With the right indentation, the shell function works.

    

""" Adopter des conventions de formatage permet de vérifier un code plus 
rapidement et de le soumettre facilement à une autre équipe.""" 


 ############# Task 4 #############

# This function sorts the j-element of the array through the subarray (first 
# element to the (j-1) element)
def sort_element_through_subarray(j, array):
    element_to_sort = array[j]
    while (j >= 1 and array[j-1] > element_to_sort): 
        array[j] = array[j-1]           
        array[j-1] = element_to_sort    # Exchange of the two elements (j and 
        j -= 1                          # j-1).
        

def sort_by_picking_elements_step_by_step(array):
    # Sorts an array arr into ascending numerical order, by straight insertion.
    n = len(array)
    for j in range(1, n):
        sort_element_through_subarray(j, array)
    return array



