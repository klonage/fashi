#ifndef ITEM_H
#define ITEM_H

#include "color_spaces.h"

#include <map>
#include <string>

enum class Type
{
	BUTY,
	SPODENKI,
	BLUZA,
	KOSZULA,
	MARYNARKA,
	SPODNIE,
	END
};

std::map<Type, std::string> type_names = {
		{Type::BUTY, "buty"}, {Type::SPODENKI, "spodenki"}, {Type::BLUZA, "bluza"},
		{Type::KOSZULA, "koszula"}, {Type::MARYNARKA, "marynarka"}, {Type::SPODNIE, "spodnie"}
};

enum class Gender
{
	MEZCZYZNA,
	KOBIETA
};

std::map<Gender, std::string> gender_names = {
		{Gender::MEZCZYZNA, "mezczyzna"}, {Gender::KOBIETA, "kobieta"}
};

enum class Style
{
	SPORTOWY,
	ELEGANCKI,
	EKSTRAWAGANCKI,
	END
};

std::map<Style, std::string> style_names = {
		{Style::SPORTOWY, "sportowy"}, {Style::ELEGANCKI, "elegancki"},
		{Style::EKSTRAWAGANCKI, "ekstrawagancki"}
};


std::map<Style, std::map<std::pair<Type, Type>, std::vector<std::pair<RGB, RGB>>>> color_matcher =
{
		{Style::SPORTOWY,
				{
						{
								{Type::BUTY, Type::SPODENKI},
								{
										{RGB(0,0,0), RGB(10,10,10)},
										{RGB(30, 20, 55), RGB(52,100, 20)}
								}
						},
						{
								{Type::BUTY, Type::BLUZA},
								{
										{RGB(30, 40, 50), RGB(23, 66, 120)}
								}
						}
				}
		},
		{Style::ELEGANCKI,
				{
						{
								{Type::BUTY, Type::BLUZA},
								{
										{RGB(102, 44, 52), RGB(32, 66, 10)}
								}
						}
				}
		}
};

std::map<Type, double> display_ratio = {
		{Type::BUTY,0.16},
		{Type::SPODENKI,0.07},
		{Type::BLUZA, 0.08},
		{Type::KOSZULA,0.37},
		{Type::MARYNARKA, 0.16},
		{Type::SPODNIE, 0.26}
};

std::vector<std::pair<Type, Type>> forbidden = {
		{Type::BLUZA, Type::MARYNARKA},
		{Type::KOSZULA, Type::BLUZA},
		{Type::SPODENKI, Type::KOSZULA},
		{Type::SPODENKI, Type::MARYNARKA},
		{Type::SPODENKI, Type::SPODNIE}
};

int get_rand(int max)
{
	return rand() % (max+1);
}

struct Item
{
	int color;
	Gender gender;
	Type type;
	Style style;

	std::string get_description() const
	{
		std::string val = type_names[type] + " " + style_names[style] + " " + gender_names[gender] + "(";
		int red = color >> 16, green = (color >> 8) & 0xFF, blue = color & 0xFF;
		auto make_color = [](char c, int v) {
			return std::string(1, c) + ":" + std::to_string(static_cast<int>(v/256.0*100));
		};
		val += make_color('r', red) + " " + make_color('g', green) + " " + make_color('b', blue) + ")";

		return val;
	}

	static double find_best_color_distance(Item first, Item second)
	{
		if ((int)first.type > (int)second.type)
			std::swap(first, second);
		auto pp = std::make_pair(first.type, second.type);
		if (first.style == second.style) // && color_matcher.find(first.style) != color_matcher.end() && color_matcher[first.style].find(pp) != color_matcher[first.style].end() && !color_matcher[first.style][pp].empty())
		{
			auto vec = color_matcher[first.style][pp];
			double min_dist = 100;

			//for (auto c : vec)
			{
				//auto d = std::max(RGB::get_distance(RGB(first.color), c.first),
				//		RGB::get_distance(RGB(second.color), c.second));
				//if (d < min_dist)
				//	min_dist = d;
				min_dist = RGB::get_distance(RGB(first.color), RGB(second.color));
			}

			return min_dist;
		}

		return 30+get_rand(70);
	}

	double get_match(const Item& second) const
	{
		if (gender != second.gender || type == second.type)
			return -1; // todo optional<double> !
		double ret = style == second.style ? 0.5 : 0;
		ret += (100-find_best_color_distance(*this, second))/100.0*0.5;

		return ret;
	}
};


bool operator== ( const Item &i1, const Item &i2)
{
	return i1.color == i2.color && i1.gender == i2.gender && i1.style == i2.style && i1.type == i2.type;
}

#endif
