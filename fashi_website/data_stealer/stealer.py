import sys
import reserved

__author__ = 'Marcin Kolny'


class UnsupportedBackend:
    def __init__(self, name):
        self._name = name

    def process(self):
        print("unsupported backend", self._name)


def get_backend(shop_backend):
    backends = {
        "reserved": reserved.ReservedBackend(True)
    }
    return backends[shop_backend] if shop_backend in backends else UnsupportedBackend(shop_backend)


proc_first = True

for backend in sys.argv[1:]:
    print('[')
    get_backend(backend).process()
    print(']')