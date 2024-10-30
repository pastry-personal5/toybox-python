#!/usr/local/bin/python

import pprint


def gen_integers(limit):
    for i in range(0, limit):
        yield(i)

def main():
   g = gen_integers(10)
   x = next(g)
   pprint.pprint(x)
   x = next(g)
   pprint.pprint(x)

if __name__ == '__main__':
    main()