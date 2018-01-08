#!/usr/bin/python3


import sys
from stack import Stack
import math


"BINARY OPERATORS"
def add(a, b):
    return (b + a)

def sub(a, b):
    return (b - a)

def mul(a, b):
    return (b * a)

def div(a, b):
    return (b / a)

def mod(a, b):
    return (b % a)

def power(a, b):
    return b ** a

"UNARY OPERATORS"
def unot(a):
    return float(not(a))

def fact(a):
    return math.factorial(a)

def dec(a):
    return (a - 1)

def inc(a):
    return (a + 1)

def root(a):
    return math.sqrt(a)

def square(a):
    return a ** 2

def log(a):
    return math.log10(a)

def uabs(a):
    return math.fabs(a)

def ln(a):
    return math.log(a)


binary_ops = {
            '+' :   add,
            '-' :   sub,
            '*' :   mul,
            '/' :   div,
            '%' :   mod,
            '^' :   power
            }

unary_ops = {
            'n'   : unot,
            '!'   : fact,
            '--'  : dec,
            '++'  : inc,
            'r'   : root,
            's'   : square,
            'l'   : log,
            'a'   : uabs,
            'ln'  : ln
            }

constants = {
            'pi': math.pi,
            'e' : math.e
            }


def calculate(line):

    tokens = line.split()

    stack = Stack()


    for token in tokens:
        if token in binary_ops:
            a = stack.pop()
            b = stack.pop()
            stack.push(binary_ops[token](a, b))
        elif token in unary_ops:
            a = stack.pop()
            stack.push(unary_ops[token](a))
        elif token in constants:
            stack.push(constants[token])
        else:
            try:
                stack.push(float(token))
            except ValueError:
                return "Bad token: {}".format(token)


    if len(stack) != 1:
        return "Expected 1 item in stack, instead got {} for line: {}".format(len(stack), line)
    else:
        return stack.peek()


def main():

    for line in sys.stdin:
        output = calculate(line)
        sys.stdout.write("{}\n".format(output))
        sys.stdout.flush()


if __name__ == '__main__':
    main()
