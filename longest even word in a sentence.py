"""
My brother mentioned this problem he came across browsing the internet.
Given a sentence, return the longest word in that sentence that has an even number of letters. Currently doesn't differentiate between letters, numbers or punctuations.
"""

def solution(input_string):
    words_as_list = input_string.split(" ")
    evens = list()
    for word in words_as_list:
        if len(word) % 2 == 0:
            evens.append(word)
    longest_even = evens[0]
    for i in range(len(evens) - 1):
        if len(evens[i + 1]) > len(evens[i]):
            longest_even = evens[i + 1]
    return longest_even
