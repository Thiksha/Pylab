from collections import Counter

def word_count(fname):
            with open(fname) as f:
                    return Counter(f.read().split())

print("no. of words in the file :", word_count("text.txt"))
