import numpy as np

array = []

class Array_1D:
    def __init__(self, el):
        self.el = el
    
    def create1D(self):
        arr = []
        for i in self.el.split(" "):
            i = int(i)
            arr.append(i)
        
        
        a = np.array(arr)
        global array
        array = a
        return a

class Array_2D:
    def __init__(self, el, rows, columns):
        self.el = el
        self.rows = rows
        self.columns = columns
    
    def create2D(self):
        arr = []
        for i in self.el.split(" "):
            i = int(i)
            arr.append(i)
        
        array2d = np.array(arr).reshape(self.rows, self.columns)
        global array
        array = array2d
        return array2d

class Array_3D:
    def __init__(self, ele, depth, rows, columns):
        self.ele = ele
        self.depth = depth
        self.rows = rows
        self.columns = columns
    
    def create3D(self):
        arr = []
        for i in self.ele.split(" "):
            i = int(i)
            arr.append(i)
        
        array3d = np.array(arr).reshape(self.depth, self.rows, self.columns)
        global array
        array = array3d
        return array3d


def addition_Array():
    original_array = np.array(array)
    size = original_array.size
    shape = original_array.shape
    
    elements = input(f"\nEnter {size} elements for array seprated by space : ")
        
    aa = []
        
    for i in elements.split(" "):
        i = int(i)
        aa.append(i)
        
    second_array = np.array(aa).reshape(shape)
    
    print("\nAddition : \n", original_array + second_array)

def substraction_array():
    original_array = np.array(array)
    size = original_array.size
    shape = original_array.shape
    
    elements = input(f"\nEnter {size} elements for array seprated by space : ")
    
    aa = []
    
    for i in elements.split(" "):
        i = int(i)
        aa.append(i)
        
    second_array = np.array(aa).reshape(shape)
    
    print("\nSubstraction : \n", original_array - second_array)

def multiplication_array():
    original_array = np.array(array)
    size = original_array.size
    shape = original_array.shape
    
    elements = input(f"\nEnter {size} elements for array seprated by space : ")
    
    aa = []
    
    for i in elements.split(" "):
        i = int(i)
        aa.append(i)
        
    second_array = np.array(aa).reshape(shape)
    
    print("\nMultiplication : \n", original_array * second_array) 


def divison_array():
    original_array = np.array(array)
    size = original_array.size
    shape = original_array.shape
    
    elements = input(f"\nEnter {size} elements for array seprated by space : ")
    
    aa = []
    
    for i in elements.split(" "):
        i = int(i)
        aa.append(i)
        
    second_array = np.array(aa).reshape(shape)
    
    print("\nDivison : \n", original_array / second_array)   

def combine_array():
    original_array = np.array(array)
    size = original_array.size
    shape = original_array.shape
    
    elements = input(f"\nEnter {size} elements for array seprated by space : ")
    
    aa = []
    
    for i in elements.split(" "):
        i = int(i)
        aa.append(i)
    
    second_array = np.array(aa).reshape(shape)
    
    print("\nOriginal Array : \n", original_array)
    
    print("\nSecond Array : \n", second_array)
    
    result = np.vstack([original_array, second_array])
    
    print("\nCombine Array(V-stake) : \n", result)

def split_array():
    original_array = np.array(array)
    size = original_array.size
    
    split_part = int(input("Enter in how many part you want to split array : "))
    
    if size % split_part == 0:
        result = np.split(original_array, split_part)
        print(result)
    else:
        print(f"to split in {split_part} is not possible")

def search_array():
    original_array = np.array(array)
    
    search_value = int(input("\nEnter value you want to search : "))
    
    index = np.where(original_array == search_value)
    
    print(f"\nYour value is at{index}.")

def sort_ascending():
    original_array = np.array(array)
    
    print("\nOriginal Array : \n", original_array)
    
    print("\nSorted Array : \n", np.sort(original_array))

def sum_array():
    original_array = np.array(array)
    
    print("\nSum : ", np.sum(original_array))

def mean_array():
    original_array = np.array(array)
    
    print("\nMean : ", np.mean(original_array))

def median_array():
    original_array = np.array(array)
    
    print("\nMedian : ", np.median(original_array))

def maximum_array():
    original_array = np.array(array)
    
    print("\nMaximum : ", np.max(original_array))

def minimum_array():
    original_array = np.array(array)
    
    print("\nMinimum : ", np.min(original_array))




while True:
    print("\nWelcome to Array Analyzer\n")
    print("1. Create a numpy array")
    print("2. Perform Mathametical Operation")
    print("3. Combine or Spilit Array")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggreagtes and Statistics")
    print("6. Exit")

    choice = input("\nEnter your choice : ")

    if choice == 1:

        while True:

            print("\n1. Create 1D Array")
            print("2. Create 2D Array")
            print("3. Create 3D Array")
            print("4. Back to Main Menu")

            opition = input("\nEnter your choice : ")

            if opition == 1:
                elements = input("\nEnter elemetns for array seprated by space : ")
                        
                arr_1d = Array_1D(elements)
                print("Create by class : ",arr_1d.create1D())
                print(array)

            elif opition == 2:

                rows = int(input("\nEntre number of rows : "))
                columns = int(input("\n Entre number of columns : "))

                elements = input(f"\nEnter {rows * columns} elemetns for array sepreated by space : ")
                        
                arr_2d = Array_2D(elements, rows, columns)
                print("2D Array : \n", arr_2d.create2D())

            elif opition == 3:

                depth = int(input("\nEnter depth of array for 3D array : "))
                rows = int(input("\nEnter number of rows : "))
                columns = int(input("\nEnter number of columns : "))
                        
                elements = input(f"\nEnter {depth * rows * columns} elements for array seprated by space : ")
                        
                arr_3d = Array_3D(elements, depth, rows, columns)
                print("3D array : :\n", arr_3d.create3D())

            elif opition == 4:

                print("\n Array creation is done")
                break

            else:
                print("\nInvalid choice Please try again")

    elif choice == 2:

        while True:

            print("\n1. Addition")
            print("2. Substraction")
            print("3. Multiplication")
            print("4. Divison")
            print("5. Back to Main Menu")

            opition = int(input("\nEnter your choice : "))

            if opition == 1:

                addition_Array()

            elif opition == 2:

                substraction_array()

            elif opition == 3:

                multiplication_array()

            elif opition == 4:

                divison_array()

            elif opition == 5:

                print("\n Mathametical operation is done")
                break

            else:
                print("\nInvalid choice Please try again")

    elif choice == 3:

        while True:

            print("\n1. Combine Array")
            print("2. Split Array")
            print("3. Back to Main Menu")

            opition = input("\nEnter your choice : ")

            if opition == 1:

                combine_array()

            elif opition == 2:

                split_array()

            elif opition == 3:

                print("\n Combine or Split operation is done")
                break

            else:
                print("\n Invalid choice Please try again")

    elif choice == 4:

        while True:

            print("\n1. Search Array")
            print("2. Sort Array in Ascending Order")
            print("3. Back to Main Menu")

            opition = input("\nEnter your choice : ")

            if opition == 1:

                search_array()

            elif opition == 2:

                sort_ascending()

            elif opition == 3:

                print("\n Search or Sort operation is done")
                break

            else:
                print("\nInvalid choice Please try again")

    elif choice == 5:

        while True:

            print("\n1. Sum of Array")
            print("2. Mean of Array")
            print("3. Median of Array")
            print("4. Maximum of Array")
            print("5. Minimum of Array")
            print("6. Back to Main Menu")

            opition = input("\nEnter your choice : ")

            if opition == 1:

                sum_array()

            elif opition == 2:

                mean_array()

            elif opition == 3:

                median_array()

            elif opition == 4:

                maximum_array()

            elif opition == 5:

                minimum_array()

            elif opition == 6:

                print("\n Aggreagtes and Statistics operation is done")
                break

            else:

                print("\nInvalid choice Please try again")

    elif choice == 6:

        print("\nThank you for using Array Analyzer Goodbye!")
        break

    else:

        print("\nInvalid choice Please try again")
