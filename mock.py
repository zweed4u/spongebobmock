#!/usr/bin/python3
import random

sentence = input("Sentence to transform: ")

def spongebob_mock(sentence: str) -> str:
    reconstructed_sentence_split = []
    for word in sentence.split():
        new_word_string = ''
        for letter in word:
            if random.random() >= .5:
                new_word_string += letter.upper()
            else:
                new_word_string += letter.lower()
        reconstructed_sentence_split.append(new_word_string)
    return ' '.join(reconstructed_sentence_split)

print(spongebob_mock(sentence))

