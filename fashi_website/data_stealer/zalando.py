import json
import urllib3
import re

__author__ = 'Marcin Kolny'


class ZalandoBackend:
    def __init__(self):
        self._main_address = 'https://www.zalando.pl/'
        self._men_clothes = self.collect_links_and_categories('odziez-meska')
        self._woman_clothes = self.collect_links_and_categories('odziez-damska')

    def get_html(self, address):
        return urllib3.PoolManager().request('GET', self._main_address + address).data.decode('utf-8')

    def collect_links_and_categories(self, gender_address):
        html_data = self.get_html(gender_address)
        found = re.findall('<li class="parentCat"><a href="(.*?)"><b></b>.*?<span', html_data,
                           re.MULTILINE | re.DOTALL)

        collector = []
        for element in found:
            html_data = self.get_html(element)
            collector += re.findall('<li class="siblingCat"><a href="(.*?)"><b></b>(.*?) <span', html_data,
                                    re.MULTILINE | re.DOTALL)
        return self.read_subpages(collector)

    def read_subpages(self, collector):
        new_data = []
        for data in collector:
            html_data = self.get_html(data[0])
            cl = re.findall(data[0] + '\?p=(\d*)"', html_data, re.MULTILINE | re.DOTALL)
            if len(cl) > 1:
                for i in range(2, int(max([int(i) for i in cl]))):
                    new_data += [data[0] + '?p=' + str(i)]
        return collector + new_data

    def process(self):
        self.subprocess(self._men_clothes, 'men')
        self.subprocess(self._woman_clothes, 'woman')

    def subprocess(self, container, gender):
        for cat in container:
            html_data = self.get_html(cat[0])
            divs = self.search('<ul class="productsGridList catalog  threeCol">(.*?)</ul>', html_data)
            items = re.findall('href="(.*?)"', divs, re.DOTALL | re.MULTILINE)
            for item in items:
                print(json.dumps(self.process_single_item(item, cat[1], gender)))

    @staticmethod
    def search(pattern, html_data):
        obj = re.search(pattern, html_data, re.DOTALL | re.MULTILINE)
        return "" if obj is None else obj.group(1)

    def process_single_item(self, item, category, gender):
        html_data = self.get_html(item)
        head_title = self.search('<span itemprop="name">(.*?)</span>', html_data).strip().split(' - ')
        item_name = ' - '.join(head_title[:-1])

        return {
            'compositors': self.get_compositors(self.search('Materiał:(.*?)</li>', html_data).strip()),
            'fashion': self.search('Fason:(.*?)</li>', html_data).strip(),
            'fastening': self.search('zapięcie:(.*?)', html_data).strip(),
            'pattern': self.search('wzór:(.*?)', html_data).strip(),
            'brand': self.search('<span itemprop="brand">(.*?)</span>', html_data),
            'name': item_name,
            'color': self.get_color(html_data, head_title[-1]),
            'price': {
                'currency': self.search('currency: "(.*?)"', html_data).strip(),
                'value': self.search('price: "([\.\d]*?)"', html_data)},
            'picture_url': self.search('<a id="image".*?href="(.*?)".*?name="pds.productviewcontent.image.full">',
                                       html_data),
            'item_url': self._main_address + item,
            'available_sizes': re.findall('<option.*?data-quantity=.*?>(.*?)[ <]', html_data,
                                          re.DOTALL | re.MULTILINE),
            'clothes_type': category,
            'decolletage': self.search('Rodzaj dekoltu:(.*?)</li>', html_data).strip(),
            'gender': gender,
            'shop': 'Zalando'
        }

    @staticmethod
    def get_compositors(message):
        compositors = []
        for compositor in message.split(','):
            compositor = compositor.strip().split(' ')
            if len(compositor) == 1:
                continue
            compositors += [{'name': compositor[1], 'percentage_value': compositor[0]}]
        return compositors

    def get_color(self, html_data, first_color):
        colors_ul = self.search('<ul class="colorList left">(.*?)</ul>', html_data)
        if colors_ul == '':
            return "[('" + first_color + "', '')]"

        colors = re.findall('<img src="(.*?)" .*? title="(.*?)" />', colors_ul, re.MULTILINE | re.DOTALL)

        color_str = '['
        for color in colors:
            color_str += "('" + color[1].split(' - ')[-1] + "', '" + color[0] + "'), "
        return color_str[:-2] + ']'
