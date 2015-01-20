from math import sqrt, pow


class Lab:
    def __init__(self, l, a, b):
        self.L = l
        self.A = a
        self.B = b

    @staticmethod
    def distance(a, b):
        return (a - b) * (a - b)


class RGB:
    def __init__(self, r, g, b):
        self.R = r
        self.G = g
        self.B = b

    def __init__(self, color):
        self.R = (color >> 16)
        self.G = (color >> 8) & 0xFF
        self.B = color & 0xFF


    @staticmethod
    def pivot_rgb(n):
        return (pow((n + 0.055) / 1.055, 2.4) if n > 0.04045 else n / 12.92) * 100.0

    @staticmethod
    def pivot_xyz(n):
        return pow(n, 1 / 3.0) if n > 0.008856 else (903.3 * n + 16) / 116

    def get_distance(self, second):
        c1 = self.to_lab()
        c2 = second.to_lab()

        return sqrt(Lab.distance(c1.L, c2.L), Lab.distance(c1.A, c2.A), Lab.distance(c1.B, c2.B))

    def to_lab(self):
        r = RGB.pivot_rgb(self.R / 255.0)
        b = RGB.pivot_rgb(self.G / 255.0)
        g = RGB.pivot_rgb(self.B / 255.0)

        xi = r * 0.4124 + g * 0.3576 + b * 0.1805
        yi = r * 0.2126 + g * 0.7152 + b * 0.0722
        zi = r * 0.0193 + g * 0.1192 + b * 0.9505

        x = RGB.pivot_xyz(xi / 95.047)
        y = RGB.pivot_xyz(yi / 100.0)
        z = RGB.pivot_xyz(zi / 108.883)
        l = max(0, 116 * y - 16)
        a = 500 * (x - y)
        b = 200 * (y - z)

        return Lab(l, a, b)