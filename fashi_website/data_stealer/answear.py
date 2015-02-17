import re
import urllib3

__author__ = 'Marcin Kolny'


class AnswearBackend:
    _main_address = 'http://answear.com/'
    _translator = {'bielizna': 'lingerie',
                   'bluzy': 'blouse',
                   'jeansy': 'jeans'}

    def __init__(self, is_first):
        self.is_first = is_first

        self.read_links()

    def read_links(self):
        html_data = urllib3.PoolManager().request('GET', self._main_address).data.decode('utf-8')

        self._man_links = self.get_links('ON', html_data)
        self._woman_links = self.get_links('ONA', html_data)

        print(self._woman_links)
        print(self._man_links)

    def get_links(self, gender, html_data):
        return [self._main_address + l for l in re.findall('<a href="(.*?)".*?title=.*?>', re.search(
            '<li><a href="/p/on.*?">' + gender + '</a>.*?</a></h4>(.*?)<div class="list single clearfix">',
            html_data,
            re.MULTILINE | re.DOTALL).group(1), re.MULTILINE | re.DOTALL)]


    def process(self):
        print('todo')
