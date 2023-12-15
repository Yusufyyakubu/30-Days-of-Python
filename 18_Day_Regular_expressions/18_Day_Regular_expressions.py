
# EXERCISE 1 
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Convert the paragraph to lowercase and split it into words
words = paragraph.lower().split()

# Count the frequency of each word
word_counts = Counter(words)

# Find the most frequent word
most_frequent_word = word_counts.most_common(1)[0][0]

# Display the result
print("The most frequent word is:", most_frequent_word)

#Exercises: Level 2
import re

def is_valid_variable(variable):
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    return bool(pattern.match(variable))

# Test cases
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname'))   # True


#Exercises: Level 3
import re
from collections import Counter

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()

def most_frequent_words(text, n=3):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(n)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)

frequent_words = most_frequent_words(cleaned_text)
print(frequent_words)
