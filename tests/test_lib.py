# tests/test_lib.py
from mlproject.lib import hello_world

def test_length_of_hello_world():
    assert len(hello_world()) != 0

from mlproject.distance import haversine

def test_variable():
    assert type(haversine(38,25,15,15)) == float
