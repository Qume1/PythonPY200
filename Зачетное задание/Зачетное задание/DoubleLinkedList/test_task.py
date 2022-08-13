from unittest import TestCase

from task import DoubleLinkedList


class TestNode(TestCase):
    def test_count(self):
        expected_value = 1
        list_ = [1, 2, 3, 4, 5, 6, 7]
        lll = DoubleLinkedList(list_)
        actual_value = lll.count_(1)
        assert actual_value == expected_value
