class SyntaxNode(object):

    def eval(self, scope):
        pass

class Program(SyntaxNode):

    def __init__(self, elements):
        self.elements = elements

    def eval(self, scope):
        return map(lambda e: e.eval(scope), self.elements)[-1]

class List(SyntaxNode):

    def __init__(self, cells):
        self.cells = cells

    def eval(self, scope):
        function = self.cells[0].eval(scope)
        return function(scope, self.cells[1:])

class Boolean(SyntaxNode):

    def __init__(self, text):
        self.text = text

    def eval(self, scope):
        return self.text == '#t'

class Integer(SyntaxNode):

    def __init__(self, text):
        self.text = text

    def eval(self, scope):
        return int(self.text)

class Identifier(SyntaxNode):

    def __init__(self, text):
        self.text = text

    def eval(self, scope):
        return scope[self.text]
