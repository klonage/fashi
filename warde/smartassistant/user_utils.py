from random import randint
from sets import Set

display_ratio = []
forbidden = []


def user_get_match_item(user, item):
    rate = user.styles[item.style] * 0.6
    rate += 0 if len(user.bought) == 0 else counted_ratio

    tmp = -(rate - display_ratio[item.type]) / (1 - display_ratio[item.type]) if rate > display_ratio[
        item.type] else 1 - rate / display_ratio[item.type]
    rate += tmp * 0.4

    return rate


def user_get_unbought_items(user, all_items, except_type=None):
    return [item for item in all_items if
            item.gender == user.gender and item.type != except_type and item not in user.bought]


def user_get_next_item(user, all_items):
    except_type = None if len(user.bought) == 0 else user.bought[-1].type
    area = user_get_unbought_items(user, all_items, except_type)

    ret_item = None
    match_index = 0.0
    already_found = Set()

    for i in range(0, min(10, len(area))):
        index = 0

        while True:
            index = randint(0, len(area)-1)
            if index not in already_found:
                break

        tmp_m_i = user_get_match_item(user, area[index])

        if tmp_m_i > match_index:
            match_index = tmp_m_i
            ret_item = area[index]

    return ret_item


def user_get_similar(user, item, all_items):
    area = user_get_unbought_items(user, item, all_items)

    tries = 0
    best_item = None
    best_ratio = 0

    while tries < 10:
        n = randint(0, len(area) - 1)

        if (item.type, area[n].type) in forbidden or (area[n].type, item.type) in forbidden:
            continue

        tries += 1

        m = get_match(item, area[n])

        if m > best_ratio:
            best_ratio = m
            best_item = area[n]

    return best_item