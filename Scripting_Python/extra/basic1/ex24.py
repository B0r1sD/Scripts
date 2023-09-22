#!/usr/bin/python

string = input('give: ')

def is_vowel(char):
    all = 'aeiou'
    return char in all

print(is_vowel(string))