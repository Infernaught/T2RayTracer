import unittest
from vec3 import vec3

class TestVec3(unittest.TestCase):
    def test_add(self):
        a = vec3()
        b = vec3(1,1,1)
        c = a+b
        self.assertEqual(c, vec3(1,1,1))

    def test_sub(self):
        a = vec3()
        b = vec3(1,1,1)
        c = a-b
        self.assertEqual(c, vec3(-1,-1,-1))

    def test_mul(self):
        a = vec3(1, 2, 3)
        b = vec3(2, 3, 4)
        c = a*b
        d = a*2
        self.assertEqual(c, vec3(2, 6, 12))
        self.assertEqual(d, vec3(2, 4, 6))

    def test_truediv(self):
        a = vec3(2, 2, 2)
        b = a/2
        self.assertEqual(b, vec3(1, 1, 1))

    def test_dot(self):
        a = vec3(1, 2, 3)
        b = vec3(2, 3, 4)
        c = a.dot(b)
        self.assertEqual(c, 20)

    def test_cross(self):
        a = vec3(1, 2, 3)
        b = vec3(2, 3, 4)
        c = a.cross(b)
        self.assertEqual(c, vec3(-1, 2, -1))

    def test_length_squared(self):
        a = vec3(1, 2, 3)
        b = a.length_squared()
        self.assertEqual(b, 14)

    def test_length(self):
        a = vec3(1, 2, 3)
        b = a.length()
        self.assertEqual(b, 14**0.5)

    def test_unit_vector(self):
        a = vec3(1, 2, 3)
        b = a.unit_vector()
        self.assertEqual(b, vec3(1, 2, 3)/14**0.5)

if __name__ == "__main__":
    unittest.main()
