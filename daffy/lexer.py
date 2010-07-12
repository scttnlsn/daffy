from ply.lex import lex

class Lexer(object):

    tokens = [
        'LPAREN', 'RPAREN',
        'TRUE', 'FALSE',
        'INTEGER','IDENTIFIER',
    ]

    t_ignore = ' \t'

    def __init__(self, **kwargs):
        self.lexer = lex(
            object = self,
            debuglog = None,
            **kwargs)

    def input(self, text):
        self.lexer.input(text)

    def token(self):
        return self.lexer.token()

    def t_LPAREN(self, t):
        r'\('
        return t

    def t_RPAREN(self, t):
        r'\)'
        return t

    def t_TRUE(self, t):
        r'\#t'
        return t

    def t_FALSE(self, t):
        r'\#f'
        return t

    def t_INTEGER(self, t):
        r'0|[1-9][0-9]*'
        return t

    def t_IDENTIFIER(self, t):
        r'[^\(\) \t\n\r]+'
        return t

    def t_newline(self, t):
        r'[\n\r]+'

    def t_error(self, t):
        print 'lex error'
        print t.value[0]
