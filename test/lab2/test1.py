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
    ## Expression: (523 + 12 - 53 * 2) / 2
    expression_1 = Binary(
        Grouping(
            Binary(
                Binary(
                    Literal(523.0),
                    Token(TokenType.PLUS, "+", None, 1),
                    Literal(12.0)
                ),
                Token(TokenType.MINUS, "-", None, 1),
                Binary(
                    Literal(53.0),
                    Token(TokenType.STAR, "*", None, 1),
                    Literal(2.0)
                )
            )
        ),
        Token(TokenType.SLASH, "/", None, 1),
        Literal(2.0)
    )

    ##---start AI code---
    # Instantiate the printer and print the resulting string representation
    printer = AstPrinter()
    ##---end AI code---
    print("\nExample 1 (all arthimic operators)")
    print(printer.print_expr(expression_1))

if __name__ == "__main__":
    main()