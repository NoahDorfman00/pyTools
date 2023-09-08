import pytoolslib.script
import importlib
import os

class manager:
    __scripts = {}

    def __registerModule(self, path, filename):
        if filename != '__init__.py' and filename[-3:] == '.py':
            path = path.replace('/', '.') + '.' + filename[:-3]
            print(path)
            c = getattr(importlib.import_module(path), filename[:-3])
            if issubclass(c, pytoolslib.script):
                print("It's a script!")
                self.__scripts[filename[:-3]] = c()
    
    def registerModules(self, scriptsPath):
        allStr = "__all__ = "
        allIdx = 0
        init = scriptsPath + "__init__.py"
        if os.path.isfile(init):
            f = open(init, 'r')
            lines = f.readlines()
            for l in range(len(lines)):
                line = lines[l]
                if line.find("__all__"):
                    openI = line.find('[')
                    closeI = line.find(']')
                    names = line[openI+1:closeI].split(',')
                    for n in range(len(names)):
                        names[n] = names[n].strip(' ').strip('\'').strip('\"')
        else:
        
        f = open(init, 'w')
        lines[allIdx] = allStr


        for module in os.listdir(scriptsPath):
            path = os.path.join(scriptsPath, module)
            if os.path.isfile(path):
                self.__registerModule(scriptsPath, module)
            else:
                for submodule in os.listdir(path):
                    subpath = os.path.join(path, submodule)
                    self.__registerModule(path, submodule)