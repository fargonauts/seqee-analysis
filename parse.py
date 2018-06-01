import sys
from copy import deepcopy
from pprint import pprint
from collections import defaultdict

def parse_sequence(header):
    _, *header = header.split(' ')
    problem = tuple()
    for item in header:
        try:
            problem += (int(item),)
        except ValueError:
            pass
    return problem

def parse_header(header):
    current = header.split('[')[1].split(']')[0]
    if (current.startswith('extend') or
        current.startswith('variation')):
        current = parse_sequence(current)
    return current

def parse_datum(line):
    a, b = line.split(':')
    b = b.strip()
    if b in ['?', '']:
        b = None
    return a, b

def save(data, current, section):
    if current is not None:
        data[current] = deepcopy(section)
        section.clear()

def parse(filename):
    data = dict()
    current = None
    section = defaultdict(list)

    with open(filename, 'r') as infile:
        for line in infile:
            if line.startswith('['):
                save(data, current, section)
                current = parse_header(line)
            elif line not in ['', '\n']:
                k, v = parse_datum(line)
                section[k].append(v)
        save(data, current, section)
    return data

