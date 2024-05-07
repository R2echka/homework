import pytest

import sys, os
sys.path.append(os.getcwd())
from scr.decorators import log

@log()
def idk(a, b):
    return a / b

@log('idk.txt')
def idk2():
    return 'Hello \n'

def test_log() -> None:
    assert idk(4, 2) == 'idk ok'
    assert idk(1, 0) == 'idk error: ZeroDivisionError. Inputs: (1, 0), {}'
    with open('idk.txt') as f:
        idk2()
        assert f.readlines()[-1] == 'idk2 ok\n'