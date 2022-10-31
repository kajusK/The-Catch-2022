import re
from typing import Dict
from dataclasses import dataclass


@dataclass
class Site:
    id: int
    code: str
    neighbors: Dict[int, int]


with open('Area_52.dot', 'r') as f:
    data = f.readlines()

sites = {}
sites[0] = Site(0, '', {})

# path length to look for
expected = 163912

for line in data:
    if 'code' in line:
        match = re.search(r'([0-9]{3}).*code \'(.)\'', line)
        id = int(match.group(1))
        code = match.group(2)
        sites[id] = Site(id, code, {})

    elif '->' in line:
        match = re.search(r'([0-9]{3}) -> ([0-9]{3}).*dist=([0-9]+)', line)
        start = int(match.group(1))
        end = int(match.group(2))
        dist = int(match.group(3))
        sites[start].neighbors[end] = dist


def traverse(node: int, visited: list, path: str, distance: int):
    if node == 0 and distance == expected:
        print(path)
        exit()

    if node in visited:
        return

    visited = visited.copy()
    visited.append(node)
    for neighbor, dist in sites[node].neighbors.items():
        traverse(neighbor, visited, path + sites[node].code, distance + dist)

traverse(0, [], '', 0)
