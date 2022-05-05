#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv) == 1:
        print('0 arguments.')
    else:
        print(f"{len(argv) - 1} arguments:")
        for i in range(len(argv) - 1):
            print(f"{i + 1}: {argv[i + 1]}")
