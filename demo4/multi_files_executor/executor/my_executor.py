from jina import Executor, requests

from .utils.helper import bar_var


class BarExecutor(Executor):
    @requests
    def bar(self, **kwargs):
        print(f'this is a multi-file executor. i get help var: {bar_var}')