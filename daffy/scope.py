import function

class Scope(object):

    def __init__(self, parent = None):
        self.parent = parent or {}
        self.symbols = {}

    def __getitem__(self, name):
        if name in self.symbols:
            return self.symbols[name]
        else:
            return self.parent[name]

    def __setitem__(self, name, value):
        self.symbols[name] = value

    def define(self, name, func):
        self[name] = function.Function(self, func)

    def syntax(self, name, func):
        self[name] = function.Syntax(self, func)

class TopLevel(Scope):

    def __init__(self):
        super(TopLevel, self).__init__()

        def do_define(scope, cells):
            scope[cells[0].text] = cells[1].eval(scope)
        self.syntax('define', do_define)

        def do_lambda(scope, cells):
            names = map(lambda x: x.text, cells[0].cells)
            return function.Function(scope, cells[1:], params = names)
        self.syntax('lambda', do_lambda)

        def do_if(scope, cells):
            which = cells[1] if cells[0].eval(scope) else cells[2]
            return which.eval(scope)
        self.syntax('if', do_if)

        self.define('+', lambda a, b: a + b)
        self.define('-', lambda a, b: a - b)
        self.define('*', lambda a, b: a * b)
        self.define('/', lambda a, b: a / b)
        self.define('=', lambda a, b: a == b)

    def __getitem__(self, name):
        if name in self.symbols:
            return self.symbols[name]
        else:
            return None
