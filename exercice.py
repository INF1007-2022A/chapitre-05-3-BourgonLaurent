#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def get_num_letters(text: str) -> int:
    letter_count = 0
    for t in text:
        if t.isalnum():
            letter_count += 1

    return letter_count


def get_word_length_histogram(text: str) -> list[int]:
    # Get length of each word
    counts = [get_num_letters(word) for word in text.split()]

    # Get how many different lengths there are
    lengths = set(counts)
    # Add one for the zero-index
    histogram = [0] * (max(lengths) + 1)

    # Change value of lengths,
    # indices without lengths
    # will stay unchanged (l[i] == 0)
    for l in lengths:
        histogram[l] = counts.count(l)

    return histogram


def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
    BLOCK_CHAR = "|"
    LINE_CHAR = "¯"

    return ""


if __name__ == "__main__":
    spam = "Stop right there criminal scum! shouted the guard confidently."
    eggs = get_word_length_histogram(spam)
    print(eggs, "\n")
    print(format_histogram(eggs), "\n")
    print(format_horizontal_histogram(eggs))
