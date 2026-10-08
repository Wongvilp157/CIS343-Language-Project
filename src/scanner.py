from error_handler import ErrorHandler
from lox_token import Token
from token_type import TokenType


class Scanner:
    def __init__(self, source):
        self.source = source
        # TODO: initialize the scanner's state.
        self.tokens = list()
        self.start = 0
        self.current = 0
        self.line = 1

    keywords = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "fun": TokenType.FUN,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE
    }

    def scan_tokens(self):
        """Return a list of Token objects, ending with one EOF token.

        Report lexical errors through ErrorHandler.error(line, message).
        Scanning begins at line 1. Ignore whitespace and // comments.
        """
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens
    
    def is_at_end(self):
        return self.current >= len(self.source)
    
    def scan_token(self):
        c = self.advance()
        match c:
            ## Single Characters
            ##---start AI code---
            case '(': self.add_token(TokenType.LEFT_PAREN)
            case ')': self.add_token(TokenType.RIGHT_PAREN)
            case '{': self.add_token(TokenType.LEFT_BRACE)
            case '}': self.add_token(TokenType.RIGHT_BRACE)
            case ',': self.add_token(TokenType.COMMA)
            case '.': self.add_token(TokenType.DOT)
            case '-': self.add_token(TokenType.MINUS)
            case '+': self.add_token(TokenType.PLUS)
            case ';': self.add_token(TokenType.SEMICOLON)
            case '*': self.add_token(TokenType.STAR)
            ##--end AI code---

            ## Operators
            ##---start AI code---
            case '!': self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            case '=': self.add_token(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case '<': self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            case '>': self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            ##--end AI code---

            ## Longer Lexemes (like division)
            ##---start AI code---
            case '/':
                if self.match('/'):
            # A comment goes until the end of the line.
                    while self.peek() != '\n' and not self.is_at_end():
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            ##--end AI code---

            ## Meaningless lexemes
            case ' ': pass
            case '\r': pass
            case '\t': pass
            case '\n': 
                self.line += 1
                pass
            
            ## String Literals
            case '"': 
                self.string()
                pass
            
            ## Identifers and Reserved Words


            ## Default
            case _: 
                if self.is_digit(c):
                    self.number()
                elif self.is_alpha(c):
                    self.identifier()
                else:
                    ErrorHandler.error(self.line, "Unexpectected character.")
    
    def advance(self):
        c = self.source[self.current]
        self.current += 1
        return c

    def add_token(self, type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    def match(self, expected):
        if self.is_at_end():
            return False
        
        if self.source[self.current] != expected:
            return False
        
        self.current += 1
        return True
    
    def peek(self):
        if self.is_at_end():
            return '\0'
        
        return self.source[self.current]
    
    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.is_at_end():
            ErrorHandler.error(self.line, "Unterminated string.")
            return
        
        ## The closing "
        self.advance()

        ## Trim the surrounding quotation marks
        starting_quote = self.start + 1
        ending_quote = self.current - 1
        value = self.source[starting_quote:ending_quote]
        self.add_token(TokenType.STRING, value)

    def is_digit(self, c):
        return c >= '0' and c <= '9'
    
    def number(self):
        while self.is_digit(self.peek()):
            self.advance()

        ## Look for a fractional part
        if self.peek() == '.' and self.is_digit(self.peek_next()):
            ## Consume the "."
            self.advance()

            while self.is_digit(self.peek()):
                self.advance()

        self.add_token(TokenType.NUMBER, float(self.source[self.start:self.current]))

    def peek_next(self):
        peek_current = self.current + 1
        if peek_current >= len(self.source):
            return '\0'
        return self.source[peek_current]
    
    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()

        text = self.source[self.start:self.current]
        type = self.keywords.get(text)
        if type == None:
            type = TokenType.IDENTIFIER
        self.add_token(type)

    def is_alpha(self, c):
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or (c == '_')
    
    def is_alpha_numeric(self, c):
        return self.is_alpha(c) or self.is_digit(c)

        
