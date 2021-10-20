from unittest import TestCase
import main


class Test(TestCase):
    def test_print_hi(self):
        assert main.print_hi(3,4),7
