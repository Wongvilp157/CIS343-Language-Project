##---start AI code---
import os
import sys

# Add the project's src/ folder (two levels up from test/lab2/) to the import path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "src"))

from token_type import TokenType
from guava_token import Token
from expr import Expr, Visitor, Binary, Unary, Literal, Grouping, Logical, Postfix
from ast_printer import AstPrinter
##---end AI code---

def main():
    # Expression: (++1 + 2++) * (--3 - 4--)
    expression_4 = Binary(
        Grouping(
            Binary(
                Unary(Token(TokenType.PLUS_PLUS, "++", None, 1), Literal(1.0)),
                Token(TokenType.PLUS, "+", None, 1),
                Postfix(Literal(2.0), Token(TokenType.PLUS_PLUS, "++", None, 1))
            )
        ),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(
            Binary(
                Unary(Token(TokenType.MINUS_MINUS, "--", None, 1), Literal(3.0)),
                Token(TokenType.MINUS, "-", None, 1),
                Postfix(Literal(4.0), Token(TokenType.MINUS_MINUS, "--", None, 1))
            )
        )
    )

    ##---start AI code---
    # Instantiate the printer and print the resulting string representation
    printer = AstPrinter()
    ##---end AI code---
    print("\nExample 4 (++ and -- with postfix operations)")
    print(printer.print_expr(expression_4))

if __name__ == "__main__":
    main()