import parser
import scope

class Daffy(object):

    def run(self, path):
        with open(path) as f:
            program = self.parse(f.read())
            return program.eval(scope.TopLevel())

    def parse(self, text):
        return parser.Parser().parse(text)
