class SampleCode:
    def __init__(self, name):
        self.name = name

    def func_hello(self, msg: str) -> int:
        if not msg:
            return 1
        else:
            print('Hi, {}. You have message: {}'.format(self.name, msg))
            return 0
