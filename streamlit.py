# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:51:11 2024

@author: Noah Garcia
"""

import streamlit as st
import random
from collections import Counter

# Define functions from your assignment
def extract_word_pairs(text):
    words = text.split()
    return [(words[i], words[i + 1]) for i in range(len(words) - 1)]

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
        if next_word.endswith('.'):
            break
        current_word = next_word
    
    return ' '.join(sentence)

# Streamlit application layout
st.title("Interactive Sentence Generator")
st.subheader("Upload a text file or enter text manually to generate a sentence based on its structure.")

# Text input
text_input = st.text_area("Enter text here:", height=150)
file_uploaded = st.file_uploader("Or upload a text file (.txt):", type="txt")

# Use the most appropriate input
if file_uploaded is not None:
    text = str(file_uploaded.read(), "utf-8")
elif text_input:
    text = text_input
else:
    text = None

# Button to generate sentence
if st.button("Generate Sentence"):
    if text:
        generated_sentence = generate_sentence(text)
        st.write("Generated Sentence:", generated_sentence)
        st.download_button("Download Sentence", generated_sentence, file_name="generated_sentence.txt")
    else:
        st.error("Please input text or upload a file to generate a sentence.")
        
        streamlit run app.py