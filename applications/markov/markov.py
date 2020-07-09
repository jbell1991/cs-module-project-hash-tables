import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()


sentence = '''Cats "and" "dogs" "and" "birds" "and" "fish" dogs birds.'''
lookup_table = {}
# TODO: analyze which words can follow other words
def analyze_text(words):
    words = words.split()
    for i in range(len(words) - 1):
        word = words[i]
        if word not in lookup_table:
            lookup_table[word] = [words[i + 1]]
        else:
            lookup_table[word].append(words[i + 1])
    return lookup_table

def construct_text(lookup_table):
    # start_words are random keys that are capitalized 
    start_words = [key for key in lookup_table.keys() if key[0].isupper() or (key[0] == '"' and key[1].isupper())]
    rand_start_word = random.choice(start_words)
    print(rand_start_word, end=" ")
    punctuation = '''.?!"'''
    stop_words = []
    middle_words = []
    for arr in lookup_table.values():
        for value in arr:
            if value[-1] in punctuation:
                stop_words.append(value)
            elif value[0] != '"':
                middle_words.append(value)
    for i in range(random.randint(0, 50)):
        print(random.choice(middle_words), end=" ")
    rand_stop_word = random.choice(stop_words)
    print(rand_stop_word)


analyze_text(words)


# TODO: construct 5 random sentences
print("Sentence 1")
construct_text(lookup_table)
print("Sentence 2")
construct_text(lookup_table)
print("Sentence 3")
construct_text(lookup_table)
print("Sentence 4")
construct_text(lookup_table)
print("Sentence 5")
construct_text(lookup_table)

