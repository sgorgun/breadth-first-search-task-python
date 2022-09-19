"""Tests for 'tasks.components' module."""
import pytest

from tasks.cycle_existence import check_cycle_existence


@pytest.mark.timeout(2)
def test_find_number_of_components():
    """Tests for find_number_of_components function."""
    assert check_cycle_existence(5, {}) == False
    assert check_cycle_existence(10, {0: [6, 7], 6: [0, 7], 7: [0, 6]}) == True
    assert check_cycle_existence(5, {1: [0], 0: [2, 1], 2: [0]}) == False
    assert check_cycle_existence(5, {0: [1, 4], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 0]}) == True
