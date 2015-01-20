from color_spaces import RGB
from random import randint

color_matcher = []


def find_best_color_distance(first, second):
    if first.type > second.type:
        first, second = second, first

    pp = (first.style, second.style)

    if first.style == second.style:  # && color_matcher.find(first.style) != color_matcher.end() && color_matcher[first.style].find(pp) != color_matcher[first.style].end() && !color_matcher[first.style][pp].empty())
        vec = color_matcher[first.style][pp]
        min_dist = 100

        # for (auto c : vec)
        # auto d = std::max(RGB::get_distance(RGB(first.color), c.first),
        # RGB::get_distance(RGB(second.color), c.second));
        # if (d < min_dist)
        # min_dist = d;
        min_dist = RGB.get_distance(RGB(first.color), RGB(second.color))

        return min_dist

    return randint(30, 100)


def get_match(first, second):
    if first.gender != second.gender or first.type == second.type:
        return None

    ret = 0.5 if first.style == second.style else 0
    ret += (100-find_best_color_distance(first, second))/100.0*0.5

    return ret