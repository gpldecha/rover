import unittest
from roverkit.utils.rover_utils import linear_scaling


class TestUtils(unittest.TestCase):

    def test_linear_interpolation(self):
        value = linear_scaling(0., -1., 1., 1020., 2006.)
        self.assertAlmostEqual(value, (1020. + 2006.)/2.0, places=6)

        value = linear_scaling(-1., -1., 1., 1020., 2006.)
        self.assertAlmostEqual(value, 1020.0, places=6)

        value = linear_scaling(1., -1., 1., 1020., 2006.)
        self.assertAlmostEqual(value, 2006.0, places=6)
