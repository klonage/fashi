import sys
import reserved
import answear
import zalando

__author__ = 'Marcin Kolny'


class UnsupportedBackend:
    def __init__(self, name):
        self._name = name

    def process(self):
        print("unsupported backend", self._name)


def get_backend(shop_backend):
    backends = {
        "reserved": reserved.ReservedBackend(),
        "zalando": zalando.ZalandoBackend()
    }
    return backends[shop_backend] if shop_backend in backends else UnsupportedBackend(shop_backend)


proc_first = True
for backend in sys.argv[1:]:
    print('[')
    b = get_backend(backend)
    if proc_first:
        proc_first = False
    else:
        print(',')
    get_backend(backend).process()
    print(']')

