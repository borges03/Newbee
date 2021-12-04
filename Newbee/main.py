from parser_Nbee import LangParser
from lexer_Nbee import LangLexer

def main():
    lexer = LangLexer()
    while True:
        text = input("newbie >> ")
        tokens = lexer.tokenize(text) # Creates a generator of tokens
        parser = LangParser()
        parser.parse(tokens) # The entry point to the parser

if __name__ == '__main__':
    main()