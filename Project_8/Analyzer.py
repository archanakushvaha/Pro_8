import numpy as np


class DataAnalytics:

    def __init__(self):
        self.__array = None

    def __check_array(self):
        if self.__array is None:
            print("\nPlease create an array first.")
            return False
        return True

    def create_analyzer(cls):
        return cls()

    def display_title(title):
        print("\n" + "=" * 40)
        print(title)
        print("=" * 40)

    def create_1d(self, elements):

        arr = []

        for i in elements.split():
            arr.append(int(i))

        self.__array = np.array(arr)

        print("\n1D Array:")
        print(self.__array)

    def create_2d(self, elements, rows, columns):

        arr = []

        for i in elements.split():
            arr.append(int(i))

        if len(arr) != rows * columns:
            print("\nInvalid number of elements.")
            return

        self.__array = np.array(arr).reshape(rows, columns)

        print("\n2D Array:")
        print(self.__array)

    def create_3d(self, elements, depth, rows, columns):

        arr = []

        for i in elements.split():
            arr.append(int(i))

        if len(arr) != depth * rows * columns:
            print("\nInvalid number of elements.")
            return

        self.__array = np.array(arr).reshape(depth, rows, columns)

        print("\n3D Array:")
        print(self.__array)

    def indexing(self):

        if not self.__check_array():
            return

        print("\nCurrent Array:")
        print(self.__array)

        try:
            index = int(input("\nEnter index: "))

            print("\nElement:")
            print(self.__array[index])

        except:
            print("\nInvalid index.")

    def slicing(self):

        if not self.__check_array():
            return

        print("\nCurrent Array:")
        print(self.__array)

        try:
            start = int(input("\nEnter start index: "))
            end = int(input("Enter end index: "))

            print("\nSliced Array:")
            print(self.__array[start:end])

        except:
            print("\nInvalid index.")

    def get_second_array(self):

        if not self.__check_array():
            return None

        size = self.__array.size
        shape = self.__array.shape

        elements = input(f"\nEnter {size} elements separated by space: ")

        arr = []

        for i in elements.split():
            arr.append(int(i))

        if len(arr) != size:
            print("\nInvalid number of elements.")
            return None

        return np.array(arr).reshape(shape)


    def addition_array(self):

        second_array = self.get_second_array()

        if second_array is not None:

            print("\nAddition:")
            print(self.__array + second_array)


    def subtraction_array(self):

        second_array = self.get_second_array()

        if second_array is not None:

            print("\nSubtraction:")
            print(self.__array - second_array)


    def multiplication_array(self):

        second_array = self.get_second_array()

        if second_array is not None:

            print("\nMultiplication:")
            print(self.__array * second_array)


    def division_array(self):

        second_array = self.get_second_array()

        if second_array is not None:

            if np.any(second_array == 0):
                print("\nDivision by zero is not allowed.")
                return

            print("\nDivision:")
            print(self.__array / second_array)

    def combine_array(self):

        if not self.__check_array():
            return

        second_array = self.get_second_array()

        if second_array is None:
            return

        try:

            result = np.concatenate((self.__array, second_array),axis=0)

            print("\nOriginal Array:")
            print(self.__array)

            print("\nSecond Array:")
            print(second_array)

            print("\nCombined Array:")
            print(result)

        except ValueError:

            print("\nArrays cannot be combined.")

    def split_array(self):

        if not self.__check_array():
            return

        try:

            parts = int(input("\nEnter number of parts: "))

            if parts <= 0:
                print("\nInvalid number of parts.")
                return

            result = np.array_split(self.__array,parts)

            print("\nSplit Arrays:")

            for i, part in enumerate(result, 1):

                print(f"\nPart {i}:")
                print(part)

        except:

            print("\nArray cannot be split.")


    def search_array(self):

        if not self.__check_array():
            return

        try:

            value = int(input("\nEnter value to search: "))

            index = np.where(self.__array == value)

            if len(index[0]) == 0:

                print("\nValue not found.")

            else:

                print("\nValue found at:")
                print(index)

        except:

            print("\nInvalid value.")


    def sort_ascending(self):

        if not self.__check_array():
            return

        result = np.sort(self.__array,axis=None)

        print("\nAscending Order:")
        print(result)


    def sort_descending(self):

        if not self.__check_array():
            return

        result = np.sort(self.__array,axis=None)[::-1]

        print("\nDescending Order:")
        print(result)


    def filter_array(self):

        if not self.__check_array():
            return

        try:

            value = int(input("\nEnter value: "))

            print("\n1. Greater than")
            print("2. Less than")
            print("3. Equal to")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:

                result = self.__array[self.__array > value]

            elif choice == 2:

                result = self.__array[self.__array < value]

            elif choice == 3:

                result = self.__array[self.__array == value]

            else:

                print("\nInvalid choice.")
                return

            print("\nFiltered Array:")
            print(result)

        except:

            print("\nInvalid input.")


    def sum_array(self):

        if self.__check_array():

            print("\nSum:",np.sum(self.__array))


    def mean_array(self):

        if self.__check_array():

            print("\nMean:",np.mean(self.__array))


    def median_array(self):

        if self.__check_array():

            print("\nMedian:",np.median(self.__array))


    def maximum_array(self):

        if self.__check_array():

            print("\nMaximum:",np.max(self.__array))


    def minimum_array(self):

        if self.__check_array():

            print("\nMinimum:",np.min(self.__array))


    def standard_deviation(self):

        if self.__check_array():

            print("\nStandard Deviation:",np.std(self.__array))


    def variance(self):

        if self.__check_array():

            print("\nVariance:",np.var(self.__array))


    def percentile(self):

        if not self.__check_array():
            return

        try:

            value = float(input("\nEnter percentile (0-100): "))

            if value < 0 or value > 100:

                print("\nPercentile must be between 0 and 100.")
                return

            result = np.percentile(self.__array,value)

            print(f"\n{value}th Percentile:",result)

        except:

            print("\nInvalid percentile.")


    def correlation(self):

        if not self.__check_array():
            return

        if self.__array.ndim != 1:

            print("\nCorrelation requires a 1D array.")

            return

        try:

            elements = input("\nEnter elements for second array: ")

            arr = []

            for i in elements.split():
                arr.append(int(i))

            second_array = np.array(arr)

            if len(self.__array) != len(second_array):

                print("\nBoth arrays must have same size.")

                return

            result = np.corrcoef(self.__array,second_array)[0, 1]

            print("\nCorrelation Coefficient:",result)

        except:

            print("\nInvalid input.")

    def dot_product(self):

        if not self.__check_array():
            return

        if self.__array.ndim != 1:

            print("\nDot product requires a 1D array.")

            return

        try:

            elements = input("\nEnter elements for second 1D array: ")

            arr = []

            for i in elements.split():
                arr.append(int(i))

            second_array = np.array(arr)

            if len(self.__array) != len(second_array):

                print("\nBoth arrays must have same size.")

                return

            result = np.dot(self.__array,second_array)

            print("\nDot Product:",result)

        except:

            print("\nInvalid input.")

    def matrix_multiplication(self):

        if not self.__check_array():
            return

        if self.__array.ndim != 2:

            print("\nMatrix multiplication requires a 2D array.")

            return

        try:

            rows = int(input("\nEnter rows of second matrix: "))

            columns = int(input("Enter columns of second matrix: "))

            if self.__array.shape[1] != rows:

                print("\nMatrix multiplication is not possible.")

                print("Columns of first matrix must equal rows of second matrix.")

                return

            elements = input(f"\nEnter {rows * columns} elements: ")

            arr = []

            for i in elements.split():
                arr.append(int(i))

            if len(arr) != rows * columns:

                print("\nInvalid number of elements.")

                return

            second_array = np.array(arr).reshape(rows, columns)

            result = np.matmul(self.__array,second_array)

            print("\nSecond Matrix:")
            print(second_array)

            print("\nMatrix Multiplication:")
            print(result)

        except:

            print("\nInvalid input.")

    def show_array(self):

        if self.__check_array():

            print("\nCurrent Array:")
            print(self.__array)

# MAIN PROGRAM

analyzer = DataAnalytics.create_analyzer()


while True:

    print("\n")
    print("       WELCOME TO ARRAY ANALYZER")
  
    print("1. Create a NumPy Array")
    print("2. Mathematical Operations")
    print("3. Indexing and Slicing")
    print("4. Combine or Split Array")
    print("5. Search, Sort and Filter")
    print("6. Aggregates and Statistics")
    print("7. Dot Product / Matrix Multiplication")
    print("8. Show Current Array")
    print("9. Exit")

    try:

        choice = int(input("\nEnter your choice: "))

    except:

        print("\nPlease enter a number.")
        continue

    if choice == 1:

        while True:

            print("\n1. Create 1D Array")
            print("2. Create 2D Array")
            print("3. Create 3D Array")
            print("4. Back to Main Menu")

            try:

                option = int(input("\nEnter your choice: "))

            except:

                print("\nPlease enter a number.")
                continue

            if option == 1:

                elements = input("\nEnter elements separated by space: ")

                try:

                    analyzer.create_1d(elements)

                except:

                    print("\nPlease enter numbers only.")

            elif option == 2:

                try:

                    rows = int(input("\nEnter number of rows: "))

                    columns = int(input("Enter number of columns: "))

                    elements = input(f"\nEnter {rows * columns} elements: ")

                    analyzer.create_2d(elements,rows,columns)

                except:

                    print("\nInvalid input.")

            elif option == 3:

                try:

                    depth = int(input("\nEnter depth: "))

                    rows = int(input("Enter rows: "))

                    columns = int(input("Enter columns: "))

                    elements = input(f"\nEnter {depth * rows * columns} elements: ")

                    analyzer.create_3d(elements,depth,rows,columns)

                except:

                    print("\nInvalid input.")

            elif option == 4:

                break

            else:

                print("\nInvalid choice.")

    elif choice == 2:

        while True:

            print("\n1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Back")

            try:

                option = int(input("\nEnter your choice: "))

            except:

                print("\nPlease enter a number.")
                continue

            if option == 1:

                analyzer.addition_array()

            elif option == 2:

                analyzer.subtraction_array()

            elif option == 3:

                analyzer.multiplication_array()

            elif option == 4:

                analyzer.division_array()

            elif option == 5:

                break

            else:

                print("\nInvalid choice.")


    elif choice == 3:

        while True:

            print("\n1. Indexing")
            print("2. Slicing")
            print("3. Back")

            try:

                option = int(input("\nEnter your choice: "))

            except:

                print("\nPlease enter a number.")
                continue

            if option == 1:

                analyzer.indexing()

            elif option == 2:

                analyzer.slicing()

            elif option == 3:

                break

            else:

                print("\nInvalid choice.")

    elif choice == 4:

        while True:

            print("\n1. Combine Array")
            print("2. Split Array")
            print("3. Back")

            try:

                option = int(input("\nEnter your choice: "))

            except:

                print("\nPlease enter a number.")
                continue

            if option == 1:

                analyzer.combine_array()

            elif option == 2:

                analyzer.split_array()

            elif option == 3:

                break

            else:

                print("\nInvalid choice.")

    elif choice == 5:

        while True:

            print("\n1. Search Array")
            print("2. Ascending Sort")
            print("3. Descending Sort")
            print("4. Filter Array")
            print("5. Back")

            try:

                option = int(input("\nEnter your choice: "))

            except:

                print("\nPlease enter a number.")
                continue

            if option == 1:

                analyzer.search_array()

            elif option == 2:

                analyzer.sort_ascending()

            elif option == 3:

                analyzer.sort_descending()

            elif option == 4:

                analyzer.filter_array()

            elif option == 5:

                break

            else:

                print("\nInvalid choice.")

    elif choice == 6:

        while True:

            print("\n1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Maximum")
            print("5. Minimum")
            print("6. Standard Deviation")
            print("7. Variance")
            print("8. Percentile")
            print("9. Correlation")
            print("10. Back")

            try:

                option = int(input("\nEnter your choice: "))

            except:

                print("\nPlease enter a number.")
                continue

            if option == 1:

                analyzer.sum_array()

            elif option == 2:

                analyzer.mean_array()

            elif option == 3:

                analyzer.median_array()

            elif option == 4:

                analyzer.maximum_array()

            elif option == 5:

                analyzer.minimum_array()

            elif option == 6:

                analyzer.standard_deviation()

            elif option == 7:

                analyzer.variance()

            elif option == 8:

                analyzer.percentile()

            elif option == 9:

                analyzer.correlation()

            elif option == 10:

                break

            else:

                print("\nInvalid choice.")

    elif choice == 7:

        while True:

            print("\n1. Dot Product")
            print("2. Matrix Multiplication")
            print("3. Back")

            try:

                option = int(input("\nEnter your choice: "))

            except:

                print("\nPlease enter a number.")
                continue

            if option == 1:

                analyzer.dot_product()

            elif option == 2:

                analyzer.matrix_multiplication()

            elif option == 3:

                break

            else:

                print("\nInvalid choice.")

    elif choice == 8:

        analyzer.show_array()

    elif choice == 9:

        print("\nThank you for using Array Analyzer!")
        print("Goodbye!")

        break

    else:

        print("\nInvalid choice. Please try again.")
