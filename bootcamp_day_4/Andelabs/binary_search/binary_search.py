class BinarySearch(List):
    def __init__(self, a, b):
        self.a = a  # a is the length of the list to be created
        self.b = b  # b is the step or difference between consecutive values
        for value in range(1,a+1):  # upper limit is a(length of the list) + 1
            item = value * b
            self.append(item)  # append to self because the class inherits from the list class
        self.length = len(self)  #length is the number of elements in the list
