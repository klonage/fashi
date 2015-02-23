import json
import sys
import re

genders = set()
currencies = set()
sizes = set()
colors = set()
compositors = set()
types = set()
patterns = set()
fastenings = set()
brands = set()
decolletages = set()
fashions = set()
shops = set()


def parse_colors(color_str):
    return


def parse_single_json(filename):
    file = open(filename)
    json_data = json.load(file)
    file.close()

    for item in json_data:
        genders.add(item['gender'])
        if 'pattern' in item:
            patterns.add(item['pattern'])
        if 'fastening' in item:
            fastenings.add(item['fastening'])
        if 'brand' in item:
            brands.add(item['brand'])
        if 'decolletage' in item:
            decolletages.add(item['decolletage'])
        if 'fashion' in item:
            fashions.add(item['fashion'])
        shops.add(item['shop'])
        currencies.add(item['price']['currency'])
        for size in item['available_sizes']:
            sizes.add(size)
        for color in [c[0] for c in re.findall("\('(.*?)', '(.*?)'\)", item['color'])]:
            colors.add(color)
        for compositor in item['compositors']:
            compositors.add(compositor['name'])
        types.add(item['clothes_type'])


def show_possibilities(files):
    for filename in files:
        parse_single_json(filename)

    print('genders: ', genders)
    print('currencies: ', currencies)
    print('sizes: ', sizes)
    print('colors: ', len(colors), colors)
    print('compositors', compositors)
    print('types', types)
    print('patterns', patterns)
    print('fastenings', fastenings)
    print('brands', brands)
    print('decolletages', decolletages)
    print('fashions', fashions)
    print('shops', shops)


show_possibilities(sys.argv[1:])