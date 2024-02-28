import unittest
from Tests import Map_tests

test_suite = unittest.TestSuite()

# Add to suite for each method in test class
test_suite.addTest(Map_tests.Map_tests('test1'))
# ...

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)


