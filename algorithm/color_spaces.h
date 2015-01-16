#ifndef COLOR_SPACES_H
#define COLOR_SPACES_H

#include <algorithm>

struct Lab { double L; double a; double b;};

class RGB
{
private:
  double r; double g; double b;

  static double pivot_rgb(double n)
  {
    return (n > 0.04045 ? std::pow((n + 0.055) / 1.055, 2.4) : n / 12.92) * 100.0;
  }

  static double pivot_xyz(double n)
  {
    return n > 0.008856 ? std::pow(n, 1/3.0) : (903.3 * n + 16) / 116;
  }

  static double distance(double a, double b)
  {
    return (a - b) * (a - b);
  }

  Lab to_lab() const
  {
    auto R = pivot_rgb(r / 255.0);
    auto G = pivot_rgb(g / 255.0);
    auto B = pivot_rgb(b / 255.0);

    auto X = R * 0.4124 + G * 0.3576 + B * 0.1805;
    auto Y = R * 0.2126 + G * 0.7152 + B * 0.0722;
    auto Z = R * 0.0193 + G * 0.1192 + B * 0.9505;

    auto x = pivot_xyz(X / 95.047);
    auto y = pivot_xyz(Y / 100.0);
    auto z = pivot_xyz(Z / 108.883);
    auto L = std::max<double>(0, 116 * y - 16);
    auto a = 500 * (x - y);
    auto b = 200 * (y - z);
    
    return Lab{L, a, b};
  }
public:
  RGB(double r, double g, double b) : r(r), g(g), b(b) {}
  explicit RGB(int color) : r(color >> 16), g((color >> 8) & 0xFF), b(color & 0xFF) {}

  static double get_distance(const RGB& color1, const RGB& color2)
  {
    auto c1 = color1.to_lab(), c2 = color2.to_lab();

    return std::sqrt(distance(c1.L, c2.L) + distance(c1.a, c2.a) + distance(c1.b, c2.b));
  }
};


#endif
