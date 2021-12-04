
from sly import Lexer

class LangLexer(Lexer):
    tokens = {NUMBER, STRING,  PLUS, TIMES, MINUS, DIVIDE, MOD, EXP,LPAREN, RPAREN, FOR, IS, EQUALS, EQ2, EQEQ,
             SMALLER, BIGGER,  GT, LT, PRINT, OR, AND, NOT, THEN, IN, IF, FOR, TO, ELSE, WHILE, PRINT, ID}
    ignore = ' \t'
    ignore_newline = r'\n+'

    # Tokens
    STRING = r'\".*?\"'
    NUMBER = r'\d+'

    # The definition of each token in a regex pattern
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    MOD = r'%'
    EQUALS = r'\='
    EQEQ = r'\=='
    LPAREN = r'\('
    RPAREN = r'\)'
    LT = r'\<'
    GT = r'\>'
    EXP = r'\^'

    # Any literals we want to ignore
    # Any literals we did not define as tokens, will be available for usage in the Parser
    literals = {',', '{', '}', '[', ']', '!', '&', '|', '^', '?', ':', '~', '.'}

    # Special cases
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['not'] = NOT
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['or'] = OR
    ID['and'] = AND
    ID['is'] = IS
    ID['then'] = THEN
    ID['in'] = IN
    ID['for'] = FOR
    ID['to'] = TO
    ID['print'] = PRINT
    ID['smaller'] = SMALLER
    ID['bigger'] = BIGGER
    ID['equal?'] = EQ2

    @_(r"(0|[1-9][0-9]*)")
    def NUMBER(self, n):
        n.value = int(n.value)
        return n
    #
    # @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')
    # def STRING(self, n):
    #     n.value = self.remove_quotes(n.value)
    #     return n

    #Remove quotes '' "" from strings
    def remove_quotes(self, text: str):
        if text.startswith('\"') or text.startswith('\''):
            return text[1:-1]
        return text

    def t_error(n):
        print("Illegal character: '%s'" % t.value[0])  #Print Error with char
        n.lexer.skip(1)  #skip character

    