from sly import Parser
from lexer_Nbee import LangLexer

class LangParser(Parser):
    tokens = LangLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
        ('right', BIGGER, SMALLER),
        ('right', AND, OR),
        )

    var = []
    exp_var = []

    def __init__(self):
        self.variables = {}

    @_('')
    def statement(self, p):
        pass

    @_('expr') #working
    def statement(self, p):
        print(p.expr)

    @_('expr PLUS term') #working
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term') #working
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor') #working
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor') #working
    def term(self, p):
        if(p.factor == 0): return "Error: Dividing by 0"
        return p.term / p.factor

    @_('term EXP factor')
    def term(self, p):
        return p.term ** p.factor

    @_('term MOD factor')  # working
    def term(self, p):
        return p.term % p.factor

    @_('NUMBER SMALLER NUMBER')
    def term(self, p):
        return p.NUMBER0 < p.NUMBER1

    @_('NUMBER BIGGER NUMBER')
    def term(self, p):
        return p.NUMBER0 > p.NUMBER1

    @_('NUMBER EQ2 NUMBER')
    def term(self, p):
        return p.NUMBER0 == p.NUMBER1

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER') #working
    def factor(self, p):
        return int(p.NUMBER)

    @_('NUMBER "." NUMBER') #working
    def factor(self, p):
        return float((f"{p.NUMBER0}.{p.NUMBER1}"))

    @_('LPAREN expr RPAREN') #working
    def factor(self, p):
        return p.expr

    @_('factor LT factor') #working
    def condition(self, p):
        return p.factor0 < p.factor1

    @_('factor GT factor') #working
    def condition(self, p):
        return p.factor0 > p.factor1

    @_('factor EQEQ factor')
    def condition(self, p):
        return p.factor0 == p.factor1

    @_('condition AND condition') #working
    def expr(self, p):
        left = p.condition0 #if this is true
        right = p.condition1 # and true
        if (left == True and right == True): result = True
        elif (left != True and right == True):result = False
        elif (right != True and left == True):result = False
        elif (right != True and left != True):result = False
        return result

    @_('condition OR condition')
    def expr(self, p):
        left = p.condition0
        right = p.condition1
        if(left == True and right == True): result = True
        elif(left != True and right == True): result = True
        elif(right != True and left == True): result = True
        elif(right != True and left != True): result = False
        return result

    @_('NOT condition')
    def expr(self, p):
        result = p.condition
        if result == True:  result = False
        elif result == False: result = True
        else: result = "Error"
        return result

    @_('PRINT expr')
    def statement(self, p):
        if(p.expr in self.variables):
            result = self.variables[p.expr]
            return result
        else:
            return p.expr

    @_('ID IS STRING') #save variables with strings
    def statement(self, p):
        for i in LangParser.var:
            if (p.ID in i):
                i[p.ID] = p.STRING
            else:
                self.variables[p.ID] = p.STRING
                LangParser.var = LangParser.var + [self.variables]

    @_('ID IS factor') # Save variables with numbers
    def statement(self, p):
        for i in LangParser.var:
            if(p.ID in i):
                i[p.ID] = p.factor
            else:
                self.variables[p.ID] = p.factor
                LangParser.var = LangParser.var +[self.variables]

    @_('ID') # Variable Print
    def statement(self, p):
        for i in LangParser.var:
            if(p.ID in i):
                result = i[p.ID]
                return result
            else:
                result = 'variable not found'
                return result

    # @_('STRING')
    # def statement(self,p):
    #     print(p.STRING)

    @_('var_as') #helper function
    def statement(self, p):
        return p.var_as

    @_('ID EQUALS factor') #Adds exp var to exp_var array
    def var_as(self, p):
        self.variables[p.ID] = p.factor
        LangParser.exp_var = LangParser.exp_var + [self.variables]
        return LangParser.exp_var

    @_('FOR var_as TO expr THEN statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_as, p.expr), p.statement)

    @_('FOR var_as IN expr THEN statement')
    def statement(self, p):
        return ('for_loop', ('for_loop_setup', p.var_as, p.expr), p.statement)

    @_('IF condition THEN statement ELSE statement')
    def statement(self, p):
        return ('if_stmt', p.condition, ('branch', p.statement0, p.statement1))

    @_('WHILE condition THEN statement')
    def statement(self, p):
        return('while_loop', ('while_loop_setup', p.condition('branch', p.statement)))