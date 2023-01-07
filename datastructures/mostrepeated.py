# find most repeated charachter in this sentence
sentence = "This is a common interview question"
# looked the answer from geeksforgeeks 1st option as they call a naive one
all_freq = {}
for j in sentence:
 if j in all_freq:
  all_freq[j] += 1
 else:
  all_freq[j] = 1
res = max(all_freq, key = all_freq.get)

print(type(all_freq))
print("The most repeated character is -", res)

# from the video lessons version
from pprint import pprint

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(char_frequency.items(), 
key=lambda kv: kv[1], reverse=True)

print(char_frequency_sorted[0])