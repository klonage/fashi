#include "user_info.h"
#include "color_spaces.h"

#include <algorithm>
#include <set>
#include <iostream>
#include <vector>
#include <fstream>
#include <map>
#include <ctime>
#include <cmath>

using namespace std;

typedef std::map<Style, std::pair<int, int>> cm_type; 

cm_type get_color_match()
{
	static cm_type cm;
	if (!cm.empty())
		return cm;



	return cm;
}

void load_color_matcher(const std::string& filename, bool ignore_header = false)
{
	// todo color_matcher;
}

std::vector<Item> load_csv(const std::string& filename, bool ignore_header = false)
{
	std::ifstream input(filename);
	int type;
	int gender;
	int style;
	int color;

	if (!ignore_header)
	{
		std::string dummy_line;
		std::getline(input, dummy_line);
	}

	std::vector<Item> items;

	while(input >> type >> gender >> style >> color)
	{
		items.push_back(Item{color, (Gender)gender, (Type)type, (Style)style});
	}

	std::cout << "loaded " << items.size() << " records" << std::endl;
	return items;
}

int main (int argc, char ** argv)
{
	srand(time(nullptr));
	std::cout << RGB::get_distance(RGB(10, 25, 10), RGB(10, 10, 100)) << std::endl;

	if (argc < 2 + static_cast<int>(style_names.size()))
	{
		std::cout << "not enough arguments" << std::endl;
		return 0;
	}

	UserInfo user;

	for (std::size_t i = 0; i < style_names.size(); i++)
		user.styles[i] = atof(argv[i+2]);

	auto items = load_csv(argv[1]);
	int flag = 0;
	Item item = user.get_next_item(items);
	while (true)
	{
		char choice;

		if (flag == 1)
			flag = get_rand(10) > 5 ? 0 : 2;

		switch (flag)
		{
		case 0:
			std::cout << "Automat zaproponowal Ci nastepujacy element:" << std::endl;
			item = user.get_next_item(items);
			break;
		case 2:
			std::cout << "do tego ubrania bedzie pasowac Ci cos takiego: " << std::endl;
			item = user.get_matching_to_previous(items);
			break;
		}

		std::cout << item.get_description() << std::endl;
		std::cout << "(M)am to\t\t(K)upuje\t\t(N)ie podoba mi sie" << std::endl;
		std::cin >> choice;
		choice = tolower(choice);

		switch (choice)
		{
		case 'm':
		user.have_it(item);
		std::cout << "Ok, zapamietam ze to juz masz!" << std::endl;
		flag = 2;
		break;
		case 'k':
			user.buy_it(item);
			std::cout << "Yeah, kupiles to!" << std::endl;
			flag = 1;
			break;
		case 'n':
			user.dont_like_it(item);
			std::cout << "Szkoda, ze Ci sie nie podoba :(" << std::endl;
			flag = 0;
			break;
		default:
			std::cout << "Zly wybor, wiec domyslam sie ze Ci sie nie podoba" << std::endl;
			user.dont_like_it(item);
		}
	}

	return 0;
}
