#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    file = 'text.txt'
    with open(file, 'r', encoding='utf-8-sig') as f:
        sentence = f.read().split('.')
        reverse_sentence = '. '.join(reversed(sentence))
        print(reverse_sentence)
