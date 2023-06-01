import numpy as np

class PpmImage:
    def __init__(self, w, h):
        self.image = np.zeros((h, w, 3), dtype=np.uint8)

    def setPixel(self, x, y, color):
        self.image[y][x] = np.array([color.x, color.y, color.z])

    def writeFile(self, filename):
        with open(filename, "w") as f:
            f.write(self.writeString())

    def writeString(self):
        s = f"P3\n{self.image.shape[1]} {self.image.shape[0]}\n255\n"
        for y in range(self.image.shape[0]-1, -1, -1):
            print(f"Scanlines remaining: {y} ")
            for x in range(0, self.image.shape[1]):
                r = self.image[y][x][0]
                g = self.image[y][x][1]
                b = self.image[y][x][2]
                s += f"{r} {g} {b}\n"
        return s


""" if __name__ == "__main__":

    #Image
    image_width = 256
    image_height = 256

    #Render
    with open("ppm.jpg", "w") as f:
        print(f"P3\n{image_width} {image_height}\n255\n")
        f.write(f"P3\n{image_width} {image_height}\n255\n")

        for y in range(image_height-1, -1, -1):
            print(f"Scanlines remaining: {y}")
            for x in range(0, image_width):
                r = float(x)/(image_width-1)
                g = float(y)/(image_height-1)
                b = 0.25

                ir = int(r*256)
                ig = int(g*256)
                ib = int(b*256)

                #print(f"{ir} {ig} {ib}\n")
                f.write(f"{ir} {ig} {ib}\n") """
