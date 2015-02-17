import re
import json

import urllib3


__author__ = 'Marcin Kolny'


class ReservedBackend:
    _main_address = 'http://www.reserved.com/pl/pl/{gender}/{helper}/clothes/{type}'
    _genders = {'woman': 'all-1', 'man': 'all-3'}
    _common_clothes = ['outerwear', 'jackets', 'sweaters', 'sweatshirts', 'shirts', 't-shirts', 'trousers', 'jeans',
                       'lingerie']

    def __init__(self):
        self._man_clothes = ['polos', 'shorts'] + self._common_clothes
        self._woman_clothes = ['blouses', 'dresses', 'skirts'] + self._common_clothes

    def process(self):
        for gender in self._genders:
            new_address = self._main_address.replace('{gender}', gender).replace('{helper}', self._genders[gender])
            clothes = self._man_clothes if gender == 'man' else self._woman_clothes
            for c in clothes:
                json_data = self.get_json_data(new_address.replace('{type}', c))
                for single_data in json_data:
                    print(json.dumps(self.generate_fashi_json(single_data, gender, c)))

    @staticmethod
    def get_json_data(address):
        json_data = json.loads(ReservedBackend.get_json_from_page(address))
        return [(c_id, json_data[c_id]) for c_id in json_data]

    @staticmethod
    def get_json_from_page(address):
        html_data = urllib3.PoolManager().request('GET', address).data.decode('utf-8')
        res = re.search('<script type=\"text/javascript\">.*?productsJson = (.*?);.*?</script>', html_data,
                        re.DOTALL | re.MULTILINE)
        return res.group(1).strip()

    @staticmethod
    def generate_fashi_json(json_data, gender, clothes_type):
        c_id = json_data[0]
        model = json_data[1]['model'][c_id]
        html_data = urllib3.PoolManager().request('GET', model['item_url']).data.decode('utf-8')

        return {
            'name': model['item_name'],
            'description': json_data[1]['model_id'],
            'price': {'value': json_data[1]['final_price'], 'currency': json_data[1]['current_currency_code']},
            'gender': gender,
            'picture_url': model['item_photo'],
            'item_url': model['item_url'],
            'shop': 'Reserved',
            'available_sizes': [data[5:] for data in model['data-groups'] if data.startswith('size-')],
            'clothes_type': clothes_type,
            'color': str(ReservedBackend.read_colors(html_data)),
            'compositors': ReservedBackend.read_compositors(html_data)
        }

    @staticmethod
    def read_colors(html_data):
        return re.findall('color_label : \'(.*?)\',.*?sample : \'(.*?)\'', html_data, re.MULTILINE | re.DOTALL)

    @staticmethod
    def read_compositors(html_data):
        comp_str = re.search('<h3>Skład materiałowy</h3>(.*?)</div>', html_data, re.MULTILINE | re.DOTALL).group(
            1).strip()
        return [{'percentage_value': x.split(' ')[0], 'name': x.split(' ')[1]} for x in comp_str.split(', ')]
