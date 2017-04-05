def words(value):
    """

    Function that counts the occurrence of a word in a string

    """
    words_dict = {}
    split_word = value.split()
    for word in split_word:
        if word.isdigit():
            if word not in words_dict:
                words_dict[int(word)] = 1
            else:
                words_dict[int(word)] +=1
        else:
            if word not in words_dict:
                words_dict[word] = 1
            else:
                words_dict[word] += 1
    return words_dict


print(words("olly olly come in here"))
print(words('testing 1 2 testing'))
string = "I have 1 2 things"
