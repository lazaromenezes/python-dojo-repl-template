from greeter import Greeter
import unittest

class GreeterTest(unittest.TestCase):

    def test_greet(self):

        greeter = Greeter()

        self.assertEqual("Hello, Joe", greeter.greet("Joe"))
