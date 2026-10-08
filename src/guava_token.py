from token_type import TokenType


class Token:
    def __init__(self, type: TokenType, lexeme, literal, line):
        # TODO: store type, lexeme, literal, and line as public attributes.
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        # TODO: return a string containing the type, lexeme, and literal.
        ## ---start AI code---
        return f"{self.type} {self.lexeme} {self.literal}"
        ## ---end AI code---
    