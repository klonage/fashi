#ifndef USER_INFO_H
#define USER_INFO_H

#include "item.h"

#include <algorithm>
#include <set>
#include <vector>

class UserInfo
{
public: // beware, classes!
	std::vector<Item> bought;

	float styles[static_cast<int>(Style::END)];
	Gender gender;

	float get_match_item(const Item& item)
	{
		float ret = styles[static_cast<int>(item.style)] * 0.6;

		auto rate = bought.empty() ? 0 : std::count_if(bought.begin(), bought.end(), [item](const Item& i) -> bool {
			return item.type == i.type;
		}) / static_cast<double>(bought.size());

		ret += (rate > display_ratio[item.type] ? -(rate-display_ratio[item.type])/(1-display_ratio[item.type]) : 1 - rate / display_ratio[item.type]) * 0.4;
		return ret;
	}

	std::vector<Item> get_unbought_items(const std::vector<Item>& items, Type except_type = Type::END)
		{
		std::vector<Item> area;
		std::copy_if(items.begin(), items.end(), std::back_inserter(area),
				[this, except_type](const Item& i)
				{
			return gender == i.gender && i.type != except_type &&
					std::find(bought.begin(), bought.end(), i) == bought.end();
				});

		return area;
		}

	Item get_next_item(const std::vector<Item>& items)
	{
		Type except_type = bought.empty() ? Type::END : bought.back().type;
		std::vector<Item> area = get_unbought_items(items, except_type);

		std::set<int> already_found;
		Item ret_item;
		float match_index = 0.f;
		for (int i = 0; i < std::min<int>(10, area.size()); i++)
		{
			int index;
			do {
				index = get_rand(area.size()-1);
			} while(already_found.find(index) != already_found.end());

			auto tmp_m_i = get_match_item(area[index]);
			if (tmp_m_i > match_index)
			{
				match_index = tmp_m_i;
				ret_item = area[index];
			}
		}

		return ret_item;
	}

	Item get_similar(const Item& item, const std::vector<Item>& items)
	{
		auto area = get_unbought_items(items, item.type);

		int tries = 0;
		Item best_item;
		float best_ratio = 0;
		while (tries < 10)
		{
			auto n = get_rand(area.size() - 1);

			if (std::find(forbidden.begin(), forbidden.end(), std::make_pair(item.type, area[n].type)) != forbidden.end() ||
					std::find(forbidden.begin(), forbidden.end(), std::make_pair(area[n].type, item.type)) != forbidden.end())
				continue;

			tries++;
			auto m = item.get_match(area[n]);
			if (m > best_ratio)
			{
				best_ratio = m;
				best_item = area[n];
			}
		}
		return best_item;
	}

	Item get_matching_to_previous(const std::vector<Item>& items)
	{
		return get_similar(bought.back(), items);
	}

	void have_it(const Item& item)
	{
		buy_it(item);
	}
	void dont_like_it(const Item& item)
	{
		styles[static_cast<int>(item.style)] = std::max<double>(styles[static_cast<int>(item.style)] * 0.9, 0.05);
		bought.push_back(item);
	}

	void buy_it(const Item& item)
	{
		styles[static_cast<int>(item.style)] = std::min<double>(1.1-0.1 * styles[static_cast<int>(item.style)], 0.95);
		bought.push_back(item);
	}
};


#endif
