import unittest
import numpy as np
from vec3 import vec3
from ppm import PpmImage

class TestPpm(unittest.TestCase):
    def test_setPixel(self):
        a = PpmImage(256, 256)
        color = vec3(255, 255, 255)
        a.setPixel(0, 0, color)
        b = np.zeros((256, 256, 3), dtype=np.uint8)
        b[0][0] = np.array([255, 255, 255])
        self.assertTrue(np.array_equal(a.image, b))

    def test_writeString(self):
        a = PpmImage(256, 256)
        for y in range(a.image.shape[1]-1, -1, -1):
            print(f"Scanlines remaining: {y}")
            for x in range(0, a.image.shape[0]):
                r = float(x)/(a.image.shape[1]-1)
                g = float(y)/(a.image.shape[0]-1)
                b = 0.25

                ir = int(r*255.999)
                ig = int(g*255.999)
                ib = int(b*255.999)
                color = vec3(ir, ig, ib)

                a.setPixel(x, y, color)
        with open("ppm_test.jpg", "r") as f:
            b = f.read()
        self.assertEqual(a.writeString(), b)

    def test_writeFile(self):
        a = PpmImage(256, 256)
        for y in range(a.image.shape[1]-1, -1, -1):
            print(f"Scanlines remaining: {y}")
            for x in range(0, a.image.shape[0]):
                r = float(x)/(a.image.shape[1]-1)
                g = float(y)/(a.image.shape[0]-1)
                b = 0.25

                ir = int(r*255.999)
                ig = int(g*255.999)
                ib = int(b*255.999)
                color = vec3(ir, ig, ib)

                a.setPixel(x, y, color)
        a.writeFile("ppm.jpg")
        with open("ppm_test.jpg", "r") as f:
            b = f.read()
        self.assertEqual(a.writeString(), b)

if __name__ == "__main__":
    unittest.main()