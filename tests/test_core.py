import unittest
import numpy as np
from tvet.core import Asteroid

class TestAsteroid(unittest.TestCase):
    def setUp(self):
        # Minimal triangle mesh for testing
        self.vertices = np.array([
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0]
        ])
        self.faces = np.array([
            [0, 1, 2]
        ])
        # Patch load_obj to return our test mesh
        import tvet.io
        self._orig_load_obj = tvet.io.load_obj
        tvet.io.load_obj = lambda filename: (self.vertices.copy(), self.faces.copy())

    def tearDown(self):
        # Restore original load_obj
        import tvet.io
        tvet.io.load_obj = self._orig_load_obj

    def test_geometry(self):
        asteroid = Asteroid(filename="./tests/dummy.obj")
        asteroid.get_geometry()
        self.assertEqual(asteroid.centers.shape, (1, 3))
        self.assertEqual(asteroid.normals.shape, (1, 3))

    def test_cosines(self):
        asteroid = Asteroid(filename="./tests/dummy.obj")
        asteroid.get_cosines()
        self.assertTrue(hasattr(asteroid, "s"))
        self.assertTrue(hasattr(asteroid, "o"))

if __name__ == "__main__":
    unittest.main()