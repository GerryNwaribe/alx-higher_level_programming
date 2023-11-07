#!/usr/bin/python3
def multiple_returns(sentence):
    b = len(sentence)
    for a in sentence:
        if b == 0:
            first = None
        else:
            first = sentence[0]
        return b, first
        