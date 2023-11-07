#!/usr/bin/python3
def multiple_returns(sentence):
    b = len(sentence)
    for a in sentence:
        if b == 0:
            first = 0
        else:
            first = sentence[0]
        return b, first
