def word_count(s):
    counts = {}
    # convert string to lowercase
    s = s.lower()
    # get rid of punctuation
    punctuations = '''":;,.-+=/\\|[]{}()*^&'''
    for char in s:
        if char in punctuations:
            s = s.replace(char, '')
    # iterate through each word in the sentence using split
    for word in s.split():
        # if it's the first time seeing the key
        if word not in counts:
            # set the value to 1
            counts[word] = 1
        # if it's a duplicate key
        else:
            # add 1 to the value 
            counts[word] += 1
            
    # return dictionary with each word as the key and count of each word as the value
    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
