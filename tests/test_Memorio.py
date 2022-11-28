from unittest import TestCase
import pandas as pd
import numpy as np
import pytest


class CustomClass:

    def __init__(self):
        self.a = 1


class TestMemorio(TestCase):

    def setUp(self):
        pass

    @pytest.mark.parametrize("inputs", [
            1, "test", [1, 2], {"a": 1, "b": 2}, pd.Series([0]), np.array([0]), CustomClass(), lambda x: x])
    def test_cache_basic(self, inputs):
        # Test a typical usage of memorio
        self.fail()

    def test_cache_basic_online_def(self, inputs):
        # Test a typical usage of memorio with online defined class
        class CustomCustomClass:

            def __init__(self):
                self.a = 1

        self.fail()

    def test_fun_changed(self):
        # Test if function change has been spotted and cache properly discarded
        self.fail()

    def test_nested_fun_changed(self):
        # Test if nested function change has been spotted and cache properly discarded
        self.fail()

    def test_persistent_storage(self):
        # Test if the storage persists across session.
        self.fail()

    def test_build_functions_tree(self):
        # Test if it can build a correct function tree , e.g. the structure of function and subfunction call to know
        # where to look when the programme check if there is any change
        self.fail()


class TestRecallFunc(TestCase):

    def test_check_for_modification(self):
        # Check if it can properly see a change in a function and in subfunctions.
        self.fail()
