from sly import Parser
from lexer_Nbee import LangLexer

class LangParser(Parser):
    tokens = LangLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('right', UMINUS),
        )

    def __init__(self):
        self.variables_n = { }

    @_('')
    def statement(self, p):
        pass

    @_('STRING IS expr')
    def statement(self, p):
        self.variables_n[p.STRING] = p.expr

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr DIVIDE expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

    @_('NUMBER PLUS NUMBER')  
    def expr(self, p):
        return  p.NUMBER0 + p.NUMBER1

    @_('NUMBER MINUS NUMBER')  
    def expr(self, p):
        return  p.NUMBER0 + p.NUMBER1

    @_('NUMBER DIVIDE NUMBER')  
    def expr(self, p):
        return  p.NUMBER0 / p.NUMBER1

    @_('NUMBER TIMES NUMBER')  
    def expr(self, p):
        return  p.NUMBER0 * p.NUMBER1

    @_('NUMBER % NUMBER')  
    def expr(self, p):
        return  p.NUMBER0 % p.NUMBER1

    @_('expr "%" expr')
    def expr(self, p):
        return ('%', p.expr0, p.expr1)

    @_('expr IN expr BOOL')
    def statement(self, p):
        return ('if_bool', p.expr1, p.expr2)
   
   @_('expr IS STRING')
    def expr(self, p):
        self.variables_n[p.expr] = p.STRING

    @_('expr IS NUMBER')
    def expr(self, p):
        self.variables_n[p.expr] = p.NUMBER

    @_('expr IS BOOL')
    def expr(self, p):
        self.variables_n[p.expr] = True;

    @_('NUMBER "." NUMBER')  
    def expr(self, p):
        return  float((f"{p.NUMBER0}.{p.NUMBER1}"))

    @_('expr AND expr')
    def expr(self, p):
        return ('and', p.expr0, p.expr1)

    @_('expr OR expr')
    def expr(self, p):
        return ('or', p.expr0, p.expr1)

    @_('NOT expr')
    def expr(self, p):
        return ('!', p.expr)

    @_('INCREASE var')
    def var_assign(self, p):
        return ('var_assign', p.var, ('+', ('var', p.var), 1))

    @_('DECREASE var')
    def var_assign(self, p):
        return ('var_assign', p.var, ('-', ('var', p.var), 1))


    @_('expr SMALLER expr')
    def expr(self, p):
        return ('<', p.expr0, p.expr1)

    @_('expr BIGGER expr')
    def expr(self, p):
        return ('>', p.expr0, p.expr1)

    @_('PRINT expr')
    def statement(self, p):
        return ('print', p.expr)

    @_('PRINT STRING')
    def statement(self, p):
        return ('print', p.STRING)

    @_('empty')
    def expr(self, p):
        return []

    if __name__ == '__main__':
    lexer = IniLexer()
    parser = IniParser()
    env = {}
    while True:
        try:
            text = input('test > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)