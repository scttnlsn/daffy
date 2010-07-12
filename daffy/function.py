class Function(object):

    def __init__(self, scope, body, params = None):
        self.scope = scope
        self.body = body 
        self.params = params

    def __call__(self, scope, cells):
        values = map(lambda x: x.eval(scope), cells)
        if callable(self.body):
            return self.body(*values)
        else:
            import scope
            inner = scope.Scope(self.scope)
            for i, param in enumerate(self.params):
                inner[param] = values[i]
            return map(lambda x: x.eval(inner), self.body)[-1]

class Syntax(Function):

    def __call__(self, scope, cells):
        return self.body(scope, cells)
