import os
import csv
import re

# Set file path
ppath1 = os.path.join("paragraph_1.txt")

# Print opening statement

print("Paragraph Analysis")
print("-----------------")

# Set word counter
num_words = 0
letters = 0

#Open and count words 
with open(ppath1, "r", encoding="utf-8") as f:
    for line in f:
        words = line.split()
        num_words += len(words)
#Print words        
print("Approximate Word Count:", num_words)

# Define number of sentences by total number of periods
num_sentences = line.count('.')

# Print out the total number of sentences
print("Approximate Sentence Count:", num_sentences)
      
# Define the letter count
letters += sum(len(words) for words in line)

# Print Average letter count
Average_Letter_Count = letters/num_words      
print("Average Letter Count:", Average_Letter_Count)

# Print out the number of words in a sentence(aka sentence length)
Average_sentence_length = num_words/num_sentences
print("Average Sentence Length:", Average_sentence_length)
