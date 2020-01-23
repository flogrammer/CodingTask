"""" Testing of the coding task 2 """
import pytest
import merging

# Instantiate merger class in order to use methods
mf = merging.MergingFactory()

def test_basic_interval_list():
    intervals = [[25, 30], [2, 19], [14, 23], [4, 8], [100, 101]]
    expected_result = [[2, 23], [25, 30], [100, 101]]
    assert all([a == b for a, b in zip(expected_result, mf.merge(intervals))])

def test_negative_interval_list():
    intervals = [[-25, 1], [2, 19], [14, 23], [-8, -4]]
    expected_result = [[-25, 1], [2, 23]]
    assert all([a == b for a, b in zip(expected_result, mf.merge(intervals))])

def test_empty_interval_list():
    intervals = []
    expected_result = []
    assert all([a == b for a, b in zip(expected_result, mf.merge(intervals))])

def test_large_interval_list():
    intervals = [[1, 123567876545678765412345665432345676543], [2, 19], [14, 23], [-8, -4]]
    expected_result = [[-8, -4], [1, 123567876545678765412345665432345676543]]
    assert all([a == b for a, b in zip(expected_result, mf.merge(intervals))])

def test_non_numeric_interval_list():
    intervals = [["1", 2], [2, 19.2]]
    intervals2 = [[[1, 2], 2]]
    with pytest.raises(Exception):
        mf.merge(intervals)
        mf.merge(intervals2)

def test_complete_overlap_interval_list():
    intervals = [[1, 100], [2, 19], [14, 23], [3, 5]]
    expected_result = [[1, 100]]
    assert all([a == b for a, b in zip(expected_result, mf.merge(intervals))])

def test_one_element_interval_list():
    intervals = [[1, 2]]
    expected_result = [[1, 2]]
    assert all([a == b for a, b in zip(expected_result, mf.merge(intervals))])

def test_two_elements_interval_list():
    intervals = [[1, 3], [1, 2]]
    expected_result = [[1, 3]]
    assert all([a == b for a, b in zip(expected_result, mf.merge(intervals))])

def test_identical_interval_lists():
    intervals = [[1, 2], [1, 2]]
    expected_result = [[1, 2]]
    assert all([a == b for a, b in zip(expected_result, mf.merge(intervals))])

def test_wrong_shape_interval_lists():
    intervals = [[1, 2, 4, 5], [1, 2]]
    with pytest.raises(Exception):
        mf.merge(intervals)

def test_wrong_interval_order():
    intervals = [[5, 3], [7, 2]]
    with pytest.raises(Exception):
        mf.merge(intervals)
