from ppm import PpmImage
from vec3 import vec3
from ray import ray

def ray_color(r):
    unit_direction = r.direction.unit_vector()
    t = 0.5 * (unit_direction.y + 1.0)
    return vec3(1.0, 1.0, 1.0) * (1.0-t) + vec3(0.5, 0.7, 1.0) * t

if __name__ == "__main__":
    #Image
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)

    #Camera
    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = vec3(0, 0, 0)
    horizontal = vec3(viewport_width, 0, 0)
    vertical = vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal/2 - vertical/2 - vec3(0, 0, focal_length)

    #Render
    im = PpmImage(image_width, image_height)
    for y in range(image_height-1, -1, -1):
        print(f"Scanlines remaining: {y} ")
        for x in range(0, image_width):
            u = float(x) / (image_width-1)
            v = float(y) / (image_height-1)
            r = ray(origin, lower_left_corner + horizontal*u + vertical*v - origin)
            color = ray_color(r)*255
            im.setPixel(x, y, color)
    print(im.image)
    im.writeFile("ray_img.jpg")
    print("Done.\n")
