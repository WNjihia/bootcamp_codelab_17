class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a  # a is the length of the list to be created
        self.b = b  # b is the step or difference between consecutive values
        for value in range(1,a+1):  # upper limit is a(length of the list) + 1
            item = value * b
            self.append(item)  # append to self because the class inherits from the list class
        self.length = len(self)  #length is the number of elements in the list

    def search(self, input_value): #input value is the value being searched for
        first_index = 0
        last_index = len(self) - 1
        found = False
        count = 0
        index = 0

        if input_value not in self:
            found = True
            index = -1

        if self[first_index] == input_value:
            found = True
            index = first_index

        if self[last_index] == input_value:
            found = True
            index = last_index

        while first_index <= last_index and not found:
            middle_point = (first_index + last_index)//2
            if self[middle_point] == input_value:
                found = True
                count = 1
                index = middle_point
            else:
                count += 1
                if input_value < self[middle_point]:
                    last_index = middle_point - 1
                else:
                    first_index = middle_point + 1
        return {'count': count, 'index': index}
