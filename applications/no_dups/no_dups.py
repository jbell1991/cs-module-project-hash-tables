def no_dups(s):
    lookup_table = {}
    # iterate over each word in the string
    for word in s.split():
        # if the word is not in the lookup_table 
        if word not in lookup_table:
            # assign the key to the value
            lookup_table[word] = word
    # set the string variable to the joined lookup_table values separated by spaces
    s = ' '.join(lookup_table.values())
    return s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
