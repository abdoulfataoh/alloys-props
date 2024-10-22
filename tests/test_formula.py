# coding: utf-8


import math

import pytest

from alloys_props.formula import (
    vec, delta, pauling_negativities, entropy_of_mixing)


def compare_floats(a, b, tol=1e-9):
    return math.isclose(a, b, abs_tol=tol)


@pytest.fixture
def alloy() -> str:
    return 'Al0.5Fe'


def test_vec(alloy):
    assert vec(alloy) == 6.333


def test_delta(alloy):
    assert compare_floats(delta(alloy), 6.05) == True


def test_pauling_negativities(alloy):
    assert compare_floats(pauling_negativities(alloy), 6.05) == True


def test_entropy_of_mixing(alloy):
    assert compare_floats(entropy_of_mixing(alloy), 6.05) == True
