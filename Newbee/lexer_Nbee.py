
from sly import Lexer

class LangLexer(Lexer):
    tokens = {  NUMBER, STRING,  PLUS, TIMES, MINUS, DIVIDE, LPAREN, RPAREN, FOR, WORD, IS, EQUALS,
             SMALLER, BIGGER, PRINT, INCREASE, DECREASE, OR, AND, NOT, BOOL, IN, IF, FOR, ELSE, WHILE, PRINT, COMMENT, SIZE}
    ignore = ' \t'
    ignore_newline = r'\n+'

    # Tokens
    STRING = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'

    # The definition of each token in a regex pattern
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    EQUALS = r'\='
    LPAREN = r'\('
    RPAREN = r'\)'
    SMALLER = r'\<'
    BIGGER = r'\>'
    INCREASE = r'increase'
    DECREASE = r'decrease'
    IS = r'\=\:'
    OR = r'or'
    AND = r'and'
    NOT = r'not'
    BOOL = r'\?'
    IN = r'in'
    IF = r'if'
    FOR = r'for'
    ELSE = r'else'
    WHILE = r'while'
    PRINT = r'print'
    COMMENT = r'comment'
    SIZE = r'size'

    # Any literals we want to ignore
    ignore = ' \t'
    # Any literals we did not define as tokens, will be available for usage in the Parser
     literals = {'=', '+', '-', '/', '*',
                '(', ')', ',', '{', '}',
                '%', '[', ']', '!', '&',
                '|', '^', '?', ':', '~',
                '.'}


    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def remove_quotes(self, text: str):
        if text.startswith('\"') or text.startswith('\''):
            return text[1:-1]
        return text

    def t_error(t):
    print("Illegal character '%s'" % t.value[0])  # print error message with causing character
    t.lexer.skip(1)  # skip invalid character

    