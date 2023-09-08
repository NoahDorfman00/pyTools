class script():
    __argc = 0
    __argTypes = []
    __retType = []

    def __checkParams(self, *args):
        if len(args) != argc:
            print(f'Expecting {argc} arguments, received {len(args)}!')
            return False
        for a in len(range(args)):
            if type(args[a]) is not argTypes[a]:
                print(f'Type {type(args[a])} of argument {a}, {args[a]}, does not match expected type {argTypes[a]}!')
                return False
        return True

    def __call__(self, *args):
        print("No 'run' method defined in script!")