from enum import Enum

TokenType = Enum(
    'TokenType',
    [
        ## Single Character
        'LEFT_PAREN', 'RIGHT_PAREN', 'LEFT_BRACE', 'RIGHT_BRACE',
        'COMMA', 'DOT', 'MINUS', 'PLUS', 'SEMICOLON', 'SLASH', 'STAR',

        ## One or two character(s)
        'BANG', 'BANG_EQUAL',
        'EQUAL', 'EQUAL_EQUAL',
        'GREATER', 'GREATER_EQUAL',
        'LESS', 'LESS_EQUAL',
        'PLUS_PLUS', 'MINUS_MINUS',

        ## Literals
        'IDENTIFIER', 'STRING', 'NUMBER',

        ## Keywords
        'AND', 'CLASS', 'ELSE', 'FALSE', 'FUN', 'FOR', 'IF', 'NULL', 'OR',
        'PRINT', 'RETURN', 'SUPER', 'THIS', 'TRUE', 'VAR', 'WHILE',

        'EOF'
    ]
)