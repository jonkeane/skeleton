import pytest
from unittest import TestCase

from skeleton import addition

class TestOne(TestCase):
    def test_add(self):
        assert addition.add_one(1) == 2
        assert addition.add_one(2) == 3

    def test_add_too_big(self):
        with pytest.raises(ValueError):
            addition.add_one(100)
