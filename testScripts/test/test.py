from pyTools import script
class test(script):
    __argc = 2
    __argTypes = [int, int]
    __retType = [int]
    def __call__(self, *args):
        __checkParams(self, *args)
        return args[0] + args[1]