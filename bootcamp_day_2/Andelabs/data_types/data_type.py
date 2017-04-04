def data_type(value):
    if type(value) == type(None):
        return 'no value'
    elif type(value) == list:
        if len(value) >= 3:
            return value[2]
        else:
            return None
    elif type(value) == bool:
        return value
    elif type(value) == int:
        if value < 100:
            return 'less than 100'
        elif value > 100:
            return 'more than 100'
        else:
            return 'equal to 100'
    elif type(value) == str:
        return len(value)
    else:
        return value


print(data_type(None))
print(data_type([1, 2, 3]))
print(data_type([1, 2]))
print(data_type(True))
print(data_type(3))
print(data_type(200))
print(data_type('andela'))
