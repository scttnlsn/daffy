import ast
import lexer
import tempfile

from ply.yacc import yacc

class ParserException(Exception):

    def __init__(self, error):
        self.error = error

class Parser(object):

    start = 'program'

    def __init__(self, **kwargs):
        self.lexer = lexer.Lexer(**kwargs)
        self.tokens = self.lexer.tokens
        self.parser = yacc(
            debug = False,
            debuglog = None,
            module = self,
            outputdir = tempfile.gettempdir())

    def parse(self, text):
        return self.parser.parse(text, lexer = self.lexer.lexer)

    def handle_error(self, error):
        raise ParserException(error)

    def p_program(self, p):
        """
        program : cells
        """
        p[0] = ast.Program(p[1])

    def p_cells(self, p):
        """
        cells : necells
              | emptylist
        """
        p[0] = p[1]

    def p_necells(self, p):
        """
        necells : cell
                | necells cell
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_cell(self, p):
        """
        cell : list
             | atom
        """
        p[0] = p[1]

    def p_list(self, p):
        """
        list : LPAREN necells RPAREN
        """
        p[0] = ast.List(p[2])

    def p_atom(self, p):
        """
        atom : datum
             | identifier
        """
        p[0] = p[1]

    def p_datum(self, p):
        """
        datum : boolean
              | integer
        """
        p[0] = p[1]

    def p_boolean(self, p):
        """
        boolean : TRUE
                | FALSE
        """
        p[0] = ast.Boolean(p[1])

    def p_integer(self, p):
        """
        integer : INTEGER
        """
        p[0] = ast.Integer(p[1])

    def p_identifier(self, p):
        """
        identifier : IDENTIFIER
        """
        p[0] = ast.Identifier(p[1])

    def p_emptylist(self, p):
        """
        emptylist :
        """
        p[0] = []

    def p_error(self, p):
        raise ParserException(p)
