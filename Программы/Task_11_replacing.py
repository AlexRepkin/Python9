#!usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Первый словарь, где ключи - цифры, а значения - строки.
    key_numbers = {i: chr(i) for i in range(45, 55)}
    print("Good day, first variant of dictionary:\n", key_numbers)
    # Второй словарь, где ключи - строки, а значения - символы.
    key_symbols = {i: j for j, i in key_numbers.items()}
    print("Reversed variant of dictionary:\n", key_symbols)
