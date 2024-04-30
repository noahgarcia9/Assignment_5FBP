# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:49:16 2024

@author: Noah Garcia
"""

import random
from collections import Counter

def extract_word_pairs(text):
    words = text.split()
    return [(words[i], words[i+1]) for i in range(len(words)-1)]

def count_word_pairs(word_pairs):
    return Counter(word_pairs)

def choose_starting_word(unique_words):
    return random.choice(list(unique_words))

def generate_sentence(text):
    word_pairs = extract_word_pairs(text)
    word_pairs_counts = count_word_pairs(word_pairs)
    unique_words = set(word for pair in word_pairs for word in pair)
    start_word = choose_starting_word(unique_words)
    
    sentence = [start_word]
    current_word = start_word
    
    while True:
  
        candidates = [pair for pair in word_pairs_counts if pair[0] == current_word]
        
      
        if not candidates:
            break
        
       
        next_words = random.choices([pair[1] for pair in candidates], 
                                    weights=[word_pairs_counts[pair] for pair in candidates], k=1)
        
        next_word = next_words[0]
        sentence.append(next_word)
        
    
        if next_word == '.':
            break
        
        current_word = next_word
    
    return ' '.join(sentence)

text = "The cat sat on the mat. The cat ate the mouse. The mouse ran away. The cat slept."
print(generate_sentence(text))
