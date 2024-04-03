#!/usr/bin/env python3
"""

author: Enoc Martínez
institution: Universitat Politècnica de Catalunya (UPC)
email: enoc.martinez@upc.edu
license: MIT
created: 3/4/24
"""
import rich

def stupid_example():
    rich.print("Hey! I'm just a stupid example")


def add_numbers(a: int, b :int) -> int:
    assert type(a) is int
    assert type(b) is int
    return a + b
