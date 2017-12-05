import sys
import re
import inspect


__author__ = 'Jabrail Lezgintsev (joe513)'
__github__ = 'https://github.com/joe513'
__email__ = 'lezgintsev13@yandex.ru'


class ModuleAnalysis:

    def __init__(self, _module):
        self.module = _module
        self.pattern = re.compile('__(.*)__')

    def display_available_functions(self):

        print('Function: ', '                  Result:')
        for func in self.module.__dict__:
            if type(getattr(self.module, str(func))) == "<class 'builtin_function_or_method'>":
                try:
                    letters_c = len(repr(func))
                    x = 30 - letters_c
                    print('%s %s: %s' % (func, ' ' * x, getattr(self.module, str(func))()))
                except (TypeError, IndexError):
                    continue

    def get_all_attrs(self):
        return self.module.__dict__

    def get_own_attrs(self, dict_or_list='dict'):

        own_attrs = {attr: getattr(self.module, attr) for attr in self.get_all_attrs() \
                     if not re.match(self.pattern, str(attr))}

        return own_attrs if dict_or_list == 'dict' else list(own_attrs.keys())

    def get_all_classes(self):
        classes = [attr for attr in dir(self.module) if inspect.isclass(getattr(self.module, attr))]
        return classes


if __name__ == '__main__':
    my = ModuleAnalysis(inspect)
    print(my.get_own_attrs())