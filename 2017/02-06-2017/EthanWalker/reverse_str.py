#!/usr/bin/env python3

def reverse_str(str):
    '''
    Reverses the characters in a provided string
    using slicing and a negative step
    :param str: string to be reversed
    :return: reversed string
    '''
    return str[::-1]

def reverse_line(line):
    '''
    Reverse each word in a multi word string but keep order intact
    :param line: input line that needs words reversed
    :return: string of the input line with each word reversed
    '''
    return ' '.join(''.join(reverse_str(word)) for word in line.split())