print(f'import {__name__}')


from .module_bar import bar_var


def print_foo():
    print(f'{__name__}: this is foo, this is imported: {bar_var}')