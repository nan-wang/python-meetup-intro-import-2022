from jina import Executor, requests


class FooExecutor(Executor):
    @requests
    def foo(self, **kwargs):
        print('this is a single-file executor')
